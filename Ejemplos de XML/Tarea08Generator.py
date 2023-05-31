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
    op = numpy.random.choice(['dot', 'mag', 'ang'])
    v1 = [round(numpy.random.uniform(-10, 10),2), round(numpy.random.uniform(-10, 10),2), round(numpy.random.uniform(-10, 10),2)]
    v2 = [round(numpy.random.uniform(-10, 10),2), round(numpy.random.uniform(-10, 10),2), round(numpy.random.uniform(-10, 10),2)]
    return op, v1, v2

def get_target_values():
    op, v1, v2 = generate_program_input()
    if op == "add":
        expected = [v1[0]+v2[0], v1[1]+v2[1], v1[2]+v2[2]]
    elif op == "sub":
        expected = [v1[0]-v2[0], v1[1]-v2[1], v1[2]-v2[2]]
    elif op == "dot":
        expected = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]
    elif op == "cross":
        ax = v1[0]
        ay = v1[1]
        az = v1[2]
        bx = v2[0]
        by = v2[1]
        bz = v2[2]
        vx =  ay*bz - by*az
        vy = -ax*bz + bx*az
        vz =  ax*by - bx*ay
        expected = [vx, vy, vz]
    elif op == "mag":
        expected = math.sqrt(v1[0]*v1[0] + v1[1]*v1[1] + v1[2]*v1[2])
    elif op == "unit":
        mag = math.sqrt(v1[0]*v1[0] + v1[1]*v1[1] + v1[2]*v1[2])
        if mag == 0:
            expected = [0,0,0]
        else:
            expected = [v1[0]/mag, v1[1]/mag, v1[2]/mag]
    elif op == "ang":
        mag1 = math.sqrt(v1[0]*v1[0] + v1[1]*v1[1] + v1[2]*v1[2])
        mag2 = math.sqrt(v2[0]*v2[0] + v2[1]*v2[1] + v2[2]*v2[2])
        if mag1 == 0 or mag2 == 0:
            expected = 0
        else:
            expected = math.acos((v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2])/(mag1*mag2))
    else:
        expected = 0
    try:
        expected = [round(expected[0],6), round(expected[1],6), round(expected[2],6)]
    except:
        expected = round(expected, 6)

    input_str = str(v1[0]) + " " + str(v1[1]) + " " + str(v1[2]) + " " + str(v2[0]) + " " + str(v2[1]) + " " + str(v2[2])
    return input_str, "between(" + str(expected-0.01*abs(expected)) + "," + str(expected+0.01*abs(expected)) + ")"

for i in range(200):
    args_str, expected_output = get_target_values()
    file_content +="      \n<testrun args=\"" + args_str + "\" cout=\"" + expected_output  + "\" />"
    

file_content += """
    </testbed>
  </testbeds>
</testconf>
"""

f = open("Tarea08 - Vectores en R3.xml", 'w');
f.write(file_content)
