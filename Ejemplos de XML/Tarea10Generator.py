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

def generate_program_input():
    b = numpy.random.randint(2,21)
    x = numpy.random.randint(20,10000)
    return [x, b]

def get_target_values():
    x,b = generate_program_input()
    input_args = str(x) + " " + str(b)
    symbols = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J']
    n = math.floor(math.log(x)/math.log(b))+1;
    expected = ""
    while n>0:
        expected = symbols[x%b] + expected
        n -= 1
        x = x//b
    return input_args, expected

for i in range(200):
    args_str, expected_output = get_target_values()
    file_content +="      \n<testrun args=\"" + args_str + "\" cout=\"" + expected_output  + "\" />"
    

file_content += """
    </testbed>
  </testbeds>
</testconf>
"""

f = open("Tarea10 - Notación posicional.xml", 'w');
f.write(file_content)
