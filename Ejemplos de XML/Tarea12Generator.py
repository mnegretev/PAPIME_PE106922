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
    return s

def get_target_values():
    s = generate_program_input()
    expected = '1' if check_balance(s) else '0'
    return "'"+s+"'", expected

for i in range(200):
    args_str, expected_output = get_target_values()
    file_content +="      \n<testrun args=\"" + args_str + "\" cout=\"" + expected_output  + "\" />"
    

file_content += """
    </testbed>
  </testbeds>
</testconf>
"""

f = open("Tarea12 - Paréntesis Balanceados.xml", 'w');
f.write(file_content)
