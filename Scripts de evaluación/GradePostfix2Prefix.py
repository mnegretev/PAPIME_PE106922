#coding=utf-8
import sys
import numpy
import subprocess

"""
/*
 * POSTFIX AND PREFIX NOTATIONS
 * 
 * Instructions:
 * Implement the algorithms to convert arithmetic expressions from prefix to postfix notation
 * and viceversa. 
 * The expression will be composed only by digits 0-9 and operators +*-/
 * You can assume a sintactically correct expression.
 * The desired conversion is indicated with the '2pre' and '2post'
 * arguments for postfix-to-prefix and prefix-to-postfix conversions respectively,
 * followed by the expression to be converted. 
 * Example: the command
 *     ./Practice06 2pre 12+  
 * transforms the postfix expression '12+' to prefix notation. The program output should be:
 *     +12
 *
 * Restrictions.
 * You cannot use other libraries apart from the ones already included.
 * You can use the <string.h> library for string manipulation or implement your own functions.
 * Also, for stack operations you can use the Stack.h file or implement your own stack. 
 * IF YOU IMPLEMENT YOUR OWN FUNCTIONS, THEY MUST BE INCLUDED IN THIS FILE.
 * THE ALREADY DECLARED FUNCTIONS ARE JUST SUGGESTIONS. YOU CAN IMPLEMENT YOUR ALGORITHM 
 * THE WAY YOU CHOOSE. JUST:
 * DON'T CHANGE THE 'main' FUNCTION.
 * DON'T ADD ANY 'printf' FUNCTION.
 */
"""

def generate_postfix_expression():
    #This function generates a random postfix expression with
    #a random length between 3 and 20
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
            expression += op1
        if numpy.random.randint(0,2) == 1 and len(stack) != 0:
            op2 = stack.pop()
        else:
            op2 = numpy.random.choice(operands)
            expression += op2
        op = numpy.random.choice(operators)
        expression += op
        stack.append(op1 + op2 + op)
        
    while len(stack) > 1:
        op1 = stack.pop()
        op2 = stack.pop()
        op = numpy.random.choice(operators)
        stack.append(op1+op2+op)
        expression += op
    return expression

def generate_prefix_expression():
    #This function generates a random prefix expression with
    #a random length between 3 and 20
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
    return expression

def postfix2prefix(s1):
    stack = []
    s1 = list(s1)
    for c in s1:
        if c in ['+','-','*','/']:
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(c + op1 + op2)
        else:
            stack.append(c)
    return stack.pop()

def prefix2postfix(s1):
    stack = []
    s1 = list(s1)
    for i in range(len(s1)-1, -1, -1):
        c = s1[i]
        if c in ['+','-','*','/']:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op1 + op2 + c)
        else:
            stack.append(c)
    return stack.pop()

def generate_program_input():
    option = numpy.random.choice([0,1])
    if option == 1:
        op = "2post"
        str_test = generate_prefix_expression()
    else:
        op = "2pre"
        str_test = generate_postfix_expression()
    return [op, str_test]

def evaluate(program_input, program_output):
    program_output = program_output.strip()
    if program_input[0] == '2pre':
        expected = postfix2prefix(program_input[1])
    else:
        expected = prefix2postfix(program_input[1])
    return program_output == expected, expected

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
