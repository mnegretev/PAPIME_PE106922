# -*- coding: utf-8 -*-
# DATA STRUCTURES AND ALGORITHMS I
# FI-UNAM-2022-2
# P R A C T I C E   01
# QUICK SORT
#
# Instructions:
# Write a program to sort, in ascending order, an array of integers using the
# Quick Sort algorithm.
# Integers to be sorted are passed as command line arguments. 
#
# Modify only the functions marked with the TODO comment. 
# DON'T ADD ANY 'print' FUNCTION.
#
# This work was supported by UNAM-DGAPA under grant PAPIME PE106922
#


import sys

def partition(i,j, A):
    #
    # TODO:
    # Write the code to do the partition process. You can do the following steps:
    #
    #    Set as pivot the element at the 'i' index
    #    Set 'i' as pivot index
    #    WHILE i < j
    #        WHILE i < size of A and A[i] is less or equal than pivot: Increment i
    #        WHILE A[j] is strictly greater than pivot: decrement j
    #        IF i < j THEN swap A[i] and A[j]
    #    Swap A[pivot index] and A[j]
    #    RETURN j
    #

def quick_sort(i,j,A):
    #
    # TODO:
    # Implement QuickSort. You can do the following steps:
    #
    #    IF i < j:
    #        Find the pivot index 'p' by calling the 'partition' function with i,j,A
    #        Order by quick sort the array from i to p-1
    #        Order by quick sort the array from p+1 to j
    # 

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
    quick_sort(0, len(A)-1, A)
    print(A)
