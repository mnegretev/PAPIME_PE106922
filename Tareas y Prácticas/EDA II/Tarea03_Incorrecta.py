# -*- coding: utf-8 -*-
# DATA STRUCTURES AND ALGORITHMS I
# FI-UNAM-2022-2
# A S S I G N M E N T   03
# CHANGE MAKING BY GREEDY ALGORITHMS
#
# Instructions:
# Write a program to solve the change making problem using a greedy algorithm. 
# Modify only the functions marked with the TODO comment. 
# DON'T ADD ANY 'print' FUNCTION.
#
# This work was supported by UNAM-DGAPA under grant PAPIME PE106922
#


import sys

def greedy_change_making(W, denominations):
    solution = []
    #
    # TODO:
    # Solve the change making problem using a greedy algorithm.
    # Use as greedy choice the largest denomination of coin which is not greater
    # than the remaining amount to be made.
    # Available denominations are stored in 'denominations' and the amount
    # to be made is stored in 'W'.
    # Assume you can pick as many coins as you need of every denomination.
    # Store the resulting coins in 'solution'
    # For example, if W = 99 and currencies = [1, 2, 5, 10, 20, 50, 100]
    # 'solution' should be [50, 20, 20, 5, 2, 2]
    #
    n = len(denominations) -1
    while W > 1:
        while denominations[n] > W:
            n -= 1
        solution.append(denominations[n])
        W -= denominations[n]
    return solution

if __name__ == '__main__':
    if len(sys.argv) < 5 or "-w" not in sys.argv or "-c" not in sys.argv:
        print("Usage:")
        print("Assignment22 -w amount -c currencies")
        print("Example:")
        print("Assignment22 -w 880 -c 1 2 5 10 20 50 100 200 500 1000")
        print("will print(the solution:")
        print("[500, 200, 100, 50, 20, 10]")
        exit()
    i = 0
    W = 0
    denominations= []
    while i < len(sys.argv):
        if sys.argv[i] == "-w":
            i += 1
            W = int(sys.argv[i])
        elif sys.argv[i] == "-c":
            while True:
                try:
                    i += 1
                    denominations.append(int(sys.argv[i]))
                except:
                    break
        else:
            i += 1
    print(greedy_change_making(W, denominations))
    
