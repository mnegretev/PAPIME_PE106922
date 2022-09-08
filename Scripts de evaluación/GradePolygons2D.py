#coding=utf-8
import sys
import numpy
import os
import subprocess
import math
from datetime import datetime

"""
/*
 * ROTATION AND TRANSLATION OF POLYGONS
 *
 * Instructions:
 * Write a program to calculate the coordinates XY of the set of vertices of a regular polygon
 * when the number of vertices 'n', the apotheme, the center coordinates and the angle of rotation are given.
 *
 * The program receives as command line arguments the number of vertices, apotheme and center. 
 * ONLY MODIFY THE SECTIONS MARKED WITH THE 'TODO' COMMENT.
 * DON'T MODIFY THE MAIN FUNCTION.
 * DON'T ADD ANY 'printf' FUNCTION.
 */
"""
def generate_program_input():
    n  = str(numpy.random.randint(3,10))
    a  = str(round(numpy.random.uniform(  1,10),4))
    cx = str(round(numpy.random.uniform(-10,10),4))
    cy = str(round(numpy.random.uniform(-10,10),4))
    r  = str(round(numpy.random.uniform( -3, 3),4))
    return [n, a, cx, cy, r]

def evaluate(program_input, program_output):
    program_output = program_output.strip().split('\n')
    n  =   int(program_input[0])
    a  = float(program_input[1])
    cx = float(program_input[2])
    cy = float(program_input[3])
    r  = float(program_input[4])
    expected_vertices = []
    expected = ""
    d = a/math.cos(math.pi/n)
    for i in range(n):
        t = i*2*math.pi/n
        expected_vertices.append([round(d*math.cos(t+r) + cx, 4), round(d*math.sin(t+r) + cy, 4)])
        expected += "%+0.4f  %+0.4f\n"%(expected_vertices[i][0], expected_vertices[i][1])

    output_vertices = []
    for i in range(len(program_output)):
        xy = program_output[i].split()
        try:
            x = float(xy[0])
            y = float(xy[1])
            output_vertices.append([x,y])
        except:
            return False, expected
    difference = 0
    try:
        m1 = numpy.array(expected_vertices)
        m2 = numpy.array(output_vertices)
        difference = numpy.linalg.norm(numpy.subtract(m1, m2))
    except:
        return False, expected
        
    return difference < 0.01, expected


if __name__ == '__main__':
    assignment_file = sys.argv[1]
    program_input = generate_program_input()
    subprocess.call(["gcc", assignment_file, "-w", "-o", "/dev/shm/a.out", "-lm"])
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
