#coding=utf-8
import sys
import numpy
import subprocess

"""
/*
 * DETERMINE IF A YEAR IS A LEAP YEAR.
 *
 * Instructions:
 * Write an algorithm to calculate whether a given year
 * will be a leap year or not. 
 * Modify the function 'is_leap_year' such that it returns '1'
 * if the argument 'year' is a leap year, and '0', otherwise.
 * MODIFY ONLY THE SECTION MARKED WITH THE 'TODO' COMMENT
 * DON'T MODIFY THE MAIN FUNCTION AND DON'T CHANGE THE FUNCTION NAMES.
 * DON'T ADD ANY 'printf' FUNCTION.
 */
"""

def generate_program_input():
    y = numpy.random.randint(1584,3000)
    x = numpy.random.randint(0,3)
    if x == 1:
        y = y - y%4
    return [str(y)]

def evaluate(program_input, program_output):
    program_output = program_output.strip()
    test = int(program_input[0])
    if ((test%4) == 0 and (test%100) != 0) or (test%400)==0:
        expected = 'True'
    else:
        expected = 'False'
    return expected == program_output, expected
    

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
