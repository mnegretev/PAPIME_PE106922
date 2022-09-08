#coding=utf-8
import sys
import numpy
import subprocess
import math

"""
/*
 * ROTATION AND TRANSLATION OF 2D POLYGONS
 *
 * Instructions:
 * Write the code to initialize, rotate and translate a polygon with 'n' vertices. 
 * 
 * MODIFY ONLY THOSE SECTIONS MARKED WITH THE 'TODO' COMMENT
 * DON'T MODIFY THE MAIN FUNCTION.
 * DON'T ADD ANY 'printf' FUNCTION.
 */
"""

def generate_program_input():
    dx = str(round(numpy.random.uniform(-10,10),4))
    dy = str(round(numpy.random.uniform(-10,10),4))
    r  = str(round(numpy.random.uniform( -3, 3),4))
    return [dx, dy, r]

def evaluate(program_input, program_output):
    dx = float(program_input[0])
    dy = float(program_input[1])
    r  = float(program_input[2])
    lines = program_output.split()
    data = []
    for i in range(len(lines)):
        try:
            x = float(lines[i])
            data.append(x)
        except:
            pass
    if len(data) < 12: #The minimum number of vertices is 3
        return False, "Invalid program output"
    try:
        original_vertices = numpy.array(data[0:int(len(data)/2)])
        output_vertices   = numpy.array(data[int(len(data)/2):int(len(data))])
        original_vertices = numpy.reshape(original_vertices, [int(len(original_vertices)/2), 2])
        output_vertices   = numpy.reshape(output_vertices  , [int(len(output_vertices)/2)  , 2])
    except:
        return False, "Invalid number of data"

    transformed_vertices = numpy.copy(original_vertices)
    expected = "Transformed polygon:\n"
    for i in range(len(original_vertices)):
        x = original_vertices[i][0]*math.cos(r) - original_vertices[i][1]*math.sin(r) + dx
        y = original_vertices[i][0]*math.sin(r) + original_vertices[i][1]*math.cos(r) + dy
        transformed_vertices[i][0] = x
        transformed_vertices[i][1] = y
        expected += "%+0.4f  %+0.4f\n"%(x,y)
    try:
        m1 = numpy.array(transformed_vertices)
        m2 = numpy.array(output_vertices)
        difference = numpy.linalg.norm(numpy.subtract(m1, m2))
    except:
        return False, expected
        
    return difference < 0.01, expected
    

if __name__ == '__main__':
    assignment_file = sys.argv[1]
    program_input = generate_program_input_A08()
    subprocess.call(["gcc", assignment_file, "-w", "-o", "/dev/shm/a.out", "-lm"])
    sp = subprocess.Popen(['/dev/shm/a.out'] + program_input, stdout=subprocess.PIPE)
    (program_output, program_error) = sp.communicate()
    result, expected_output = evaluate_A08(program_input, program_output)
    if result:
        print("Correct result with the following values:")
    else:
        print("The program failed with the following values:")
    print("Program input:   " + str(program_input))
    print("Expected value:\n" + str(expected_output))
    print("Program output:\n" + program_output      )
