#coding=utf-8
import sys
import numpy
import subprocess
import requests

"""
# AIR QUALITY
#
# Instructions:
# Write a program to check the air quality index according to the
# data provided by the CDMX government
# The program already has a function that get air quality data using
# the API provided by the CDMX government. Specifications and usage of API can be found in:
# https://datos.cdmx.gob.mx/explore/dataset/prueba_datos_calidad_aire/api/
# DON'T ADD ANY PRINT FUNCTION
# ONLY MODIFY THE SECTIONS MARKED WITH THE TODO COMMENT
"""

print("Getting air quality data from CDMX API")
url="https://datos.cdmx.gob.mx/api/records/1.0/search/?dataset=prueba_datos_calidad_aire&rows=50"
air_data = ""#requests.get(url).json()

def generate_program_input():
    correct = False
    i = -1
    while not correct:
        i = numpy.random.randint(0, len(air_data['records']))
        r = air_data['records'][i]['fields']
        try:
            recommendations = [r['recomendacion_uno'], r['recomendacion_dos'], r['recomendacion_tres']]
            correct = True
        except:
            pass
    return [air_data['records'][i]['fields']['alcaldia_municipio']]

def evaluate(program_input, program_output):
    program_output = program_output.strip().replace("\n","")
    expected = ''
    for r in air_data['records']:
        if r['fields']['alcaldia_municipio'] == program_input[0]:
            expected += 'Calidad del aire:\n' + r['fields']['indice'] + "\nRecomendaciones:\n"
            if r['fields']['indice'] != 'SIN COBERTURA':
                expected += r['fields']['recomendacion_uno'] +"\n"+ r['fields']['recomendacion_dos']+"\n"+ r['fields']['recomendacion_tres']
                
    return expected.replace('\n','') == program_output, expected
    

if __name__ == '__main__':
    assignment_file = sys.argv[1]
    program_input = generate_program_input()
    sp = subprocess.Popen(["python3", assignment_file] + program_input, stdout=subprocess.PIPE)
    (program_output, program_error) = sp.communicate()
    program_output = program_output.decode('utf8')
    result, expected_output = evaluate(program_input, program_output)
    if result:
        print("Correct result with the following values:")
    else:
        print("The program failed with the following values:")
    print("Program input:   " + str(program_input))
    print("Expected value:" + str(expected_output))
    print("Program output:" + program_output      )
