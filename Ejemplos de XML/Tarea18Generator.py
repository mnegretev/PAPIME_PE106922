import numpy
import math
from collections import deque

file_content = """
<testconf language="python"> <!-- Soporta solo "C" y "Python" -->
  <testbeds>
    <testbed score="10" type="proportional" onerror="None">  <!-- Tipos: ver comentario de arriba -->
"""

def generate_program_input():
    A = numpy.random.randint(1,1000,numpy.random.randint(10,30))
    B = ""
    for a in A:
        B += str(a) + " "
    return A, B

def get_target_values():
    A, A_str = generate_program_input()
    A.sort()
    C = []
    for a in A:
        C.append(a)
    return A_str, str(C)


for i in range(200):
    args_str, expected_output = get_target_values()
    file_content +="      \n<testrun args=\"" + args_str + "\" cout=\"" + expected_output  + "\" />"
    

file_content += """
    </testbed>
  </testbeds>
</testconf>
"""

f = open("Tarea18 - Ordenamiento por Burbuja.xml", 'w');
f.write(file_content)
