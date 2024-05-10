import numpy as np

# Construct all states
num_states = 2 ** 10
all_states = list(range(num_states))
best_paths = [([state], 0) for state in all_states]


for step in range(13):
    best_epaths = []

    for to_state in all_states:
        best_tload = -float('inf')
        best_epath = None

        for from_state in all_states:

            # Evaluate state transition
            add_load = np.random.randint(40)
            tload = best_paths[from_state][1] + add_load

            # Update best tload and extended path to get to to_state
            if tload >= best_tload:
                best_tload = tload
                best_epath = best_paths[from_state][0] + [to_state]

        # Record best state to come from as well as best total add_load
        best_epaths.append((best_epath, best_tload))

    for to_state in all_states:
        best_paths[to_state] = best_epaths[to_state]


print('hi')
