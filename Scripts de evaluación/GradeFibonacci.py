#coding=utf-8
import sys
import numpy
import subprocess

"""
/*
 * FIBONACCI SEQUENCE
 *
 * Instructions:
 * Write an algorithm to generate the first 'n' Fibonacci numbers.
 * Consider [0,1] as the first two numbers. Assume n>=2
 * MODIFY ONLY THE SECTION MARKED WITH THE 'TODO' COMMENT
 * DON'T ADD ANY 'printf' FUNCTION.
 */
"""

def generate_program_input():
    return [str(numpy.random.randint(2,40))]

def evaluate(program_input, program_output):
    program_output = program_output.strip()
    n = int(program_input[0])
    fib = [0,1]
    for i in range(2,n):
        fib.append(fib[i-1] + fib[i-2])
    expected = ""
    for x in fib:
        expected += str(x) + "  "
    
    expected = expected.strip()
    return expected.replace(" ","") == program_output.replace(" ",""), expected
    

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
