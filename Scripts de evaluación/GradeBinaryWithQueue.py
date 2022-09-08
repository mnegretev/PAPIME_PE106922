#coding=utf-8
import sys
import numpy
import math
import subprocess
from collections import deque

"""
/*
 * BINARY FORMAT USING A QUEUE
 * 
 * Instructions:
 * Implement an algorithm to convert a decimal number to binary.
 * Conversion must be done using a queue of strings.
 * Program must return the binary string. 
 * Complete the queue implementation and use it to perform the conversion. 
 * MODIFY ONLY THOSE SECTIONS MARKED WITH THE 'TODO' COMMENT
 * DON'T MODIFY THE MAIN FUNCTION.
 * DON'T ADD ANY 'printf' FUNCTION.
 */
"""

def get_binary_string(n):
    Q = deque()
    Q.append('1')
    for i in range(n):
        head = Q.popleft()
        Q.append(head + "0")
        Q.append(head + "1")
    return head

def generate_program_input():    
    return [str(numpy.random.randint(10,10000))]

def evaluate(program_input, program_output):
    program_output = program_output.strip()
    expected = get_binary_string(int(program_input[0]))
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
