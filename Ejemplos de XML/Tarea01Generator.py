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
    return str(numpy.random.randint(1,20))

def get_target_values():
    n = numpy.random.randint(1,20)
    expected = ""
    for i in range(n):
        expected += "Hello world!_"
    return str(n), expected


for i in range(200):
    args_str, expected_output = get_target_values()
    file_content +="      \n<testrun args=\"" + args_str + "\" cout=\"" + expected_output  + "\" />"
    

file_content += """
    </testbed>
  </testbeds>
</testconf>
"""

f = open("Tarea01 - Hello World.xml", 'w');
f.write(file_content)
