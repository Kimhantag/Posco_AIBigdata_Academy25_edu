#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

class TRPO():
    def __init__(self, actor_critic, max_kl, damping, lr):
        self.actor_critic = actor_critic
        self.max_kl = max_kl
        self.damping = damping
        self.lr = lr
        self.optimizer = optim.Adam(actor_critic.parameters(), lr=lr)

    def zero_grad(self):
        self.optimizer.zero_grad()    
        
    def step(self):
        self.optimizer.step()
        
    def update(self, rollouts):
        # Policy loss 계산
        advantages = rollouts.returns[:-1] - rollouts.value_preds[:-1]
        log_probs = self.actor_critic.evaluate_actions(rollouts.obs[:-1], rollouts.actions)
        old_log_probs = log_probs.detach()
        policy_ratio = torch.exp(log_probs - old_log_probs)
        policy_loss = -(policy_ratio * advantages).mean()

        # Policy 업데이트를 위한 그래디언트 계산
        self.actor_critic.zero_grad()
        policy_loss.backward(retain_graph=True)
        policy_grad = [p.grad for p in self.actor_critic.parameters()]

        # 켤레 그래디언트 방법을 이용한 자연 그래디언트 계산 (단순화된 예시)
        flat_grad = self._flatten_grads(policy_grad)
        step_direction = self._conjugate_gradient(flat_grad)

        # KL 제약 조건 하에서 스텝 크기 계산
        step_size = torch.sqrt(2 * self.max_kl / (torch.dot(step_direction, self._hessian_vector_product(step_direction)) + 1e-8))

        # 모델 파라미터 업데이트
        old_params = self._get_flat_params()
        new_params = old_params + step_size * step_direction
        self._set_flat_params(new_params)

    def _flatten_grads(self, grads):
        flat_grads = torch.cat([grad.view(-1) for grad in grads])
        return flat_grads

    def _conjugate_gradient(self, flat_grad, cg_iters=10, residual_tol=1e-10):
        x = torch.zeros_like(flat_grad)
        r = flat_grad.clone()
        p = flat_grad.clone()
        rdotr = torch.dot(r, r)

        for i in range(cg_iters):
            _Avp = self._hessian_vector_product(p)
            alpha = rdotr / torch.dot(p, _Avp)
            x += alpha * p
            r -= alpha * _Avp
            new_rdotr = torch.dot(r, r)
            beta = new_rdotr / rdotr
            p = r + beta * p
            rdotr = new_rdotr
            if rdotr < residual_tol:
                break
        return x

    def _hessian_vector_product(self, vector, damping=0.1):
        self.actor_critic.zero_grad()
        kl_div = self._compute_kl_divergence()
        kl_grad = torch.autograd.grad(kl_div, self.actor_critic.parameters(), create_graph=True)
        kl_grad_vector = torch.cat([grad.view(-1) for grad in kl_grad])
        grad_vector_product = torch.dot(kl_grad_vector, vector)
        grad_grad = torch.autograd.grad(grad_vector_product, self.actor_critic.parameters())
        fisher_vector_product = torch.cat([grad.contiguous().view(-1) for grad in grad_grad]).data
        return fisher_vector_product + vector * damping

    def _get_flat_params(self):
        params = torch.cat([param.view(-1) for param in self.actor_critic.parameters()])
        return params

    def _set_flat_params(self, flat_params):
        prev_ind = 0
        for param in self.actor_critic.parameters():
            flat_size = int(np.prod(list(param.size())))
            param.data.copy_(flat_params[prev_ind:prev_ind + flat_size].view(param.size()))
            prev_ind += flat_size

