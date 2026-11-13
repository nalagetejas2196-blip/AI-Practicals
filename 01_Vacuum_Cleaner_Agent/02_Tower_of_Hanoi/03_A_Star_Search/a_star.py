
import heapq

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def heuristic(state):
    return sum(1 for i in range(9) if state[i] != 0 and state[i] != goal[i])

def get_neighbors(state):
    neighbors = []
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
            neighbors.append((tuple(new_state), move))

    return neighbors

def a_star():
    pq = [(heuristic(start), 0, start, [])]
    best_cost = {start: 0}

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if g != best_cost[state]:
            continue

        if state == goal:
            print("Solution found!")
            print("Moves:", " -> ".join(path))
            print("Total moves:", len(path))
            return

        for neighbor, move in get_neighbors(state):
            new_g = g + 1

            if new_g < best_cost.get(neighbor, float("inf")):
                best_cost[neighbor] = new_g
                new_f = new_g + heuristic(neighbor)
                heapq.heappush(pq, (new_f, new_g, neighbor, path + [move]))

    print("No solution found")

a_star()
