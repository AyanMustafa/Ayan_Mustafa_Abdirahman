#Assignment one train RL agent to navigate to across the road with action right, left, right
import numpy as np
import random

# Define action indices
RIGHT = 0
LEFT = 1
FORWARD = 2
ACTIONS = ['RIGHT', 'LEFT', 'RIGHT', 'FORWARD']

# Map actions to integers
action_space = [RIGHT, LEFT, FORWARD]

# Q-table: state (0-4) x actions (3)
Q = np.zeros((5, 3))

# Hyperparameters
alpha = 0.1      # learning rate
gamma = 0.9      # discount factor
epsilon = 0.2    # exploration rate
episodes = 1000

# Correct sequence
correct_sequence = [RIGHT, LEFT, RIGHT, FORWARD]

def get_next_state(current_state, action):
    if current_state >= len(correct_sequence):
        return current_state  # already at goal

    if action == correct_sequence[current_state]:
        return current_state + 1
    else:
        return 0  # reset if wrong

def get_reward(state, next_state):
    if next_state == 4:
        return 10  # reward for finishing sequence
    elif next_state > state:
        return 1   # small reward for correct step
    else:
        return -2  # penalty for mistake

# Training
for ep in range(episodes):
    state = 0
    while state < 4:
        if random.uniform(0, 1) < epsilon:
            action = random.choice(action_space)
        else:
            action = np.argmax(Q[state])

        next_state = get_next_state(state, action)
        reward = get_reward(state, next_state)

        Q[state][action] += alpha * (reward + gamma * np.max(Q[next_state]) - Q[state][action])

        state = next_state

# Testing the learned policy
print("Learned Q-table:")
print(Q)

# Testing the agent
print("\nAgent testing:")
state = 0
path = []
while state < 4:
    action = np.argmax(Q[state])
    path.append(['RIGHT', 'LEFT', 'FORWARD'][action])
    state = get_next_state(state, action)

print("Action path taken:", path)
