import numpy as np

class QLearningAgent:
    def __init__(self, num_actions, learning_rate=0.1, discount_factor=0.9):
        self.num_actions = num_actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.q_values = {}

    def choose_action(self, state):
        if state not in self.q_values:
            self.q_values[state] = np.zeros(self.num_actions)
        return np.argmax(self.q_values[state])

    def learn_from_dataset(self, dataset):
        for state, action, reward, next_state, done in dataset:
            if state not in self.q_values:
                self.q_values[state] = np.zeros(self.num_actions)
            if next_state not in self.q_values:
                self.q_values[next_state] = np.zeros(self.num_actions)

            best_next_action = np.argmax(self.q_values[next_state])
            td_target = reward + self.discount_factor * self.q_values[next_state][best_next_action]
            td_error = td_target - self.q_values[state][action]
            self.q_values[state][action] += self.learning_rate * td_error

    def get_q_values(self):
        return self.q_values
