#!/usr/bin/python3
"""N queens solution finder module. """
import sys


def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
        
    # Check upper diagonal on the right side
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, row, N):
    if row == N:
        # Print the solution
        for i in range(N):
            print(" ".join(str(board[i][j]) for j in range(N)))
        print()
        return
    
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens(board, row + 1, N)
            board[row][col] = 0

def main():
    # Check if the number of arguments is correct
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize an empty chessboard of size N x N
    board = [[0 for _ in range(N)] for _ in range(N)]
    
    # Call the recursive function to find and print all solutions
    solve_nqueens(board, 0, N)

if __name__ == "__main__":
    main()