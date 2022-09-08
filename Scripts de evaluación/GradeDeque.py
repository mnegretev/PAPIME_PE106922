#coding=utf-8
import sys
import numpy
import subprocess
from collections import deque

"""
/*
 * DOUBLE ENDED QUEUE
 *
 * Instructions:
 * Implement a Double Ended Queue to solve sliding window maximum problem.
 * Array data and size of subarray are passed as command line arguments:
 * ./a.out -k k_value -n n1 n2 n3 n4 ...
 * 
 * MODIFY ONLY THE SECTIONS MARKED WITH THE 'TODO' COMMENT.
 * DON'T MODIFY THE MAIN FUNCTION.
 * DON'T ADD ANY 'printf' FUNCTION.
 */
"""
def sliding_window_max(k, data):
    Q = deque()
    M = []
    for i in range(k):
        while len(Q) > 0 and data[i] >= data[Q[-1]]:
            Q.pop()
        Q.append(i)
    for i in range(k,len(data)):
        M.append(data[Q[0]])
        while len(Q) > 0 and Q[0] <= i-k:
            Q.popleft()
        while len(Q) > 0 and data[i] >= data[Q[-1]]:
            Q.pop()
        Q.append(i)
    M.append(data[Q[0]])
    return M

def generate_program_input():
    k = numpy.random.randint(3,11)
    n = numpy.random.randint(20,50)
    return ['-k', str(k), '-n'] + [str(numpy.random.randint(-100, 101)) for i in range(n)]
    
def evaluate(program_input, program_output):
    try:
        result = [int(x) for x in program_output.split()]
    except:
        result = []
    k = int(program_input[1])
    data = [int(d) for d in program_input[3:]]
    expected = sliding_window_max(k,data)
    return result == expected, str(expected)

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
    print("Program input:  " + str(program_input))
    print("Expected value: " + str(expected_output))
    print("Program output: " + program_output      )
