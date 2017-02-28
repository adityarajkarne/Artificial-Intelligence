#!/usr/bin/env python3


import sys

# Count # of pieces in given row
def count_on_row(board, row):
    return sum( board[row] )

# Count # of pieces in given column
def count_on_col(board, col):
    return sum( [ row[col] for row in board ] )


def count_on_diag(board,row,col):
    return sum([ board[i][j] for i in range(len(board)) for j in range(len(board))  if row+col==i+j or row-col==i-j])


# Count total # of pieces on board
def count_pieces(board):
    return sum([ sum(row) for row in board ] )

# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    return "\n".join([ " ".join([ "Q" if col else "_" for col in row ]) for row in board])


# Add a piece to the board at the given position, and return a new board (doesn't change original)
def add_piece(board, row, col):
    return board[0:row] + [board[row][0:col] + [1,] + board[row][col+1:]] + board[row+1:]

# Get list of successors of given board state

def successors(board):
    return [ add_piece(board, r, c) for r in [r for r in range(0,N) if count_on_row(board, r)==0] for c in [c for c in range(0,N) if count_on_col(board, c)==0] if count_on_diag(board,r,c)==0]


def is_valid(board):
        return all( [ count_on_row(board, r) <= 1 for r in range(0, N) ] ) and \
        all( [ count_on_col(board, c) <= 1 for c in range(0, N) ] ) and \
        all( [ count_on_diag(board, r, c) <= 1 for r in range(0, N) for c in range(0,N) if board[r][c]==1] )


# check if board is a goal state
def is_goal(board):
    return count_pieces(board) == N and \
        all( [ count_on_row(board, r) <= 1 for r in range(0, N) ] ) and \
        all( [ count_on_col(board, c) <= 1 for c in range(0, N) ] ) and \
        all( [ count_on_diag(board, r, c) <= 1 for r in range(0, N) for c in range(0,N) if board[r][c]==1] )

# Solve n-queens!
def solve(initial_board):
    fringe = [initial_board]
    while len(fringe) > 0:
        child=fringe.pop()
        if is_valid(child):
            for s in successors(child):
                if is_goal(s):
                    return(s)
                fringe.append(s)
    return False


# This is N, the size of the board. It is passed through command line arguments.
N = int(sys.argv[1])
Q = int(sys.argv[2])
R = int(sys.argv[3])


# The board is stored as a list-of-lists. Each inner list is a row of the board.
# A zero in a given square indicates no piece, and a 1 indicates a piece.
initial_board = [[0]*N]*N
print ("Starting from initial board:\n" + printable_board(initial_board) + "\n\nLooking for solution...\n")
solution = update_pieces(solve(initial_board), R)
print (printable_board(solution) if solution else "Sorry, no solution found. :(")


