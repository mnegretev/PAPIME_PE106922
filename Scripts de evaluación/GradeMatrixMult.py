#coding=utf-8
import sys
import numpy
import subprocess

"""
/*
 * MATRIX MULTIPLICATION
 *
 * Instructions:
 * Multiply three matrices whose orders are given by a0Xa1, a1Xa2, a2Xa3
 * The three matrices must be filled with random integers in [0,99]
 * The program must print the three generated matrices and the result of the product.
 * Values a0, a1, a2 and a3 are passed as command line arguments.
 *
 * IT IS MANDATORY TO USE THE 'malloc' FUNCTION TO ALLOCATE ALL THE SPACE NEEDED
 * TO STORE THE MATRICES ELEMENTS.
 * THE USE OF THE BRACKET NOTATION [] IS NOT ALLOWED. STUDENTS MUST USE POINTERS INSTEAD.
 * MODIFY ONLY THE SECTIONS MARKED WITH THE 'TODO' COMMENT.
 * DON'T MODIFY THE MAIN FUNCTION.
 * DON'T ADD ANY 'printf' FUNCTION.
 */
"""

def generate_program_input():
    a1 = str(numpy.random.randint(1,5))
    a2 = str(numpy.random.randint(1,5))
    a3 = str(numpy.random.randint(1,5))
    a4 = str(numpy.random.randint(1,5))
    return [a1, a2, a3, a4]

def evaluate(program_input, program_output):
    a0 = int(program_input[0])
    a1 = int(program_input[1])
    a2 = int(program_input[2])
    a3 = int(program_input[3])
    lines = program_output.split()
    data = []
    for i in range(len(lines)):
        try:
            x = int(lines[i])
            data.append(x)
        except:
            pass
    try:
        idx  = 0;
        m1 = numpy.array(data[idx : idx + a0*a1])
        idx += a0*a1
        m2 = numpy.array(data[idx : idx + a1*a2])
        idx += a1*a2
        m3 = numpy.array(data[idx : idx + a2*a3])
        idx += a2*a3
        program_result = numpy.array(data[idx : len(data)])
        m1 = numpy.reshape(m1, [a0,a1])
        m2 = numpy.reshape(m2, [a1,a2])
        m3 = numpy.reshape(m3, [a2,a3])
        program_result  = numpy.reshape(program_result, [a0,a3])
        expected_matrix = numpy.matmul(numpy.matmul(m1, m2), m3)
    except:
        return False, "Invalid program output"
                         
    expected_output  = "Matrix one   is:\n"
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            expected_output += str(m1[i][j])+'\t'
        expected_output += '\n'
    expected_output += "Matrix two   is:\n"
    for i in range(len(m2)):
        for j in range(len(m2[0])):
            expected_output += str(m2[i][j])+'\t'
        expected_output += '\n'
    expected_output += "Matrix three is:\n"
    for i in range(len(m3)):
        for j in range(len(m3[0])):
            expected_output += str(m3[i][j])+'\t'
        expected_output += '\n'
    expected_output += "Resulting matrix is:\n"
    for i in range(len(expected_matrix)):
        for j in range(len(expected_matrix[0])):
            expected_output += str(expected_matrix[i][j])+'\t'
        expected_output += '\n'
    
    return numpy.array_equal(program_result, expected_matrix), expected_output
    

if __name__ == '__main__':
    assignment_file = sys.argv[1]
    program_input = generate_program_input()
    subprocess.call(["gcc", assignment_file, "-w", "-o", "/dev/shm/a.out"])
    sp = subprocess.Popen(['/dev/shm/a.out'] + program_input, stdout=subprocess.PIPE)
    (program_output, program_error) = sp.communicate()
    result, expected_output = evaluate(program_input, program_output)
    if result:
        print("Correct result with the following values:")
    else:
        print("The program failed with the following values:")
    print("Program input:   " + str(program_input))
    print("Expected value:\n" + str(expected_output))
    print("Program output:\n" + program_output      )
