#coding=utf-8
import sys
import numpy
import subprocess

"""
# ROD CUTTING
#
# Instructions:
# Write a program to solve the rod cutting problem using dynamic programming.
#
# Modify only the sections marked with the TODO comment. 
# DON'T ADD ANY 'print' FUNCTION.
#
"""

def rod_cutting(n, aux, p):
    q = -1
    if n == 0:
        return 0
    if aux[n] != None:
        return aux[n]
    for i in range(1, n+1):
        q = max(q, p[i] + rod_cutting(n-i, aux, p))
    aux[n] = q
    return q

def generate_program_input():
    n = numpy.random.randint(2,10)
    return [str(n)]

def evaluate(program_input, program_output):
    n = int(program_input[0])
    p   = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    aux = [None for i in range(len(p))]
    expected         = rod_cutting(n, aux, p)
    try:
        program_output = int(program_output)
    except:
        return False, str(expected)
    return program_output == expected, str(expected)


if __name__ == '__main__':
    assignment_file = sys.argv[1]
    program_input = generate_program_input_A15()
    #subprocess.call(["gcc", assignment_file, "-I", ".", "-w", "-o", "/dev/shm/a.out"])
    sp = subprocess.Popen(["python", assignment_file] + program_input, stdout=subprocess.PIPE)
    (program_output, program_error) = sp.communicate()
    result, expected_output = evaluate_A15(program_input, program_output)
    if result:
        print("Correct result with the following values:")
    else:
        print("The program failed with the following values:")
    print("Program input:   " + str(program_input))
    print("Expected value:\n" + str(expected_output))
    print("Program output:\n" + program_output      )
