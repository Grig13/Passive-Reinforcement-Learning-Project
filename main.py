from environment import SpookyMansion
from agent import QLearningAgent

# Set up the environment
env = SpookyMansion(size=5, ghost_probability=0.2, diamond_probability=0.1, inspect_impact=0.1, punishment_severity=1.0)

# Set up the Q-learning agent
num_actions = len(["left", "right", "up", "down", "inspect"])
agent = QLearningAgent(num_actions)

# Training loop with a dataset
num_episodes = 1
dataset = env.generate_dataset(num_episodes)

for episode in range(num_episodes):
    state = env.reset()
    total_reward = 0
    done = False

    while not done:
        action = agent.choose_action(state)
        next_state, reward, done = env.step(action)
        total_reward += reward

    agent.learn_from_dataset(dataset)

# Print learned Q-values
print("Learned Q-values:")
print(agent.get_q_values())
