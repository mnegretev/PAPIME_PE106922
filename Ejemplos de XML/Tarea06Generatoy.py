import numpy


file_content = """
<testconf language="C"> <!-- Soporta solo "C" y "Python" -->
  <build score="2">   <!-- Cuantos puntos solo porque compile. En python esto se ignora -->
    <flags>-lm</flags> <!-- Banderas de compilacion -->
  </build>
  <testbeds>
    <testbed score="8" type="proportional" onerror="halt">  <!-- Tipos: ver comentario de arriba -->
"""

test_strings = open("TestStrings.txt", 'r').readlines()
test_strings = [x.strip() for x in test_strings]

def generate_program_input():
    str_test1 = numpy.random.choice(test_strings).strip()
    if numpy.random.randint(0,2) == 0:
        str_test2 = numpy.random.choice(test_strings).strip()
    else:
        str_test2 = str_test1
        str_test2 = list(str_test2)
        str_test2.sort()
        str_test2 = "".join(str_test2)
    return [str_test1, str_test2]

def get_target_values():
    s1, s2 = generate_program_input()
    a1 = list(s1)
    a2 = list(s2)
    a1.sort()
    a2.sort()
    input_args = "'" + s1 + "' '" + s2 + "'"
    if a1 == a2:
        expected = '1'
    else:
        expected = '0'
    return input_args, expected


for i in range(100):
    args_str, expected_output = get_target_values()
    file_content +="      \n<testrun args=\"" + args_str + "\" cout=\"" + expected_output  + "\" />"
    

file_content += """
    </testbed>
  </testbeds>
</testconf>
"""

f = open("Tarea06 - Permutación de cadenas.xml", 'w');
f.write(file_content)
