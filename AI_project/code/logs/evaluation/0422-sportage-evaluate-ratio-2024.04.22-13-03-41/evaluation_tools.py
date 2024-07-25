import os
import numpy as np
import torch
import tools

def evaluate(PCT_policy, eval_envs, timeStr, args, device, eval_freq=100, factor=1):
    PCT_policy.eval()
    obs = eval_envs.reset()
    obs = torch.FloatTensor(obs).to(device).unsqueeze(dim=0)
    all_nodes, leaf_nodes = tools.get_leaf_nodes_with_factor(obs, args.num_processes,
                                                             args.internal_node_holder, args.leaf_node_holder)
    batchX = torch.arange(args.num_processes)
    step_counter = 0
    episode_ratio = []
    episode_reward = []
    episode_length = []
    all_episodes = []

    # 결과 파일 경로 설정 및 디렉터리 생성
    result_path = os.path.join('./logs/evaluation', timeStr)
    os.makedirs(result_path, exist_ok=True)
    result_file_path = os.path.join(result_path, 'result.txt')
    
    with open(result_file_path, 'w') as file:
        while step_counter < eval_freq:
            with torch.no_grad():
                selectedLogProb, selectedIdx, policyDistEntropy, value = PCT_policy(all_nodes, True, normFactor=factor)
            selected_leaf_node = leaf_nodes[batchX, selectedIdx.squeeze()]
            items = eval_envs.packed
            obs, reward, done, infos = eval_envs.step(selected_leaf_node.cpu().numpy()[0][0:6])

            if done:
                if 'ratio' in infos:
                    episode_ratio.append(infos['ratio'])
                if 'counter' in infos:
                    episode_length.append(infos['counter'])
                if 'reward' in infos:
                    episode_reward.append(infos['reward'])

                episode_details = f'Episode {step_counter} ends.\n' \
                                  f'Mean ratio: {np.mean(episode_ratio):.5f}, length: {np.mean(episode_length):.5f}\n' \
                                  f'Mean reward: {np.mean(episode_reward):.5f}, length: {np.mean(episode_length):.5f}\n' \
                                  f'Episode ratio: {infos.get("ratio", 0):.5f}, Episode reward: {infos.get("reward", 0)}, length: {infos.get("counter", 0)}\n\n'
                file.write(episode_details)
                print(episode_details)
                
                all_episodes.append(items)
                step_counter += 1
                obs = eval_envs.reset()

            obs = torch.FloatTensor(obs).to(device).unsqueeze(dim=0)
            all_nodes, leaf_nodes = tools.get_leaf_nodes_with_factor(obs, args.num_processes,
                                                                     args.internal_node_holder, args.leaf_node_holder)
            all_nodes, leaf_nodes = all_nodes.to(device), leaf_nodes.to(device)

        final_result = f"Evaluation using {len(episode_ratio)} episodes\n" \
                       f"Mean ratio {np.mean(episode_ratio):.5f}, Mean reward {np.mean(episode_reward):.5f}, mean length {np.mean(episode_length):.5f}\n"
        file.write(final_result)
        print(final_result)
    
    # Save the test trajectories.
    path = os.path.join(result_path, 'trajs.npy')
    all_episodes = np.array(all_episodes, dtype=object)
    np.save(path, all_episodes)


