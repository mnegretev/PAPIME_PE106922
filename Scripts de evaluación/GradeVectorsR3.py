#coding=utf-8
import sys
import math
import numpy
import subprocess

"""
/*
 * OPERATIONS WITH VECTORS IN R3
 *
 * Instructions:
 * Write a program to implement the addition, substraction, cross product,
 * dot product, norm2, unitary vector and angle between vectors in R3.
 * The program receives as command line arguments the operation code followed
 * by the components of the vectors to operate.
 * Operation codes are 'add', 'sub', 'cross', 'dot', 'mag', 'unit' and 'ang'
 * Example: the command
 *     ./Assignment07 cross 1 0 0  0 1 0
 * should print the output
 *     0.00000,0.00000,1.00000
 * MODIFY ONLY THOSE FUNCTIONS MARKED WITH THE 'TODO' COMMENT
 * DON'T MODIFY THE MAIN FUNCTION.
 * DON'T ADD ANY 'printf' FUNCTION.
 */
"""

def generate_program_input():
    op = numpy.random.choice(['add', 'sub', 'cross', 'dot', 'mag', 'unit', 'ang'])
    v1 = [round(numpy.random.uniform(-10, 10),2), round(numpy.random.uniform(-10, 10),2), round(numpy.random.uniform(-10, 10),2)]
    v2 = [round(numpy.random.uniform(-10, 10),2), round(numpy.random.uniform(-10, 10),2), round(numpy.random.uniform(-10, 10),2)]
    return [op, str(v1[0]), str(v1[1]), str(v1[2]), str(v2[0]), str(v2[1]), str(v2[2])]

def evaluate(program_input, program_output):
    op = program_input[0]
    v1 = [float(program_input[1]), float(program_input[2]), float(program_input[3])]
    v2 = [float(program_input[4]), float(program_input[5]), float(program_input[6])]
    if op == "add":
        expected = [v1[0]+v2[0], v1[1]+v2[1], v1[2]+v2[2]]
    elif op == "sub":
        expected = [v1[0]-v2[0], v1[1]-v2[1], v1[2]-v2[2]]
    elif op == "dot":
        expected = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]
    elif op == "cross":
        ax = v1[0]
        ay = v1[1]
        az = v1[2]
        bx = v2[0]
        by = v2[1]
        bz = v2[2]
        vx =  ay*bz - by*az
        vy = -ax*bz + bx*az
        vz =  ax*by - bx*ay
        expected = [vx, vy, vz]
    elif op == "mag":
        expected = math.sqrt(v1[0]*v1[0] + v1[1]*v1[1] + v1[2]*v1[2])
    elif op == "unit":
        mag = math.sqrt(v1[0]*v1[0] + v1[1]*v1[1] + v1[2]*v1[2])
        if mag == 0:
            expected = [0,0,0]
        else:
            expected = [v1[0]/mag, v1[1]/mag, v1[2]/mag]
    elif op == "ang":
        mag1 = math.sqrt(v1[0]*v1[0] + v1[1]*v1[1] + v1[2]*v1[2])
        mag2 = math.sqrt(v2[0]*v2[0] + v2[1]*v2[1] + v2[2]*v2[2])
        if mag1 == 0 or mag2 == 0:
            expected = 0
        else:
            expected = math.acos((v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2])/(mag1*mag2))
    else:
        expected = 0
    try:
        expected = [round(expected[0],6), round(expected[1],6), round(expected[2],6)]
    except:
        expected = round(expected, 6)

    components = program_output.split(',')
    if len(components) == 1:
        try:
            v = float(components[0])
        except:
            return False, str(expected)
    elif len(components) == 3:
        try:
            v = [float(components[0]), float(components[1]), float(components[2])]
        except:
            return False, str(expected)
    else:
        return False, str(expected)

    try:
        comparisson = [v[0] - expected[0], v[1] - expected[1], v[2] - expected[2]]
    except:
        try:
            comparisson = v - expected
        except:
            return False, str(expected)

    return numpy.linalg.norm(comparisson) < 0.001, str(expected)

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
