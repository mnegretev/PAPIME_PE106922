#coding=utf-8
import sys
import numpy
import subprocess

"""
/*
 * MATRIX TRANSPOSE
 *
 * Instructions:
 * Calculate the transpose of a matrix using ONLY ONE-DIMENSIONAL ARRAYS, i.e., 
 * you CANNOT USE the double bracket [][] notation.
 * The program receives the matrix order as command line parameters, e.g:
 * ./Prac_01 3 5 indicates a 3x5 matrix.
 * The program must fill the matrix with random integers in the interval [-99,99].
 * The program must print both the original and the transposed matrix.
 * ONLY MODIFY THE SECTIONS MARKED WITH THE 'TODO' COMMENT
 * DON'T ADD ANY 'printf' FUNCTION.
 */
"""

def generate_program_input():
    return [str(numpy.random.randint(1,10)), str(numpy.random.randint(1,10))]

def evaluate(program_input, program_output):
    rows = int(program_input[0])
    cols = int(program_input[1])
    lines = program_output.split()
    data = []
    for i in range(len(lines)):
        try:
            x = int(lines[i])
            data.append(x)
        except:
            pass
    try:
        original_matrix   = numpy.array(data[0:int(len(data)//2)])
        transposed_matrix = numpy.array(data[int(len(data)//2):int(len(data))])
        original_matrix   = numpy.reshape(original_matrix  , [rows, cols])
        transposed_matrix = numpy.reshape(transposed_matrix, [cols, rows])
        expected_matrix   = original_matrix.transpose()
    except Exception:
        print (Exception)
        return False, "Invalid program output"
    expected_output = "The original matrix is:\n"
    for i in range(len(original_matrix)):
        for j in range(len(original_matrix[0])):
            expected_output += str(original_matrix[i][j])+'\t'
        expected_output += '\n'
    expected_output += "The transposed matrix is:\n"
    for i in range(len(expected_matrix)):
        for j in range(len(expected_matrix[0])):
            expected_output += str(expected_matrix[i][j])+'\t'
        expected_output += '\n'
    return numpy.array_equal(original_matrix.transpose(), transposed_matrix), expected_output
    

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
