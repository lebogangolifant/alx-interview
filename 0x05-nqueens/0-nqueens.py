#!/usr/bin/python3
"""
N queens puzzle
"""

import sys


def is_safe(board, row, col, size):
    """
    Check if it's safe to place a queen at a given position.
    """
    for c in range(col):
        if board[c] == row or board[c] - c == row - col or \
                     board[c] + c == row + col:
            return False
    return True


def solve_n_queens_util(board, col, size):
    """
    Recursive utility function to solve the N-Queens problem.
    """
    if col == size:
        print([[i, board[i]] for i in range(size)])
        return

    for r in range(size):
        if is_safe(board, r, col, size):
            board[col] = r
            solve_n_queens_util(board[:], col + 1, size)


def solve_n_queens(size):
    """
    Solve the N-Queens problem and print solutions.
    """
    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * size
    solve_n_queens_util(board, 0, size)


if __name__ == "__main__":
    # Check for the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        # Convert the argument to an integer
        chessboard_size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_n_queens(chessboard_size)
