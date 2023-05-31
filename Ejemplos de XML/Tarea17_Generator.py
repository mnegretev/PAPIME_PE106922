#coding=utf-8
import sys
import numpy
import subprocess
from collections import deque

"""
/*
 * ESTRUCTURAS DE DATOS Y ALGORITMOS I
 * FACULTAD DE INGENIERÍA, UNAM, 2020-2
 * P R A C T I C E   05
 * Instructions:
 * Implement a Stack using two queues and a Queue using two stacks. 
 * Don't modify the Stack.h nor Queue.h files.
 * To manipulate the data structures, only the following functions are allowed:
 *    stack_int_push
 *    stack_int_pop
 *    stack_int_is_full
 *    stack_int_is_empty
 *    queue_int_enqueue
 *    queue_int_dequeue
 *    queue_int_is_full
 *    queue_int_is_empty
 * These functions are already implemented in the Stack.h and Queue.h files.
 * MODIFY ONLY THE SECTIONS MARKED WITH THE 'TODO' COMMENT.
 * DON'T MODIFY THE MAIN FUNCTION.
 * DON'T ADD ANY 'printf' FUNCTION.
 */
"""

def generate_program_input():
    n = numpy.random.randint(4,20)
    stack = []
    queue = deque()
    choices1 = ['enq','deq','push','pop']
    choices2 = ['enq','push']
    seq = []
    while n > 0:
        if len(stack) == 0 or len(queue) == 0:
            op = numpy.random.choice(choices2)
        else:
            op = numpy.random.choice(choices1)
        seq.append(op)
        n -= 1
        if op == 'enq' or op == 'push':
            k = numpy.random.randint(0,10)
            seq.append(str(k))
        if op == 'enq':
            queue.append(k)
        elif op == 'deq':
            queue.popleft()
        elif op == 'push':
            stack.append(k)
        else:
            stack.pop()
    return seq

def evaluate(program_input, program_output):
    stack = []
    queue = deque()
    for i in range(len(program_input)):
        if program_input[i] == 'enq':
            queue.append(int(program_input[i+1]))
        elif program_input[i] == 'deq':
            queue.popleft()
        elif program_input[i] == 'push':
            stack.append(int(program_input[i+1]))
        elif program_input[i] == 'pop':
            stack.pop()
    expected = ""
    if len(stack) > 0:
        expected += "Peek: " + str(stack[len(stack) - 1]) + "\n"
    if len(queue) > 0:
        expected += "Tail: " + str(queue[len(queue)-1])
        expected += "\nHead: " + str(queue[0])
    return program_output.replace("\n","") ==  expected.replace("\n",""), expected
    

if __name__ == '__main__':
    assignment_file = sys.argv[1]
    program_input = generate_program_input()
    subprocess.call(["gcc", assignment_file, "-I",".", "-w", "-o", "/dev/shm/a.out"])
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
