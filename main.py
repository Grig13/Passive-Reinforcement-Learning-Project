# import gym
#
# env = gym.make('FrozenLake-v1')
#
# def random_agent():
#     total_reward = 0
#     num_episodes = 5
#
#     for episode in range(num_episodes):
#         state = env.reset()
#         episode_reward = 0
#
#         while True:
#             action = env.action_space.sample()
#             step_result = env.step(action)
#
#             if len(step_result) == 5:
#                 next_state, reward, done, _, info = step_result
#                 action_prob = info.get('prob', None)
#                 print(f"Action Probability: {action_prob}")
#             else:
#                 print(f"Step result: {step_result}")
#
#             episode_reward += reward
#
#             print(f"Episode {episode + 1}, State: {state}, Action: {action}, Reward: {reward}, Done: {done}, Total Reward: {episode_reward}")
#
#             if done:
#                 total_reward += episode_reward
#                 break
#
#     return total_reward
#
# total_reward = random_agent()
# print(f"Total Reward for all episodes: {total_reward}")
#
# env.close()
import numpy as np

# import numpy as np
#
# class PassiveAgent:
#     def __init__(self):
#         self.q_values = {}
#
#     def learn_from_dataset(self, dataset):
#         for state, action, reward in dataset:
#             state_hashable = (state[0], tuple(sorted(state[1].items())))  # Convert dictionary to hashable tuple
#             if (state_hashable, action) not in self.q_values:
#                 self.q_values[(state_hashable, action)] = 0.0
#             self.q_values[(state_hashable, action)] += reward
#
#     def choose_action(self, state):
#         # For simplicity, choose the action with the highest Q-value
#         actions = [0, 1, 2, 3]  # Assuming four possible actions
#         state_hashable = (state[0], tuple(sorted(state[1].items())))  # Convert dictionary to hashable tuple
#         q_values_state = [self.q_values.get((state_hashable, a), 0.0) for a in actions]
#         return np.argmax(q_values_state)


# def generate_dataset(num_episodes=100):
#     dataset = []
#     for _ in range(num_episodes):
#         state = (0, {'prob': 1})
#         action = np.random.choice([0, 1, 2, 3])
#         reward = np.random.rand()
#         dataset.append((state, action, reward))
#     return dataset
#
# def main():
#     agent = PassiveAgent()
#
#     dataset = generate_dataset()
#
#     agent.learn_from_dataset(dataset)
#
#     test_episodes = 5
#     total_reward = 0.0
#     for _ in range(test_episodes):
#         state = (0, {'prob': 1})
#         action = agent.choose_action(state)
#         print(f"State: {state}, Action: {action}")
#
#         reward = np.random.rand()
#         total_reward += reward
#
#         print(f"Reward: {reward}")
#     print(f"Total Reward for all test episodes: {total_reward}")
#
# if __name__ == "__main__":
#     main()


from environment import SpookyMansion

env = SpookyMansion(size=4, ghost_probability=0.3, diamond_probability=0.2)
print(env.mansion)
print(env.step("right"))
print(env.inspect())
print(env.step("down"))
print(env.step("left"))
