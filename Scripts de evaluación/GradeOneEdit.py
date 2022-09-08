#coding=utf-8
import sys
import numpy
import subprocess

"""
/*
 * ONE EDIT STRINGS
 *
 * Instructions:
 * Write a program to determine if a string is one-edit away from another string..
 * A string S1 is said to be a one-edit of another string S2 if ONLY ONE of the following conditions is held:
 * a) S1 is obtained from S2 by chaging one character
 * b) S1 is obtained from S2 by deleting one character
 * c) S1 is obtained from S2 by inserting one character
 * Examples:
 * bear -> beer  = true
 * bear -> bar   = true
 * bear -> beard = true
 * bear -> ber   = false
 * The program must receive as command line arguments the two strings two be analized.
 * The output of the program must be 1, if S1 is one-edit away of S2, and 0, otherwise.
 * THE USE OF EXTRA LIBRARIES IS NOT ALLOWED
 * MODIFY ONLY THE INDICATED FUNCTIONS
 */
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

def evaluate(program_input, program_output):
    expected = 1 if get_expected_value(program_input[0], program_input[1]) else 0
    try:
        program_output = int(program_output.strip())
        return program_output == expected, str(expected)
    except:
        return False, str(expected)


if __name__ == '__main__':
    assignment_file = sys.argv[1]
    program_input = generate_program_input()
    subprocess.call(["gcc", assignment_file, "-I", ".", "-w", "-o", "/dev/shm/a.out"])
    sp = subprocess.Popen(['/dev/shm/a.out'] + program_input, stdout=subprocess.PIPE)
    (program_output, program_error) = sp.communicate()
    result, expected_output = evaluate(program_input, program_output)
    if result:
        print("Correct result with the following values:")
    else:
        print("The program failed with the following values:")
    print("Program input:   " + str(program_input))
    print("Expected value:\n" + str(expected_output))
    print("Program output:\n" + program_output.decode("utf-8"))
