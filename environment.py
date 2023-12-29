import numpy as np


class SimpleEnvironment:
    def __init__(self, num_states, num_actions, transition_matrix, reward_matrix):
        self.num_states = num_states
        self.num_actions = num_actions
        self.transition_matrix = transition_matrix
        self.reward_matrix = reward_matrix
        self.current_state = np.random.randint(0, num_states)

    def reset(self):
        self.current_state = np.random.randint(0, self.num_states)

    def step(self, action):
        if action < 0 or action >= self.num_actions:
            raise ValueError("Invalid Action")

        transition_probs = self.transition_matrix[self.current_state, action, :]
        next_state = np.random.choice(np.arange(self.num_states), p=transition_probs)
        reward = self.reward_matrix[self.current_state, action, next_state]

        self.current_state = next_state

        return next_state, reward

    def get_state(self):
        return self.current_state
