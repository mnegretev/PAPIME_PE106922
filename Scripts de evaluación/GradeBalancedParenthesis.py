#coding=utf-8
import sys
import numpy
import math
import subprocess

"""
/*
 * BALANCED PARENTHESIS
 * 
 * Instructions:
 * Implement an algorithm to check whether an expression has balanced
 * parentheses, brackets and braces. 
 * You can assume that the expression only has numbers, operators and the mentioned symbols.
 * Complete the stack implementation and use it to check the expression.
 * MODIFY ONLY THOSE SECTIONS MARKED WITH THE 'TODO' COMMENT
 * DON'T MODIFY THE MAIN FUNCTION.
 * DON'T ADD ANY 'printf' FUNCTION.
 */
"""
def generate_expression(counter):
    if numpy.random.randint(2) == 0 or counter > 5:
        op1 = str(numpy.random.randint(1,100))
    else:
        op1 = generate_expression(counter+1)
    if numpy.random.randint(2) == 0 or counter > 5:
        op2 = str(numpy.random.randint(1,100))
    else:
        op2 = generate_expression(counter+1)
    x = numpy.random.randint(3)
    if x == 0:
        return '(' + op1 + numpy.random.choice(['+','-','*','/']) + op2 + ')'
    elif x == 1:
        return '[' + op1 + numpy.random.choice(['+','-','*','/']) + op2 + ']'
    else:
        return '{' + op1 + numpy.random.choice(['+','-','*','/']) + op2 + '}'
    
def check_balance(s):
    stack = []
    for c in s:
        if c ==  '(' or c == '{' or c == '[':
            stack.append(c)
        elif c == ')' and (len(stack) == 0 or stack.pop() != '('):
            return False
        elif c == ']' and (len(stack) == 0 or stack.pop() != '['):
            return False
        elif c == '}' and (len(stack) == 0 or stack.pop() != '{'):
            return False
    return len(stack) == 0

def generate_program_input():
    s = generate_expression(0)
    if numpy.random.randint(2) == 0:
        s = s.replace(numpy.random.choice(['(',')','[',']','{','}']), "", numpy.random.randint(1,4))
    return [s]

def evaluate(program_input, program_output):
    program_output = program_output.strip()
    expected = '1' if check_balance(program_input[0]) else '0'
    return program_output == expected, expected
    

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
