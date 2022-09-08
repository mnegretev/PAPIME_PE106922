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

def generate_postfix(counter):
    op1 = str(round(numpy.random.uniform(1.0, 10.0), 2))
    op2 = str(round(numpy.random.uniform(1.0, 10.0), 2))
    op  = numpy.random.choice(['+','*','/','-'])
    if counter == 0 or numpy.random.randint(0,2) == 0:
        return [op1, op2, op]
    return generate_postfix(counter - 1) + generate_postfix(counter - 1) + [op]
    
def generate_prefix(counter):
    op1 = str(round(numpy.random.uniform(1.0, 10.0), 2))
    op2 = str(round(numpy.random.uniform(1.0, 10.0), 2))
    op  = numpy.random.choice(['+','*','/','-'])
    if counter == 0 or numpy.random.randint(0,2) == 0:
        return [op, op1, op2]
    return [op] + generate_postfix(counter - 1) + generate_postfix(counter - 1)

def check_postfix(expression):
    stack = []
    try:
        for s in expression:
            if s in ['+','*','/','-']:
                op2 = stack.pop()
                op1 = stack.pop()
                res = op1+op2 if s=='+' else op1-op2 if s=='-' else op1*op2 if s=='*' else op1/op2
                stack.append(res)
            else:
                stack.append(float(s))
    except:
        return None
    return stack.pop()

def check_prefix(expression):
    stack = []
    expression.reverse()
    try:
        for s in expression:
            if s in ['+','*','/','-']:
                op1 = stack.pop()
                op2 = stack.pop()
                res = op1+op2 if s=='+' else op1-op2 if s=='-' else op1*op2 if s=='*' else op1/op2
                stack.append(res)
            else:
                stack.append(float(s))
    except:
        return None
    return stack.pop()

def generate_program_input():
    counter = numpy.random.randint(3,10)
    choice  = numpy.random.randint(0,2)
    expression = generate_postfix(counter) if choice == 0 else generate_prefix(counter)
    expected   = check_postfix(expression) if choice == 0 else check_prefix(expression)
    while expected is None:
        expression = generate_postfix(counter) if choice == 0 else generate_prefix(counter)
        expected   = check_postfix(expression) if choice == 0 else check_prefix(expression)
    return expression

def evaluate(program_input, program_output):
    try:
        result = float(program_output.strip())
    except:
        result = float("inf")
    expected = check_prefix(program_input) if program_input[0] in ['+','*','/','-'] else check_postfix(program_input)
    return abs(expected - result) < 0.1, str(round(expected, 4))

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
