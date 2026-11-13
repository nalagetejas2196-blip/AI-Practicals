
from collections import deque

def tower_of_hanoi_bfs(n):
    start = tuple([0] * n)
    goal = tuple([2] * n)

    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            print("Total moves:", len(path))
            for move in path:
                print(move)
            return

        pegs = [[], [], []]

        for disk, peg in enumerate(state):
            pegs[peg].append(disk)

        for source in range(3):
            if not pegs[source]:
                continue

            disk = pegs[source][-1]

            for destination in range(3):
                if source == destination:
                    continue

                if not pegs[destination] or disk < pegs[destination][-1]:
                    new_state = list(state)
                    new_state[disk] = destination
                    new_state = tuple(new_state)

                    if new_state not in visited:
                        visited.add(new_state)
                        move = f"Move disk {disk + 1} from peg {source + 1} to peg {destination + 1}"
                        queue.append((new_state, path + [move]))

n = int(input("Enter number of disks: "))
tower_of_hanoi_bfs(n)
