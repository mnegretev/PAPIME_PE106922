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

def get_multiple(n):
    Q = deque()
    Q.append('9')

    head = Q.popleft()
    multiple = int(head)
    Q.append(head + '0')
    Q.append(head + '9')
    while multiple % n != 0:
        head = Q.popleft()
        multiple = int(head)
        Q.append(head + '0')
        Q.append(head + '9')
    return multiple
        

def get_target_values():
    n = numpy.random.randint(10,100)
    expected = get_multiple(n)
    return str(n), str(expected)


for i in range(200):
    args_str, expected_output = get_target_values()
    file_content +="      \n<testrun args=\"" + args_str + "\" cout=\"" + expected_output  + "\" />"
    

file_content += """
    </testbed>
  </testbeds>
</testconf>
"""

f = open("Tarea15 - Ceros y nueves.xml", 'w');
f.write(file_content)
