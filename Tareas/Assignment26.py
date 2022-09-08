# -*- coding: utf-8 -*-
# DATA STRUCTURES AND ALGORITHMS I
# FI-UNAM-2022-2
# A S S I G N M E N T   2 6
# N-QUEEN PROBLEM
#
# Instructions:
# Write a program to solve the N-Queen problem using backtracking.
# The chess board is represented by a two-dimensional array
# with '1' in cell [i][j] if there is a queen in it, and '0', otherwise.
#
# Modify only the sections marked with the TODO comment. 
# DON'T ADD ANY 'print' FUNCTION.
#

import sys

def is_bad(board, row, col):
    #
    # TODO:
    #
    # Write a function to determine if it is a bad idea to put a queen
    # in the coordinates [row, col]
    # given the current board configuration.
    # Hint: You can check the difference in X and Y between a queen
    # and the position of interest. If delta_X== 0, delta_Y==0 or delta_x=delta_y
    # then it is not a safe position.
    # Return False if it is safe to put a queen in [row, col], i.e, if
    # queen in [row, col] does not attack any other queen in board.
    # Return True otherwise
    #
    return False

def N_Queen(board, row, N):
    #
    # TODO:
    #
    # Write a recursive function to check the candidate solutions in a row.
    # Base case:
    # - If row >= N, then
    #     - return True (we are done)
    #
    # Recursive case:
    # - For all columns in row:
    #     - If it is not bad to place a Queen in row,column then
    #         - Place Quenn in row, col
    #         - If placing Queen in row,col leads to a solution (check this recursively)
    #             - return True (it lead to a correct solution)
    #         - If it does not (the else of the previous if), then remove the placed Queen (this is the bakctrack)
    # - If all digits have been tried and nothing worked, return false (this triggers backtracking)
    #

    return False

def init_board(n):
    board = []
    for i in range(n):
        board.append([])
        for j in range(n):
            board[i].append(0)
    return board

def print_board(board):
    for x in range(len(board)):
        row_string = ""
        for y in range(len(board[0])):
            row_string += " Q" if board[x][y] == 1 else " ."
        print(row_string)

def main(n):
    board = init_board(n)
    N_Queen(board, 0, n)
    print_board(board)
            

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Too few parameteres. At least one integer required.")
        exit()
    n = int(sys.argv[1])
    if n < 4:
        print("N must be greater or equal than 4.")
        exit()
    main(n)
