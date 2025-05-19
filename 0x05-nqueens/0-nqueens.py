#!/usr/bin/python3
"""Solves the N-Queens problem using backtracking."""

import sys


def is_safe(row, col, queens):
    """Check if a queen can be placed at (row, col)."""
    for r, c in queens:
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True


def solve_nqueens(n, row=0, queens=[]):
    """Recursive backtracking solution to N-Queens."""
    if row == n:
        print(queens)
        return

    for col in range(n):
        if is_safe(row, col, queens):
            solve_nqueens(n, row + 1, queens + [[row, col]])


def validate_and_solve():
    """Validate arguments and start solving."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)


if __name__ == "__main__":
    validate_and_solve()
