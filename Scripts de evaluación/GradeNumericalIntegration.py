#coding=utf-8
import sys
import numpy
import math
import subprocess

"""
/*
 * FUNCTION POINTERS FOR NUMERICAL INTEGRATION
 *
 * Instructions:
 * Write the code to implement a numerical integrator using the trapezoidal rule. 
 * The integrator must be implemented using function pointers, such that it can calculate
 * the definite integral of any real function (satisfying integrability conditions).
 * MODIFY ONLY THOSE SECTIONS MARKED WITH THE 'TODO' COMMENT
 * DON'T MODIFY THE MAIN FUNCTION.
 * DON'T ADD ANY 'printf' FUNCTION.
 */
"""

def generate_program_input():
    functions = ['sin','cos','tan','sinh','cosh','tanh','asin','acos','atan','exp','log','sqrt']
    f = numpy.random.choice(functions)
    if f in ['sin','cos','sinh','cosh','tanh','atan','exp']:
        lower = numpy.random.uniform(-3.1415, -0.5)
        upper = numpy.random.uniform(0.5, 3.1415)
    elif f in ['tan','asin','acos']:
        lower = numpy.random.uniform(-0.9, -0.5)
        upper = numpy.random.uniform(0.5, 0.9)
    else:
        lower = numpy.random.uniform(0.5, 1.0)
        upper = numpy.random.uniform(2.0, 3.1415)
    step = numpy.random.choice(['0.0001','0.0002','0.0003'])
    return [f, str(lower), str(upper), step]

def evaluate(program_input, program_output):
    functions = {'sin':math.sin,'cos':math.cos,'tan':math.tan,'sinh':math.sinh,'cosh':math.cosh,'tanh':math.tanh,'asin':math.asin,'acos':math.acos,'atan':math.atan,'exp':math.exp,'log':math.log,'sqrt':math.sqrt}
    try:
        program_output = float(program_output.strip())
    except:
        program_output = float("inf")
        pass
    lower = float(program_input[1])
    upper = float(program_input[2])
    step  = float(program_input[3])
    expected = 0
    x = lower
    while x < upper:
        expected += step*(functions[program_input[0]](x) + functions[program_input[0]](x+step))/2.0
        x += step
    return abs(expected - program_output) < step*100, str(expected)
    

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
