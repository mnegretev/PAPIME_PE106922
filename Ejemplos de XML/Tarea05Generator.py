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



for i in range(60):
    n1 = numpy.random.randint(len(test_strings))
    n2 = numpy.random.randint(len(test_strings))
    s1, s2 = test_strings[n1], test_strings[n2]
    a1 = list(s1)
    a2 = list(s2)
    a1.append('\0')
    a2.append('\0')
    i = 0;
    while a1[i] == a2[i] and a1[i] != '\0':
        i+=1
    expected_output =str(ord(a1[i]) - ord(a2[i]))
    args_str =  "'" + s1 + "' '" + s2 + "'"
    file_content +="      \n<testrun args=\"" + args_str + "\" cout=\"" + expected_output  + "\" />"
    

file_content += """
    </testbed>
  </testbeds>
</testconf>
"""

f = open("Tarea05 - Comparación lexicográfica.xml", 'w');
f.write(file_content)
