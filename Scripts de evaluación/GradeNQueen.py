#coding=utf-8
import sys
import numpy
import subprocess

"""
# N-QUEEN
#
# Instructions:
# Write a program to solve the N-Queen problem using backtracking.
# The chess board is represented by a two-dimensional array
# with '1' in cell [i][j] if there is a queen in it, and '0', otherwise.
#
# Modify only the sections marked with the TODO comment. 
# DON'T ADD ANY 'print' FUNCTION.
"""

def is_safe(board, row, col):
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] != 0 and (x != row or y != col):
                delta_x = abs(row - x)
                delta_y = abs(col - y)
                if delta_x == 0 or delta_y == 0 or delta_x == delta_y:
                    return False
    return True

def N_Queen(board, row, N):   
    if row >= N:
        return True
    
    for i in range(N):
        if is_safe(board, row, i):
            board[row][i] = 1
            if N_Queen(board, row + 1, N) == True:
                return True
            board[row][i] = 0
    return False

def init_board(n):
    board = []
    for i in range(n):
        board.append([])
        for j in range(n):
            board[i].append(0)
    return board

def print_board(board):
    b = ""
    for x in range(len(board)):
        row_string = ""
        for y in range(len(board[0])):
            row_string += " Q" if board[x][y] == 1 else " ."
        b += row_string + "\n"
    return b

def check_output(s, n):
    rows = s.split('\n')
    board = []
    queens = 0
    for r in rows:
        if r == "":
            continue
        row = []
        for c in r:
            if c == 'Q':
                row.append(1)
                queens += 1
            elif c== '.':
                row.append(0)
        board.append(row)
    if len(board) != n:
        return False
    if len(board[0]) != n:
        return False
    if queens != n:
        return False
                
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1 and not is_safe(board, i, j):
                return False
    return True
        
        
                   
def generate_program_input():
    n = numpy.random.randint(5,15)
    return [str(n)]

def evaluate(program_input, program_output):
    n = int(program_input[0])
    result = check_output(program_output, n)
    board = init_board(n)
    N_Queen(board, 0, n)
    expected = print_board(board)
    return result, expected


if __name__ == '__main__':
    assignment_file = sys.argv[1]
    program_input = generate_program_input()
    #subprocess.call(["gcc", assignment_file, "-I", ".", "-w", "-o", "/dev/shm/a.out"])
    sp = subprocess.Popen(["python", assignment_file] + program_input, stdout=subprocess.PIPE)
    (program_output, program_error) = sp.communicate()
    result, expected_output = evaluate(program_input, program_output)
    if result:
        print("Correct result with the following values:")
    else:
        print("The program failed with the following values:")
    print("Program input:   " + str(program_input))
    print("Expected value:\n" + str(expected_output))
    print("Program output:\n" + program_output      )
