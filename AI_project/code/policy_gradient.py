#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import torch
import torch.nn as nn
import torch.optim as optim

class PolicyGradient():
    def __init__(self,
                 actor_critic,
                 lr=None,
                 eps=None,
                 max_grad_norm=None):

        self.actor_critic = actor_critic
        self.max_grad_norm = max_grad_norm

        # Adam 최적화기를 사용합니다.
        self.optimizer = optim.Adam(actor_critic.parameters(), lr=lr, eps=eps)

    def zero_grad(self):
        self.optimizer.zero_grad()    
        
    def step(self):
        self.optimizer.step()
        
    def update(self, rollouts):
        value_loss_epoch = 0
        action_loss_epoch = 0
        dist_entropy_epoch = 0

        # Rollout에서 데이터 추출
        obs_batch, actions_batch, return_batch = rollouts

        # 에이전트의 행동 로그 확률과 엔트로피 계산
        _, action_log_probs, dist_entropy = self.actor_critic.evaluate_actions(obs_batch, actions_batch)

        # Policy Gradient 손실 계산: -E[log(pi(a|s))*R]
        action_loss = -(action_log_probs * return_batch).mean()

        # 손실에 대한 그래디언트를 계산하고, 역전파를 수행합니다.
        self.optimizer.zero_grad()
        (action_loss - dist_entropy.mean()).backward()

        # 그래디언트 클리핑을 적용하고 최적화 스텝 수행
        nn.utils.clip_grad_norm_(self.actor_critic.parameters(), self.max_grad_norm)
        self.optimizer.step()

        # 로그 확률의 평균 엔트로피 반환
        dist_entropy_epoch = dist_entropy.mean().item()

        return value_loss_epoch, action_loss_epoch, dist_entropy_epoch

