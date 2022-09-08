#coding=utf-8
import sys
import numpy
import subprocess

"""
# MATRIX CHAIN MULTIPLICATION
#
# Instructions:
# Write a program to solve the Matrix Chain Multiplication problem
# using dynamic programming. The chain of N matrices is given by an
# array of N+1 integers, e.g., an array [3 1 4 1 5] represents four
# matrices with orders 3x1, 1x4, 4x1 and 1x5.
# The program must calculate the best multiplication order to perform
# the minimun number of scalar multiplications.
#
# Modify only the sections marked with the TODO comment. 
# DON'T ADD ANY 'print' FUNCTION.
#
"""

def chain_order(A, i, j, aux_m, aux_s):
    #
    # TODO:
    # Write a recursive algorithm, using dynamic programming, to find the
    # best order to multiply matrices represented by array A, from index i to j.
    # Use aux_m and aux_s as auxiliar variables to implement memoization.
    # Return the minimum number of scalar multiplications 'q' and the
    # corresponding string 's' indicating the optimal order. 
    #
    if abs(j-i) == 1:
        return 0, "A"+str(j)

    if aux_m[i][j] != None:
        return aux_m[i][j], aux_s[i][j]
    
    q = sys.maxsize
    for k in range(i+1,j):
        m1, s1 = chain_order(A, i, k, aux_m, aux_s)
        m2, s2 = chain_order(A, k, j, aux_m, aux_s)
        m  = m1 + m2 +  A[i]*A[k]*A[j]
        if m < q:
            q = m
            s = "(" + s1 + s2 + ")"
    aux_m[i][j] = q
    aux_s[i][j] = s
    return q, s

def generate_program_input():
    n = numpy.random.randint(1,100, numpy.random.randint(5,20))
    return [str(i) for i in n]

def evaluate(program_input, program_output):
    A = [int(s) for s in program_input]
    aux_m = [[None for i in range(len(A))] for i in range(len(A))]
    aux_s = [[None for i in range(len(A))] for i in range(len(A))]
    m,s = chain_order(A,0,len(A)-1, aux_m, aux_s)
    expected_nice = "Minimum number of scalar multiplications:\n" + str(m) + "Optimal order of multiplication:\n" + s
    expected      = "Minimum number of scalar multiplications:"   + str(m) + "Optimal order of multiplication:" + s
    expected      = expected.replace('\r', '').replace('\n', '').replace(' ', '')
    program_output = program_output.replace('\r', '').replace('\n', '').replace(' ', '')
    return program_output == expected, str(expected_nice)


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
