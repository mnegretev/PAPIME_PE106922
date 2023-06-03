# -*- coding: utf-8 -*-
# DATA STRUCTURES AND ALGORITHMS II
# FI-UNAM-2022-2
# A S S I G N M E N T   0 6
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
# This work was supported by UNAM-DGAPA under grant PAPIME PE106922
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
    #print("Minimum number of scalar multiplications:")
    #print(str(m))
    #print("Optimal order of multiplication:")
    print(s)
    
