import random

class SpookyMansion:
    def __init__(self, size=5, ghost_probability=0.2, diamond_probability=0.1, inspect_impact=0.5, punishment_severity=1.0):
        self.size = size
        self.ghost_probability = ghost_probability
        self.diamond_probability = diamond_probability
        self.inspect_impact = inspect_impact
        self.punishment_severity = punishment_severity

        self.mansion = [[self._generate_room() for _ in range(size)] for _ in range(size)]

        self.explorer_position = (0, 0)

    def get_state_key(self, state):
        return f"state_{state[0]}_{state[1]}"

    def _generate_room(self):
        if random.random() < self.ghost_probability:
            return "ghost"
        elif random.random() < self.diamond_probability:
            return "diamond"
        else:
            return "empty"

    def step(self, action):
        if action == "left" and self.explorer_position[1] > 0:
            self.explorer_position = (self.explorer_position[0], self.explorer_position[1] - 1)
        elif action == "right" and self.explorer_position[1] < self.size - 1:
            self.explorer_position = (self.explorer_position[0], self.explorer_position[1] + 1)
        elif action == "up" and self.explorer_position[0] > 0:
            self.explorer_position = (self.explorer_position[0] - 1, self.explorer_position[1])
        elif action == "down" and self.explorer_position[0] < self.size - 1:
            self.explorer_position = (self.explorer_position[0] + 1, self.explorer_position[1])

        current_room = self.mansion[self.explorer_position[0]][self.explorer_position[1]]

        if current_room == "ghost":
            punishment = int(self.punishment_severity * self._gather_diamonds())
            return self.explorer_position, -punishment, True
        elif current_room == "diamond":
            return self.explorer_position, 1, True
        else:
            return self.explorer_position, 0, False

    def inspect(self):
        current_room = self.mansion[self.explorer_position[0]][self.explorer_position[1]]
        if current_room == "ghost":
            return -self.inspect_impact
        elif current_room == "diamond":
            return self.inspect_impact
        else:
            return 0

    def _gather_diamonds(self):
        return sum(row.count("diamond") for row in self.mansion)

    def reset(self):
        self.explorer_position = (0, 0)
        self.mansion = [[self._generate_room() for _ in range(self.size)] for _ in range(self.size)]
        return self.explorer_position

    def generate_dataset(self, num_episodes, max_steps=100):
        dataset = []

        for _ in range(num_episodes):
            state = self.reset()
            done = False
            steps = 0

            while not done and steps < max_steps:
                action = random.choice(["left", "right", "up", "down", "inspect"])
                next_state, reward, done = self.step(action)
                dataset.append((state, action, reward, next_state, done))
                state = next_state
                steps += 1

        return dataset

    def _take_action(self, action):
        if action == "inspect":
            reward = self.inspect()
        else:
            reward = self.step(action)
        return self.explorer_position, reward
