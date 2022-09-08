# -*- coding: utf-8 -*-
# DATA STRUCTURES AND ALGORITHMS I
# FI-UNAM-2022-2
# A S S I G N M E N T   2 5
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

import sys

def chain_order(A, i, j, aux_m, aux_s):
    #
    # TODO:
    # Write a recursive algorithm, using dynamic programming, to find the
    # best order to multiply matrices represented by array A, from index i to j.
    # Use aux_m and aux_s as auxiliar variables to implement memoization.
    # Return the minimum number of scalar multiplications 'q' and the
    # corresponding string 's' indicating the optimal order. 
    #
    return q, s

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("At least two positive integers are required")
        exit()
    A = []
    for s in sys.argv:
        try:
            A.append(int(s))
        except:
            pass
    steps = 0
    aux_m = [[None for i in range(len(A))] for i in range(len(A))]
    aux_s = [[None for i in range(len(A))] for i in range(len(A))]
    m,s = chain_order(A,0,len(A)-1, aux_m, aux_s)
    print("Minimum number of scalar multiplications:")
    print(m)
    print("Optimal order of multiplication:")
    print(s)
    
