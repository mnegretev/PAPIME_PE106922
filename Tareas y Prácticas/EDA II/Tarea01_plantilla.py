# -*- coding: utf-8 -*-
# ESTRUCTURAS DE DATOS Y ALGORITMOS I
# FACULTAD DE INGENIERIA, UNAM, 2021-2
# A S S I G N M E N T   0 1
# Instructions:
# Write a program to sort, in ascending order, an array of integers using the
# Bubble Sort algorithm.
# Integers to be sorted are passed as command line arguments. 
#
# Modify only the functions marked with the TODO comment. 
# DON'T ADD ANY 'print' FUNCTION.
#
# This work was supported by UNAM-DGAPA under grant PAPIME PE106922
#


import sys

def bubble_sort(A):
    #
    # TODO:
    # Implement the Bubble Sort algorithm.
    # Integers to be sorted are stored in the list 'A'.
    # Return a list with the sorted integers.
    #
    j = len(A)
    while j>0:
        for i in range(1,j):
            if A[i] < A[i-1]:
                A[i], A[i-1] = A[i-1], A[i]
        j -= 1

    return A

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("At least one integer is required")
        exit()
    A = []
    for s in sys.argv:
        try:
            A.append(int(s))
        except:
            pass
    print(bubble_sort(A))
