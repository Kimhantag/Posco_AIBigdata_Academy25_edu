import torch
import torch.nn as nn
import torch.optim as optim

class A3C():
    def __init__(self, 
                 actor_critic,
                 clip_param,
                 max_grad_norm=None,
                 lr=None,
                 eps=None):

        self.actor_critic = actor_critic
        self.clip_param = clip_param
        self.max_grad_norm = max_grad_norm

        # Adam 최적화기를 사용합니다
        self.optimizer = optim.Adam(actor_critic.parameters(), lr=lr, eps=eps)

    def zero_grad(self):
        self.optimizer.zero_grad()    
        
    def step(self):
        self.optimizer.step()
        
    def update(self, rollouts):
        # 각각의 rollout으로부터 반환된 값과 예측된 값 사이의 임시 차이를 계산합니다
        value_loss_epoch = 0
        action_loss_epoch = 0
        dist_entropy_epoch = 0

        for sample in rollouts:
            obs_batch, recurrent_hidden_states_batch, actions_batch, \
                value_preds_batch, return_batch, masks_batch, old_action_log_probs_batch, \
                    adv_targ = sample

            # 행동을 평가하고, 로그 확률, 엔트로피, 가치를 얻습니다
            values, action_log_probs, dist_entropy, _ = self.actor_critic.evaluate_actions(
                obs_batch, recurrent_hidden_states_batch, masks_batch, actions_batch)
            
            # 임시 차이(advantages) 계산
            advantages = return_batch - values

            # 행동 로스(action loss) 계산
            action_loss = -(advantages.detach() * action_log_probs).mean()

            # 가치 로스(value loss) 계산
            value_loss = 0.5 * (return_batch - values).pow(2).mean()

            # 엔트로피 보너스를 사용하여 탐험을 장려
            dist_entropy = dist_entropy.mean()

            # 업데이트를 위해 그래디언트 초기화
            self.optimizer.zero_grad()

            # 로스 계산
            total_loss = (value_loss + action_loss - dist_entropy).mean()
            total_loss.backward()

            # 그래디언트 클리핑을 적용하고 최적화 스텝 수행
            nn.utils.clip_grad_norm_(self.actor_critic.parameters(), self.max_grad_norm)
            self.optimizer.step()

            # 에폭 로스를 집계합니다
            value_loss_epoch += value_loss.item()
            action_loss_epoch += action_loss.item()
            dist_entropy_epoch += dist_entropy.item()

        # 업데이트 횟수로 나누어 평균을 구합니다
        num_updates = len(rollouts)
        value_loss_epoch /= num_updates
        action_loss_epoch /= num_updates
        dist_entropy_epoch /= num_updates

        return value_loss_epoch, action_loss_epoch, dist_entropy_epoch
