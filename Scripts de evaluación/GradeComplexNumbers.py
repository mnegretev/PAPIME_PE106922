#coding=utf-8
import sys
import numpy
import subprocess
import math

"""
/*
 * COMPLEX NUMBERS
 *
 * Instructions:
 * Write a program to calculate the sum of two complex numbers
 * and print the result expressed in the magnitude-angle form.
 * MODIFY ONLY THE SECTIONS MARKED WITH THE 'TODO' COMMENT
 * DON'T ADD ANY 'printf' FUNCTION.
 * DON'T MODIFY THE MAIN FUNCTION.
 */
"""

def generate_program_input():
    x1 = round(numpy.random.uniform(-10,10), 2)
    x2 = round(numpy.random.uniform(-10,10), 2)
    x3 = round(numpy.random.uniform(-10,10), 2)
    x4 = round(numpy.random.uniform(-10,10), 2)
    return [str(x1), str(x2), str(x3), str(x4)]

def evaluate(program_input, program_output):
    program_output = program_output.strip().split()
    if len(program_output) < 3:
        output_mag = 0
        output_ang = 0
    else:
        output_mag = float(program_output[0])
        output_ang = float(program_output[2])
    r1 = float(program_input[0])
    i1 = float(program_input[1])
    r2 = float(program_input[2])
    i2 = float(program_input[3])
    expected_mag = math.sqrt((r1+r2)**2 + (i1+i2)**2)
    expected_ang = math.atan2((i1+i2), (r1+r2))
    error = abs(expected_mag - output_mag) + abs(expected_ang - output_ang)
    return error < 0.001, str(round(expected_mag, 7)) + " ang " + str(round(expected_ang, 7))
    

if __name__ == '__main__':
    assignment_file = sys.argv[1]
    program_input = generate_program_input()
    subprocess.call(["gcc", assignment_file, "-w", "-o", "/dev/shm/a.out", "-lm"])
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
