
N = 8
board = [-1] * N

def safe(row, col):
    for previous_col in range(col):
        previous_row = board[previous_col]

        if previous_row == row:
            return False

        if abs(previous_row - row) == abs(previous_col - col):
            return False

    return True

def solve(col):
    if col == N:
        return True

    for row in range(N):
        if safe(row, col):
            board[col] = row

            if solve(col + 1):
                return True

            board[col] = -1

    return False

if solve(0):
    print("Solution for 8 Queens:")
    for row in range(N):
        for col in range(N):
            if board[col] == row:
                print("Q", end=" ")
            else:
                print("x", end=" ")
        print()
else:
    print("No solution exists")
