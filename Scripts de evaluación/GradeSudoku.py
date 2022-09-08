#coding=utf-8
import sys
import numpy
import subprocess

"""
# SUDOKU
#
# Instructions:
# Write a program to solve a Sudoku puzzle using backtracking.
# Sudoku is represented by a bidimensional array of integers
# where 0 represents an empty cell. 
#
# Modify only the sections marked with the TODO comment. 
# DON'T ADD ANY 'print' FUNCTION.
"""        

test_strings = open("SudokuTests.txt", 'r').readlines()
test_strings = [x.strip().split() for x in test_strings]

def generate_program_input():
    n = numpy.random.randint(len(test_strings))
    return test_strings[n]

def evaluate(program_input, program_output):
    sp = subprocess.Popen(['python', '../Assignments/Practice12solved.py'] + program_input, stdout=subprocess.PIPE)
    (expected_nice, program_error) = sp.communicate()
    expected_nice = expected_nice.decode('utf-8')
    expected = expected_nice.replace(' ', '').replace('\n','')
    program_output = program_output.replace(' ', '').replace('\n','')
    return expected == program_output, expected_nice


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
