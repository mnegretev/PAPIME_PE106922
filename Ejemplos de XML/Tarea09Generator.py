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

test_strings = open("TestStrings.txt", 'r').readlines()
test_strings = [x.strip() for x in test_strings]

def is_one_edit_replace(s1, s2):
    found_difference = False
    a1 = list(s1)
    a2 = list(s2)
    for i in range(len(a1)):
        if a1[i] != a2[i]:
            if found_difference:
                return False
            found_difference = True
    return found_difference

def is_one_edit_insert(s1, s2):
    found_difference = False
    a1 = list(s1)
    a2 = list(s2)
    len1 = len(a1)
    len2 = len(a2)
    idx1 = 0
    idx2 = 0
    while idx1 < len1 and idx2 < len2:
        if a1[idx1] != a2[idx2]:
            if found_difference:
                return False
            found_difference = True
            idx2 += 1
        else:
            idx1 += 1
            idx2 += 1
    return True

def get_expected_value(s1,s2):
    a1 = list(s1)
    a2 = list(s2)
    len1 = len(a1)
    len2 = len(a2)
    if len1 == len2:
        return is_one_edit_replace(s1, s2)
    elif len1+1 == len2:
        return is_one_edit_insert(s1, s2)
    elif len1-1 == len2:
        return is_one_edit_insert(s2, s1)
    else:
        return False

def replace_char(s):
    a = list(s)
    idx = numpy.random.randint(0, len(a)-1)
    a[idx] = 'x'
    return "".join(a)

def insert_char(s):
    a = list(s)
    idx = numpy.random.randint(0, len(a)-1)
    a.insert(idx, 'x')
    return "".join(a)

def remove_char(s):
    a = list(s)
    idx = numpy.random.randint(0, len(a)-1)
    a.pop(idx)
    return "".join(a)

def generate_program_input():
    str_test1 = numpy.random.choice(test_strings).strip()
    rndchoice = numpy.random.randint(0,3)
    if  rndchoice == 0:
        str_test2 = numpy.random.choice(test_strings).strip()
    elif rndchoice == 1:
        str_test2 = replace_char(str_test1)
    elif rndchoice == 2:
        str_test2 = insert_char(str_test1)
    else:
        str_test2 = remove_char(str_test1)
    return [str_test1, str_test2]

def get_target_values():
    s1, s2 = generate_program_input();
    expected = "True" if get_expected_value(s1, s2) else "False"
    return "'" + s1 + "' '" + s2 + "'", expected


for i in range(200):
    args_str, expected_output = get_target_values()
    file_content +="      \n<testrun args=\"" + args_str + "\" cout=\"" + expected_output  + "\" />"
    

file_content += """
    </testbed>
  </testbeds>
</testconf>
"""

f = open("Tarea09 - Cadenas de una edición.xml", 'w');
f.write(file_content)
