#coding=utf-8
import sys
import numpy
import subprocess

"""
# INSERTION SORT
#
# Instructions:
# Write a program to sort, in ascending order, an array of integers using the
# Insertion Sort algorithm.
# Integers to be sorted are passed as command line arguments. 
#
# Modify only the functions marked with the TODO comment. 
# DON'T ADD ANY 'print' FUNCTION.
#
"""

def output_to_array(prog_output):
    A = []
    prog_output = prog_output.replace('[','').replace(']','').replace(',',' ').split()
    for s in prog_output:
        try:
            A.append(int(s))
        except:
            pass
    return A

def input_to_array(prog_input):
    A = [int(s) for s in prog_input]
    return A

def generate_program_input():
    A = numpy.random.randint(1,1000,numpy.random.randint(10,30))
    B = []
    for a in A:
        B.append(str(a))
    return B

def evaluate(program_input, program_output):
    expected       = input_to_array(program_input)  
    program_output = output_to_array(program_output)
    expected.sort()
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
