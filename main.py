import gym

env = gym.make('FrozenLake-v1')

def random_agent():
    total_reward = 0
    num_episodes = 5

    for episode in range(num_episodes):
        state = env.reset()
        episode_reward = 0

        while True:
            action = env.action_space.sample()
            step_result = env.step(action)

            if len(step_result) == 5:
                next_state, reward, done, _, info = step_result
                action_prob = info.get('prob', None)
                print(f"Action Probability: {action_prob}")
            else:
                print(f"Step result: {step_result}")

            episode_reward += reward

            print(f"Episode {episode + 1}, State: {state}, Action: {action}, Reward: {reward}, Done: {done}, Total Reward: {episode_reward}")

            if done:
                total_reward += episode_reward
                break

    return total_reward

total_reward = random_agent()
print(f"Total Reward for all episodes: {total_reward}")

env.close()
