#coding=utf-8
import sys
import numpy
import subprocess

"""
/*
 * PREFIX NOTATION
 * 
 * Instructions:
 * Implement the algorithm to evaluate a PREFIX arithmetic expression.
 * Expression is passed as a command line argument where each character
 * is either an operarand or operator.
 * You can assume that the expression only have chars in  0-9, '+', '-', '*' and '/'.
 * You can use the Stack.h file for all stack operations.
 * You can assume that the expression is syntactically correct.
 * Manipulation of stack data can only be done with the is_empty, push and pop operations.
 * MODIFY ONLY THOSE SECTIONS MARKED WITH THE 'TODO' COMMENT
 * DON'T MODIFY THE MAIN FUNCTION.
 * DON'T ADD ANY 'printf' FUNCTION.
 */
"""

def generate_prefix_expression():
    #This function generates a random prefix expression with
    #a random length between 3 and 20
    valid = False
    while not valid:
        n = numpy.random.randint(3,20)
        stack = []
        operands = ['1','2','3','4','5','6','7','8','9']
        operators = ['+','-','*', '/']
        expression = ""
    
        while len(expression) < n:
            if numpy.random.randint(0,2) == 1 and len(stack) != 0:
                op1 = stack.pop()
            else:
                op1 = numpy.random.choice(operands)
                expression = op1 + expression
            if numpy.random.randint(0,2) == 1 and len(stack) != 0:
                op2 = stack.pop()
            else:
                op2 = numpy.random.choice(operands)
                expression = op2 + expression
            op = numpy.random.choice(operators)
            expression = op + expression
            stack.append(op + op1 + op2)
        
        while len(stack) > 1:
            op1 = stack.pop()
            op2 = stack.pop()
            op = numpy.random.choice(operators)
            stack.append(op+op1+op2)
            expression = op + expression
        try:
            evaluate_prefix(expression)
            valid = True
        except:
            pass
    return expression

def evaluate_prefix(s1):
    stack = []
    s1 = list(s1)
    for i in range(len(s1)-1, -1, -1):
        c = s1[i]
        if c in ['+','-','*','/']:
            op1 = stack.pop()
            op2 = stack.pop()
            if c == '+':
                stack.append(op1 + op2)
            elif c == '-':
                stack.append(op1 - op2)
            elif c == '*':
                stack.append(op1 * op2)
            elif c == '/':
                stack.append(op1 / op2)
        else:
            stack.append(float(c))
    return stack.pop()

def generate_program_input():
    return [generate_prefix_expression()]

def evaluate(program_input, program_output):
    expected = evaluate_prefix(program_input[0])
    try:
        program_output = float(program_output.strip())
        return abs(program_output - expected) < 0.001, str(expected)
    except:
        return False, str(expected)


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
    print("Program input:   " + str(program_input))
    print("Expected value:\n" + str(expected_output))
    print("Program output:\n" + program_output      )
