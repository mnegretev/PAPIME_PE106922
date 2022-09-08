#coding=utf-8
import sys
import numpy
import subprocess

"""
# CHANGE MAKING
#
# Instructions:
# Write a program to solve the change making problem using a greedy algorithm. 
#
# Modify only the functions marked with the TODO comment. 
# DON'T ADD ANY 'print' FUNCTION.
#
"""

def greedy_change_making(W, denominations):
    solution = []
    while W > 0:
        n = len(denominations) -1
        while denominations[n] > W:
            n -= 1
        solution.append(denominations[n])
        W -= denominations[n]
    return solution

def output_to_array(prog_output):
    A = []
    prog_output = prog_output.replace('[','').replace(']','').replace(',',' ').split()
    for s in prog_output:
        try:
            A.append(int(s))
        except:
            pass
    return A

def input_to_w_denominations(prog_input):
    w = int(prog_input[1])
    denominations = []
    for i in range(3, len(prog_input)):
        denominations.append(int(prog_input[i]))
    return w, denominations

def generate_program_input():
    W = numpy.random.randint(10,1000)
    C = ['1', '2', '5', '10', '20', '50', '100', '200', '500', '1000']
    input_str = ['-w', str(W), '-c'] + C
    return input_str

def evaluate(program_input, program_output):
    w, denominations = input_to_w_denominations(program_input)
    expected         = greedy_change_making(w, denominations)
    program_output   = output_to_array(program_output)
    return program_output == expected, str(expected)


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
