#coding=utf-8
import sys
import numpy
import subprocess

"""
/*
 * HELLO WORLD
 *
 * Instructions:
 * Write a program to print 'hello world' as many times as
 * indicated by the integer passed as command line parameters.
 * Example: the command
 *     ./a.out 3
 * should print the output:
 *     Hello world!
 *     Hello world!
 *     Hello world!
 * MODIFY ONLY THE SECTIONS MARKED WITH THE 'TODO' COMMENT
 */
"""

def generate_program_input():
    return [str(numpy.random.randint(1,20))]

def evaluate(program_input, program_output):
    n = int(program_input[0])
    expected = ""
    for i in range(n):
        expected += "Hello world!\n"
    return expected.lower() == program_output.lower(), expected    

if __name__ == '__main__':
    assignment_file = sys.argv[1]
    program_input = generate_program_input()
    subprocess.call(["rm", "/dev/shm/a.out"])
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
