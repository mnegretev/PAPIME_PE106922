# -*- coding: utf-8 -*-
# DATA STRUCTURES AND ALGORITHMS I
# FI-UNAM-2022-2
# P R A C T I C E   1 1
# KNAPSACK PROBLEM WITH DYNAMIC PROGRAMMING
#
# Instructions:
# Write a program to solve the knapsack problem using dynamic programming
# given an array of item values 'V', item weights 'W' and capacity C. 
#
# Modify only the functions marked with the TODO comment. 
# DON'T ADD ANY 'print' FUNCTION.
#

import sys
import numpy

def knapsack(C, n, aux=None):
    global W,V
    if n == 0 or C == 0:
        return 0
    return knapsack(C, n-1, aux) if W[n-1] > C else max(V[n-1] + knapsack(C - W[n-1], n - 1, aux), knapsack(C, n-1, aux))

if __name__ == '__main__':
    global W,V
    if len(sys.argv) < 2:
        print("Usage:")
        print("Practice11.py -C capacity -W w1 w2 w3 w4 .... wn -V v1 v2 v3 v4 .... vn")
        print("Practice11.py -C capacity -N n")
        print("Second option generates 'n' random arrays W and V")
        exit()
    W = []
    V = []
    C = int(sys.argv[2])
    if sys.argv[3] == "-W": 
        i = 4
        while i < len(sys.argv) and sys.argv[i] != "-V":
            W.append(int(sys.argv[i]))
            i+=1
        i+= 1
        while i < len(sys.argv):
            V.append(int(sys.argv[i]))
            i+= 1
        if len(W) != len(V):
            print("W and V must have the same length")
            exit()
        n = len(W)
    else:
        n = int(sys.argv[4])
        W = numpy.random.randint(1,1000, n)
        V = numpy.random.randint(1,1000, n)
    print("C="+str(C))
    print("W="+str(W))
    print("V="+str(V))
    aux = [[None for j in range(C+1)] for i in range(n+1)]
    print(knapsack(C, len(W), aux))
    
