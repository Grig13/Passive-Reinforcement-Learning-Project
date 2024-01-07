import numpy as np

class QLearningAgent:
    def __init__(self, num_actions, exploration_prob=0.1, learning_rate=0.1):
        self.num_actions = num_actions
        self.q_values = {}
        self.exploration_prob = exploration_prob
        self.learning_rate = learning_rate

    def get_q_values(self, state):
        return self.q_values.get(state, [0] * self.num_actions)

    def choose_action(self, state):
        if np.random.rand() < self.exploration_prob:
            return np.random.choice(self.num_actions)
        else:
            q_values = self.get_q_values(state)
            return np.argmax(q_values)

    def learn_from_dataset(self, dataset):
        for state, action, reward, next_state, done in dataset:
            current_q_values = self.get_q_values(state)
            next_q_values = self.get_q_values(next_state)
            target = reward + (0 if done else np.max(next_q_values))
            current_q_values[action] = (1 - self.learning_rate) * current_q_values[action] + self.learning_rate * target

