import numpy


file_content = """
<testconf language="C"> <!-- Soporta solo "C" y "Python" -->
  <build score="2">   <!-- Cuantos puntos solo porque compile. En python esto se ignora -->
    <flags>-lm</flags> <!-- Banderas de compilacion -->
  </build>
  <testbeds>
    <testbed score="8" type="proportional" onerror="halt">  <!-- Tipos: ver comentario de arriba -->
"""

def calculate_gcd(a, b):
    if a==b:
        return a
    if a > b:
        return calculate_gcd(a-b, b)
    return calculate_gcd(a, b-a)

def calculate_lcm(a,b):
    gcd = calculate_gcd(a, b)
    return a*b/gcd

for i in range(200):
    a = numpy.random.randint(10,1000)
    b = numpy.random.randint(10,1000)
    expected_gcd = int(calculate_gcd(a,b))
    expected_lcm = int(calculate_lcm(a,b))
    args_str = str(a) + " " + str(b)
    expected_output = str(str(expected_lcm) + "_" + str(expected_gcd))
    file_content +="      \n<testrun args=\"" + args_str + "\" cout=\"" + expected_output  + "\" />"
    

file_content += """
    </testbed>
  </testbeds>
</testconf>
"""

f = open("Tarea03 - MCM y MCD.xml", 'w');
f.write(file_content)
