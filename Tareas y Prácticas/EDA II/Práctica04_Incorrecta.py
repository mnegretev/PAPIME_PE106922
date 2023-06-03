# -*- coding: utf-8 -*-
# DATA STRUCTURES AND ALGORITHMS I
# FACULTAD DE INGENIERÍA, UNAM, 2021-1
# P R A C T I C E   04
# SUDOKU SOLVER
#
# Instructions:
# Write a program to solve a Sudoku puzzle using backtracking.
# Sudoku is represented by a bidimensional array of integers
# where 0 represents an empty cell. 
#
# Modify only the sections marked with the TODO comment. 
# DON'T ADD ANY 'print' FUNCTION.
#
# This work was supported by UNAM-DGAPA under grant PAPIME PE106922
#


import sys

def is_bad(sudoku, row, col, x):
    #
    # TODO:
    #
    # Check if it is a bad idea to place digit x in the position [row, col]
    # given the current sudoku configuration.
    # According to sudoku rules, you need to check the whole row 'row',
    # the whole column 'col' and the corresponding 3x3 box.
    # Return true if it is a bad idea, i.e., x repeats somewhere
    # in the row, column or 3x3 box.
    # Return false otherwise
    #
    return None

def solve_sudoku(sudoku):
    #
    # TODO:
    #
    # Write a recursive function to check the candidate solutions in a row:
    #
    # - Find an empty cell (just call the corresponding function and store the [row,col] coordinates)
    #   cell = find_empty_cell(sudoku)
    # - If there is no empty cell, return True (we are done)
    # - For all digits x in [1-9] do:
    #     - If it is not bad to add digit x, then
    #           - Place digit x in [row,col] (the coordinates of the found empty cell)
    #           - If placing digit x in row,col leads to a solution (check this recursively)
    #                 - return True
    #           - If it does not (the else of the previous if), then remove the placed digit (this is the bakctrack)
    # - If all digits have been tried and nothing worked, return false (this trigger backtracking)
    #
    return False

def find_empy_cell(sudoku):
    #
    # This function returns the coordinates of the first empty cell.
    # Coordinates are returned as a tuple [i,j]
    # If no empty cell is found, it returns None
    #
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return [i,j]
    return None

def parse_from_args(args):
    sudoku = [[0 for i in range(9)] for j in range(9)]
    for i in range(1, len(args)):
        if args[i] == '--grading':
            continue
        if len(args[i]) != 9:
            print("Invalid format in argument " + str(i+1))
            return None
        for j in range(9):
            sudoku[i-1][j] = int(args[i][j])
    return sudoku
            

def print_sudoku(sudoku):
    for x in range(len(sudoku)):
        row_string = ""
        for y in range(len(sudoku[0])):
            if y % 3 == 0 and y > 0:
                row_string += " |"
            row_string += " " + str(sudoku[x][y]) if sudoku[x][y] != 0 else " ."
        if x%3 == 0 and x > 0:
            print(" - - - - - - - - - - -")
        print(row_string)

def print_simple(sudoku):
    s = ''
    for x in range(len(sudoku)):
        for y in range(len(sudoku[0])):
            s += str(sudoku[x][y])
    print(s)

if __name__ == '__main__':
    if len(sys.argv) < 10:
        print("Too few parameteres.")
        exit()
    sudoku = parse_from_args(sys.argv)
    if '--grading' in sys.argv:
        if not solve_sudoku(sudoku):
            print("Cannot solve sudoku")
        print_simple(sudoku)
        exit()
        
    print("Unsolved Sudoku:")
    print_sudoku(sudoku)
    if not solve_sudoku(sudoku):
        print("Cannot solve sudoku")
    print("")
    print("Solved Sudoku:")
    print_sudoku(sudoku)
