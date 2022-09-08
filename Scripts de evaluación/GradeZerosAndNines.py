#coding=utf-8
import sys
import numpy
import math
import subprocess
from collections import deque

"""
/*
 * ZEROS AND NINES
 * 
 * Instructions:
 * Write a program to find the smallest multiple of an integer 'n'
 * such that its digits are only zeros and nines. 
 * Use a queue of strings to generate the zeros-and-nines digit. 
 * Program must return the multiple as an integer, not a string. 
 * Complete the queue implementation and use it to find the multiple. 
 * MODIFY ONLY THOSE SECTIONS MARKED WITH THE 'TODO' COMMENT
 * DON'T MODIFY THE MAIN FUNCTION.
 * DON'T ADD ANY 'printf' FUNCTION.
 */
"""

def get_multiple(n):
    Q = deque()
    Q.append('9')

    head = Q.popleft()
    multiple = int(head)
    Q.append(head + '0')
    Q.append(head + '9')
    while multiple % n != 0:
        head = Q.popleft()
        multiple = int(head)
        Q.append(head + '0')
        Q.append(head + '9')
    return multiple
        
def generate_program_input():    
    return [str(numpy.random.randint(10,100))]

def evaluate(program_input, program_output):
    try:
        program_output = int(program_output.strip())
    except:
        program_output = -1
    expected = get_multiple(int(program_input[0]))
    return program_output == expected, str(expected)

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
