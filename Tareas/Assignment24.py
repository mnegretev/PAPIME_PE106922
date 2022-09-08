# -*- coding: utf-8 -*-
# DATA STRUCTURES AND ALGORITHMS I
# FI-UNAM-2022-2
# A S S I G N M E N T   2 4
# ROD CUTTING PROBLEM
#
# Instructions:
# Write a program to solve the rod cutting problem using dynamic programming.
#
# Modify only the sections marked with the TODO comment. 
# DON'T ADD ANY 'print' FUNCTION.
#

import sys

L   = [0, 1, 2, 3, 4,  5,  6,  7,  8,  9, 10]
p   = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

#
# TODO:
# Declare an auxiliar array 'aux' to store the calculated rod lengths
#

def rod_cutting(n):
    q = -1
    #
    # TODO:
    # Complete this function to calculate the maximum revenue 'q' for a
    # rod of length n.
    # Use the auxiliar array 'aux' to check if max revenue for 'n' has
    # been previously calculated (memoized algorithm).
    # Return max revenue 'q'.
    #
    return q

if __name__ == '__main__':
    if len(sys.argv) < 2 or int(sys.argv[1]) < 0 or int(sys.argv[1]) > 10:
        print("At least one integer 0 <= n <= 10 is required")
        exit()
    print(rod_cutting(int(sys.argv[1])))
