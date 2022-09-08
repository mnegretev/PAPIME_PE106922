#coding=utf-8
import sys
import numpy
import subprocess

"""
/*
 * LEAST COMMON MULTIPLE AND GREATEST COMMON DIVISOR
 *
 * Instructions:
 * Write a program to calculate the Least Common Multiple and the
 * Greatest Common Divisor of two positive integers.
 * 
 * THE USE OF EXTRA LIBRARIES IS NOT ALLOWED
 * MODIFY ONLY THE INDICATED FUNCTIONS
 * DON'T ADD ANY PRINTF FUNCTION
 */
"""

def calculate_gcd(a, b):
    if a==b:
        return a
    if a > b:
        return calculate_gcd(a-b, b)
    return calculate_gcd(a, b-a)

def calculate_lcm(a,b):
    gcd = calculate_gcd(a, b)
    return a*b/gcd

def generate_program_input():
    a = numpy.random.randint(10,1000)
    b = numpy.random.randint(10,1000)
    return [str(a), str(b)]

def evaluate(program_input, program_output):
    a = int(program_input[0])
    b = int(program_input[1])
    expected_gcd = calculate_gcd(a,b)
    expected_lcm = calculate_lcm(a,b)
    expected = str(str(expected_lcm) + "\n" + str(expected_gcd))
    program_output = program_output.split()
    try:
        program_lcm = int(program_output[0])
        program_gcd = int(program_output[1])
        return program_gcd == expected_gcd and program_lcm == expected_lcm, expected
    except:
        return False, expected


if __name__ == '__main__':
    assignment_file = sys.argv[1]
    program_input = generate_program_input()
    subprocess.call(["gcc", assignment_file, "-I", ".", "-w", "-o", "/dev/shm/a.out"])
    sp = subprocess.Popen(['/dev/shm/a.out'] + program_input, stdout=subprocess.PIPE)
    (program_output, program_error) = sp.communicate()
    result, expected_output = evaluate(program_input, program_output)
    if result:
        print("Correct result with the following values:")
    else:
        print("The program failed with the following values:")
    print("Program input:   " + str(program_input))
    print("Expected value:\n" + str(expected_output))
    print("Program output:\n" + program_output.decode("utf-8"))
