#!/usr/bin/python3
"""
nqueens problem
"""
import sys


def backtrack(r, n, cols, pos, neg, board, solutions):
    """
    Backtracking function to find all solutions for N queens problem
    """
    if r == n:
        # Collecting solution
        res = []
        for l in range(len(board)):
            for k in range(len(board[l])):
                if board[l][k] == 1:
                    res.append([l, k])
        solutions.append(res)
        return

    for c in range(n):
        if c in cols or (r + c) in pos or (r - c) in neg:
            continue

        cols.add(c)
        pos.add(r + c)
        neg.add(r - c)
        board[r][c] = 1

        backtrack(r + 1, n, cols, pos, neg, board, solutions)

        cols.remove(c)
        pos.remove(r + c)
        neg.remove(r - c)
        board[r][c] = 0


def nqueens(n):
    """
    Solution to nqueens problem
    Args:
        n (int): number of queens. Must be >= 4
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for _ in range(n)]
    solutions = []

    backtrack(0, n, cols, pos_diag, neg_diag, board, solutions)

    solutions.sort(key=lambda x: x[0][1])

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
