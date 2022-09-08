#coding=utf-8
import sys
import numpy
import subprocess
import string

"""
/*
 * URLIFY A STRING
 *
 * Instructions:
 * URLify a string (which is defined inside a struct),
 * i.e., replace all spaces by the string "%20", e.g:
 * If the input string is "hello world!", the output string should be "hello%20world!"
 * The program must receive the input string as a command line parameter
 * and print only the resulting string, e.g., the command:
 *     ./a.out "hello world!"
 * should print the output
 *     hello%20world
 * MODIFY ONLY THE SECTIONS MARKED WITH THE 'TODO' COMMENT
 * DON'T ADD ANY LIBRARY
 * DON'T MODIFY THE MAIN FUNCTION.
 * DON'T ADD ANY 'printf' FUNCTION.
 */
"""

test_strings = open("TestStrings.txt", 'r').readlines()
test_strings = [x.strip() for x in test_strings]

def generate_program_input():
    return [numpy.random.choice(test_strings).strip()]

def evaluate(program_input, program_output):
    expected = program_input[0].replace(" ", "%20")
    program_output = program_output.strip()
    if not all(c in string.printable for c in program_output):
        return False, expected
    return expected == program_output, expected
    

if __name__ == '__main__':
    assignment_file = sys.argv[1]
    test_strings = ["Imagine","all the people", "Living life", "in peace", "Let it be", "Don't stop me now"]
    program_input = generate_program_input(test_strings)
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
