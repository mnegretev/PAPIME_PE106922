#coding=utf-8
import sys
import numpy
import os
import subprocess
import random
import string
from datetime import datetime

"""
/*
 * CAESAR CIPHER
 *
 * Instructions:
 * Write a program to implement the Caesar Cipher
 * The program must receive as command line arguments, the number
 * of positions to shift, and the string to be ciphered.
 * Only the characters in a-z and A-Z must be shifted and
 * all the other chars must remain the same.
 
 * ONLY MODIFY THE FUNCTION caesar_cipher
 * USE OF POINTERS IS MANDATORY
 * THE ARRAY NOTATION [] IS NOT ALLOWED. USE POINTERS INSTEAD.
 * DON'T MODIFY THE MAIN FUNCTION.
 * DON'T ADD ANY 'printf' FUNCTION.
 */
"""

test_strings = open("TestStrings.txt", 'r').readlines()
test_strings = [x.strip() for x in test_strings]

def generate_program_input():
    return [str(numpy.random.randint(-1000,1000)), numpy.random.choice(test_strings)]

def evaluate(program_input, program_output):
    program_output = program_output.strip()
    n = int(program_input[0]) #Number of alphabet positions to be shifted
    s = program_input[1].strip()  #String to be shifted
    #The following lines perform the shift and calculate the expected output
    n = n%26
    a1 = list(s)
    for i in range(len(a1)):
        c = ord(a1[i])
        if c >= 0x41 and c <= 0x5A:
            c += n
            if c > 0x5A:
                c -= 26
            if c < 0x41:
                c += 26
        if c >= 0x61 and c <= 0x7A:
            c += n
            if c > 0x7A:
                c -= 26
            if c < 0x61:
                c += 26
        a1[i] = chr(c)
    expected = "".join(a1)
    return program_output == expected, expected


if __name__ == '__main__':
    assignment_file = sys.argv[1]
    program_input = generate_program_input()
    subprocess.call(["gcc", assignment_file, "-w", "-o", "/dev/shm/a.out"])
    sp = subprocess.Popen(['/dev/shm/a.out'] + program_input, stdout=subprocess.PIPE)
    (program_output, program_error) = sp.communicate()
    result, expected_output = evaluate(program_input, program_output)
    if result:
        print("Correct result with the following values:")
    else:
        print("The program failed with the following values:")
    print("Program input:   " + str(program_input))
    print("Expected value:\n" + str(expected_output))
    print("Program output:\n" + program_output      )
