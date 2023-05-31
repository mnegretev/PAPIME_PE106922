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

def generate_program_input():
    x1 = round(numpy.random.uniform(-10,10), 2)
    x2 = round(numpy.random.uniform(-10,10), 2)
    x3 = round(numpy.random.uniform(-10,10), 2)
    x4 = round(numpy.random.uniform(-10,10), 2)
    return [x1, x2, x3, x4]

def get_target_values():
    r1, i1, r2, i2 = generate_program_input()
    expected_mag = math.sqrt((r1+r2)**2 + (i1+i2)**2)
    input_str = str(r1) + " " + str(i1) + " " + str(r2) + " " + str(i2)
    return input_str, "between(" + str(expected_mag - 0.01*expected_mag) + ","+ str(expected_mag+0.01*expected_mag) + ")"

for i in range(200):
    args_str, expected_output = get_target_values()
    file_content +="      \n<testrun args=\"" + args_str + "\" cout=\"" + expected_output  + "\" />"
    

file_content += """
    </testbed>
  </testbeds>
</testconf>
"""

f = open("Tarea07 - Números complejos.xml", 'w');
f.write(file_content)
