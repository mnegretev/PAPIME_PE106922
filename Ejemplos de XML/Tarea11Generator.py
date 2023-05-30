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
    functions = ['sin','cos','tan','sinh','cosh','tanh','asin','acos','atan','exp','log','sqrt']
    f = numpy.random.choice(functions)
    if f in ['sin','cos','sinh','cosh','tanh','atan','exp']:
        lower = numpy.random.uniform(-3.1415, -0.5)
        upper = numpy.random.uniform(0.5, 3.1415)
    elif f in ['tan','asin','acos']:
        lower = numpy.random.uniform(-0.9, -0.5)
        upper = numpy.random.uniform(0.5, 0.9)
    else:
        lower = numpy.random.uniform(0.5, 1.0)
        upper = numpy.random.uniform(2.0, 3.1415)
    step = numpy.random.choice([0.0001,0.0002,0.0003])
    return [f, lower, upper, step]

def get_target_values():
    functions = {'sin':math.sin,'cos':math.cos,'tan':math.tan,'sinh':math.sinh,'cosh':math.cosh,'tanh':math.tanh,
                 'asin':math.asin,'acos':math.acos,'atan':math.atan,'exp':math.exp,'log':math.log,'sqrt':math.sqrt}   
    f,lower,upper,step  = generate_program_input()
    str_args = f + " " + str(lower) + " " + str(upper) + " " + str(step)
    expected = 0
    x = lower
    while x < upper:
        expected += step*(functions[f](x) + functions[f](x+step))/2.0
        x += step
    expected_str = "between(" + str(expected-0.1) + "," + str(expected+0.1) + ")"
    return str_args, expected_str

for i in range(200):
    args_str, expected_output = get_target_values()
    file_content +="      \n<testrun args=\"" + args_str + "\" cout=\"" + expected_output  + "\" />"
    

file_content += """
    </testbed>
  </testbeds>
</testconf>
"""

f = open("Tarea11 - Integración numérica.xml", 'w');
f.write(file_content)
