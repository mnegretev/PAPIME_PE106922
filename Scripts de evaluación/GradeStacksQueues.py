#coding=utf-8
import sys
import numpy
import subprocess
from collections import deque

"""
/*
 * STACK AND QUEUES
 *
 * Instructions:
 * Implement a Stack and a Queue of chars.
 *
 * MODIFY ONLY THOSE SECTIONS MARKED WITH THE 'TODO' COMMENT
 * DON'T MODIFY THE MAIN FUNCTION.
 * DON'T ADD ANY 'printf' FUNCTION UNLESS INDICATED
 */
"""

test_strings = open("TestStrings.txt", 'r').readlines()
test_strings = [x.strip() for x in test_strings]

def is_valid_with_stack(str1):
    S = []
    try:
        for c in str1:
            if c =='*':
                S.pop()
            else:
                S.append(c)
    except:
        return False, ""
    return len(S) > 0, "".join(S)

def is_valid_with_queue(str1):
    Q = deque()
    try:
        for c in str1:
            if c =='*':
                Q.popleft()
            else:
                Q.append(c)
    except:
        return False, ""
    return len(Q) > 0, "".join(Q)

def generate_program_input():
    op  = "stack" if numpy.random.randint(2)==0 else "queue"
    st  = test_strings[numpy.random.randint(len(test_strings))]
    while len(st) > 40:
        st  = test_strings[numpy.random.randint(len(test_strings))]
    idx = numpy.random.randint(len(st), size=numpy.random.randint(len(st)//2))
    for i in idx:
        st = st[:i] + '*' + st[i:]
    [is_valid, resulting_str] = is_valid_with_stack(st) if op == 'stack' else is_valid_with_queue(st)
    while not is_valid:
        st  = test_strings[numpy.random.randint(len(test_strings))]
        while len(st) > 40:
            st  = test_strings[numpy.random.randint(len(test_strings))]
        idx = numpy.random.randint(len(st), size=numpy.random.randint(len(st)//2))
        for i in idx:
            st = st[:i] + '*' + st[i:]
        [is_valid, resulting_str] = is_valid_with_stack(st) if op == 'stack' else is_valid_with_queue(st)
    return [op, st]

def evaluate(program_input, program_output):
    try:
        program_output = program_output.strip().replace("\n","")
    except:
        program_output = program_output.strip().decode().replace("\n","")
    op = program_input[0]
    st = program_input[1]
    [is_valid, expected] = is_valid_with_stack(st) if op == 'stack' else is_valid_with_queue(st)
    if expected[0] == ' ':
        expected = expected[1:]
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
    print("Program output:\n" + program_output.decode())
