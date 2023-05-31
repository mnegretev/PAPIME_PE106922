import numpy
import math
from collections import deque

file_content = """
<testconf language="C"> <!-- Soporta solo "C" y "Python" -->
  <build score="2">   <!-- Cuantos puntos solo porque compile. En python esto se ignora -->
    <flags>-lm</flags> <!-- Banderas de compilacion -->
  </build>
  <testbeds>
    <testbed score="8" type="proportional" onerror="halt">  <!-- Tipos: ver comentario de arriba -->
"""

def get_binary_string(n):
    Q = deque()
    Q.append('1')
    for i in range(n):
        head = Q.popleft()
        Q.append(head + "0")
        Q.append(head + "1")
    return head

def generate_program_input():    
    return [str(numpy.random.randint(10,10000))]

def get_target_values():
    n = numpy.random.randint(10,10000)
    expected = get_binary_string(n)
    return str(n), expected

for i in range(200):
    args_str, expected_output = get_target_values()
    file_content +="      \n<testrun args=\"" + args_str + "\" cout=\"" + expected_output  + "\" />"
    

file_content += """
    </testbed>
  </testbeds>
</testconf>
"""

f = open("Tarea14 - Colas para binarios.xml", 'w');
f.write(file_content)
