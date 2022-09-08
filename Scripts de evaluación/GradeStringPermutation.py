#coding=utf-8
import sys
import numpy
import subprocess

"""
/*
 * STRING PERMUTATION
 *
 * Instructions:
 * Write a program to determine if a string is a permutation of another one.
 * A string S1 is said to be a permutation of another string S2 if the
 * total number of each different character in S1 is the same than string S2.
 * The program receives as command line arguments the two strings two be analized.
 * The output of the program must be only '1', if S1 is permutation of S2, and '0', otherwise.
 * THE USE OF EXTRA LIBRARIES IS NOT ALLOWED.
 * MODIFY ONLY THE is_permutation FUNCTION.
 * DON'T ADD ANY 'printf' FUNCTION.
 */
"""

test_strings = open("TestStrings.txt", 'r').readlines()
test_strings = [x.strip() for x in test_strings]

def generate_program_input():
    str_test1 = numpy.random.choice(test_strings).strip()
    if numpy.random.randint(0,2) == 0:
        str_test2 = numpy.random.choice(test_strings).strip()
    else:
        str_test2 = str_test1
        str_test2 = list(str_test2)
        str_test2.sort()
        str_test2 = "".join(str_test2)
    return [str_test1, str_test2]

def evaluate(program_input, program_output):
    program_output = program_output.strip()
    s1 = program_input[0]
    s2 = program_input[1]
    a1 = list(s1)
    a2 = list(s2)
    a1.sort()
    a2.sort()
    if a1 == a2:
        expected = '1'
    else:
        expected = '0'
    return expected == program_output, expected
    

if __name__ == '__main__':
    assignment_file = sys.argv[1]
    test_strings = ["Imagine","all the people", "Living life", "in peace", "Let it be", "Don't stop me now"]
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
