from environment import SpookyMansion
from agent import QLearningAgent
import matplotlib.pyplot as plt


env = SpookyMansion(size=5, ghost_probability=0.2, diamond_probability=0.1, inspect_impact=0.1, punishment_severity=1.0)

num_actions = len(["left", "right", "up", "down", "inspect"])
agent = QLearningAgent(num_actions)

num_episodes = 10
dataset = env.generate_dataset(num_episodes)
q_values_over_episodes = []

print("Generated Dataset:")
for data in dataset:
    print(data)

for episode in range(num_episodes):
    state = env.reset()
    total_reward = 0
    done = False

    print(f"Episode {episode}/{num_episodes}, Initial State: {state}, Q-Values: {agent.get_q_values(state)}")

    while not done:
        action = agent.choose_action(state)
        next_state, reward, done = env.step(action)

        print(f"Chosen action: {action}, Reward: {reward}, Next State: {next_state}, Q-Values: {agent.get_q_values(next_state)}")

        dataset.append((state, action, reward, next_state, done))
        agent.learn_from_dataset([(state, action, reward, next_state, done)])
        total_reward += reward
        state = next_state

    q_values_over_episodes.append(agent.get_q_values().copy())
    print(f"Episode {episode}/{num_episodes}, Total Reward: {total_reward}")


print("\nLearned Q-values:")
print(agent.get_q_values())

for action_idx in range(agent.num_actions):
    plt.plot(range(num_episodes), [q_values[state][action_idx] for q_values in q_values_over_episodes], label=f"Action {action_idx}")

plt.xlabel('Episodes')
plt.ylabel('Q-Values')
plt.legend()
plt.show()

