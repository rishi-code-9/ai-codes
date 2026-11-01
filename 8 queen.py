
# 8 Queens Problem using Backtracking

N = 8

# Create an empty chessboard
board = [[0 for _ in range(N)] for _ in range(N)]


# Check whether a queen can be placed safely
def is_safe(row, col):

    # Check same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


# Backtracking function
def solve(row):

    # All queens are placed
    if row == N:
        return True

    # Try each column
    for col in range(N):

        if is_safe(row, col):

            # Place queen
            board[row][col] = 1

            # Move to next row
            if solve(row + 1):
                return True

            # Backtrack
            board[row][col] = 0

    return False


# Execute the program
if solve(0):

    print("Solution Found!\n")

    for row in board:
        for cell in row:
            if cell == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

else:
    print("No Solution Exists")
