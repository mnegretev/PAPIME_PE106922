#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# DATA STRUCTURES AND ALGORITHMS I
# FI-UNAM-2022-2
# A S S I G N M E N T   02
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
# This work was supported by UNAM-DGAPA under grant PAPIME PE106922
#


import sys

def insertion_sort(A):
    #
    # TODO:
    # Implement the Insertion Sort algorithm.
    # Integers to be sorted are stored in the list 'A'.
    # Return a list with the sorted integers.
    #
    for i in range(1, len(A)):
        j = i
        while A[j] < A[j-1] and j > 0:
            A[j], A[j-1] = A[j-1], A[j]
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
    print(insertion_sort(A))
