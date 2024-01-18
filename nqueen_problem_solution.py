def is_valid(board, row, col, N):
    # placing a queen at board[row][col] is valid

    # Checkqueens in the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check for queens in the left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i] == j:
            return False

    # Check for queens in the right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i] == j:
            return False

    return True

def solve_n_queens_util(N, row, board, solutions):
    # All queens are placed successfully
    if row == N:
        solutions.append(board[:])  # Append a copy of the current board
        return

    for col in range(N):
        # Check queen at this position is valid
        if is_valid(board, row, col, N):
            # Place the queen
            board[row] = col

            # placing the next queen
            solve_n_queens_util(N, row + 1, board, solutions)

            # remove the queen and try other positions
            board[row] = -1

def solve_n_queens(N):
    # Initialize the chessboard with all positions set to -1
    board = [-1] * N

    solutions = []  # List to store all valid placements

    # Start with the first row (row 0)
    solve_n_queens_util(N, 0, board, solutions)

    return solutions

# Example usage
N = 4
result = solve_n_queens(N)
print("a list of valid queen placements for chessboard for ", N, "queens:", result)