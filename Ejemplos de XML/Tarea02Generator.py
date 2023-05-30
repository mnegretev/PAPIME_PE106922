import numpy

years = numpy.random.randint(1600, 2300, 150);
file_content = """
<testconf language="C"> <!-- Soporta solo "C" y "Python" -->
  <build score="2">   <!-- Cuantos puntos solo porque compile. En python esto se ignora -->
    <flags>-lm</flags> <!-- Banderas de compilacion -->
  </build>
  <testbeds>
    <testbed score="8" type="proportional" onerror="halt">  <!-- Tipos: ver comentario de arriba -->
"""
for year in years:
    if (year%4 == 0 and year%100 != 0) or year % 400 == 0:
        file_content +="      \n<testrun args=\"" + str(year) + "\" cout=\"True\" />"
    else:
        file_content +="      \n<testrun args=\"" + str(year) + "\" cout=\"False\" />"

years = numpy.random.randint(0,100, 50)*4 + 1600;
for year in years:
    if (year%4 == 0 and year%100 != 0) or year % 400 == 0:
        file_content +="      \n<testrun args=\"" + str(year) + "\" cout=\"True\" />"
    else:
        file_content +="      \n<testrun args=\"" + str(year) + "\" cout=\"False\" />"


file_content += """
    </testbed>
  </testbeds>
</testconf>
"""

f = open("Tarea02 - Año Bisiesto.xml", 'w');
f.write(file_content)
