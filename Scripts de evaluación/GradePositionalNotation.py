#coding=utf-8
import sys
import numpy
import math
import subprocess

"""
/*
 * POSITIONAL NOTATION
 *
 * Instructions:
 * Write a program to convert a given number in decimal to a differente base. 
 * Decimal number and desired base are passed as a command line arguments.
 * Example: The command:
 *    ./a.out 54 13
 * (convert 54 to base 13) should print the output:
 *    42
 * Use of libraries different to the ones already included is not allowed. 
 * ONLY MODIFY THE SECTIONS MARKED WITH THE 'TODO' COMMENT.
 * DON'T MODIFY THE MAIN FUNCTION.
 * DON'T ADD ANY 'printf' FUNCTION.
 */
"""

def generate_program_input():
    y = numpy.random.randint(2,21)
    x = numpy.random.randint(20,10000)
    return [str(x), str(y)]

def evaluate(program_input, program_output):
    result = program_output.strip()
    x = int(program_input[0])
    b = int(program_input[1])
    symbols = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J']
    n = math.floor(math.log(x)/math.log(b))+1;
    expected = ""
    while n>0:
        expected = symbols[x%b] + expected
        n -= 1
        x = x//b
    return expected == result, expected
    

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
