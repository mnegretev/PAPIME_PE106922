import numpy
import math

file_content = """
<testconf language="C"> <!-- Soporta solo "C" y "Python" -->
  <build score="2">   <!-- Cuantos puntos solo porque compile. En python esto se ignora -->
    <flags>-lm</flags> <!-- Banderas de compilacion -->
  </build>
  <testbeds>
    <testbed score="8" type="proportional" onerror="halt">  <!-- Tipos: ver comentario de arriba -->
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
    return [op] + generate_prefix(counter - 1) + generate_prefix(counter - 1)

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
    result   = check_postfix(expression) if choice == 0 else check_prefix(expression.copy())
    while result is None:
        expression = generate_postfix(counter) if choice == 0 else generate_prefix(counter)
        result = check_postfix(expression) if choice == 0 else check_prefix(expression.copy())
    return expression

def get_target_values():
    expression = generate_program_input()
    expected = check_prefix(expression.copy()) if expression[0] in ['+','*','/','-'] else check_postfix(expression)
    input_str = "";
    for s in expression:
        input_str += "'" + s + "' "
    return input_str, "between(" + str(expected - 0.01*expected) + "," + str(expected + 0.01*expected) + ")"

for i in range(200):
    args_str, expected_output = get_target_values()
    file_content +="      \n<testrun args=\"" + args_str + "\" cout=\"" + expected_output  + "\" />"
    

file_content += """
    </testbed>
  </testbeds>
</testconf>
"""

f = open("Tarea13 - Notación postfix y prefix.xml", 'w');
f.write(file_content)
