# -*- coding: utf-8 -*-
# DATA STRUCTURES AND ALGORITHMS I
# FI-UNAM-2022-2
# A S S I G N M E N T   2 2
# MERGE SORT
#
# Instructions:
# Write a program to sort, in ascending order, an array of integers using the
# Merge Sort algorithm.
# Integers to be sorted are passed as command line arguments. 
#
# Modify only the functions marked with the TODO comment. 
# DON'T ADD ANY 'print' FUNCTION.
#

import sys

def merge_two_sorted_arrays(A,B):
    #
    # TODO:
    # Implement an algorithm to merge two sorted arrays A and B.
    # The resulting array C should be also a sorted array whose length
    # will be the length of A plus the length of B.
    # Return the resulting sorted array C.
    #
    

def merge_sort(A):
    #
    # TODO:
    # Implement the Merge Sort algorithm.
    # Integers to be sorted are stored in the list 'A'.
    # Return a list with the sorted integers.
    #
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
    print(merge_sort(A))
