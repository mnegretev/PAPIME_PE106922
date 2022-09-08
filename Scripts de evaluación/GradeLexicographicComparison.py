#coding=utf-8
import sys
import numpy
import subprocess

"""
/*
 * LEXICOGRAPHIC STRING COMPARISON
 *
 * Instructions:
 * Write a program to compare two strings.
 * The program receives as command line arguments the two strings to be compared
 * and returns the integer corresponding to the comparison result. 
 * The comparison to be implemented must be the same than the strcmp function
 * THE USE OF THE STRCMP FUNCTION INCLUDED IN THE STRING LIBRARY IS NOT ALLOWED
 * MODIFY ONLY THE string_compare FUNCTION
 * DON'T ADD ANY 'printf' FUNCTION.
 */
"""

test_strings = open("TestStrings.txt", 'r').readlines()
test_strings = [x.strip() for x in test_strings]

def generate_program_input():
    n1 = numpy.random.randint(len(test_strings))
    n2 = numpy.random.randint(len(test_strings))
    return [test_strings[n1], test_strings[n2]]

def evaluate(program_input, program_output):
    program_output = program_output.strip()
    s1 = program_input[0]
    s2 = program_input[1]
    a1 = list(s1)
    a2 = list(s2)
    a1.append('\0')
    a2.append('\0')
    i = 0;
    while a1[i] == a2[i] and a1[i] != '\0':
        i+=1
    expected = str(ord(a1[i]) - ord(a2[i]))
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
