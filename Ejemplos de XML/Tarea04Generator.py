import numpy


file_content = """
<testconf language="C"> <!-- Soporta solo "C" y "Python" -->
  <build score="2">   <!-- Cuantos puntos solo porque compile. En python esto se ignora -->
    <flags>-lm</flags> <!-- Banderas de compilacion -->
  </build>
  <testbeds>
    <testbed score="8" type="proportional" onerror="halt">  <!-- Tipos: ver comentario de arriba -->
"""

def generate_program_input():
    return [str(numpy.random.randint(2,40))]

def evaluate(program_input, program_output):
    program_output = program_output.strip()
    n = int(program_input[0])
    fib = [0,1]
    for i in range(2,n):
        fib.append(fib[i-1] + fib[i-2])
    expected = ""
    for x in fib:
        expected += str(x) + "  "
    
    expected = expected.strip()
    return expected.replace(" ","") == program_output.replace(" ",""), expected

for i in range(60):
    n = numpy.random.randint(2,40)
    fib = [0,1]
    for i in range(2,n):
        fib.append(fib[i-1] + fib[i-2])
    expected_output = ""
    for x in fib:
        expected_output += str(x) + "_"
    args_str = str(n)
    file_content +="      \n<testrun args=\"" + args_str + "\" cout=\"" + expected_output  + "\" />"
    

file_content += """
    </testbed>
  </testbeds>
</testconf>
"""

f = open("Tarea04 - Fibonacci.xml", 'w');
f.write(file_content)
