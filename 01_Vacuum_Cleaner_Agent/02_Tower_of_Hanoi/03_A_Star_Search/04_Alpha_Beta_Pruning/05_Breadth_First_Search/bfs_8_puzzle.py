
from collections import deque

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def bfs():
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    move_used = {}

    while queue:
        state = queue.popleft()

        if state == goal:
            path = []
            current = goal

            while parent[current] is not None:
                path.append(move_used[current])
                current = parent[current]

            path.reverse()

            print("Solution found!")
            print("Moves:", " -> ".join(path))
            print("Total moves:", len(path))
            return

        zero = state.index(0)
        row, col = divmod(zero, 3)

        moves = [
            (-1, 0, "Up"),
            (1, 0, "Down"),
            (0, -1, "Left"),
            (0, 1, "Right")
        ]

        for dr, dc, move in moves:
            nr, nc = row + dr, col + dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                new_zero = nr * 3 + nc
                new_state = list(state)
                new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]
                new_state = tuple(new_state)

                if new_state not in visited:
                    visited.add(new_state)
                    parent[new_state] = state
                    move_used[new_state] = move
                    queue.append(new_state)

    print("No solution found")

bfs()
