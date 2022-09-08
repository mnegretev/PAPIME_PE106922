# -*- coding: utf-8 -*-
import sys
import os
import numpy
import subprocess
import json
import math

"""
# NEAREST SUBWAY STATION
#
# Instructions:
# Write a program to find the nearest subway station given a current location in latitude and longitude.
# Geographic coordinates of subway stations are defined in the file 'SubwayStations.json'
# Modify only the functions marked with the TODO comment. 
# DON'T CHANGE THE 'main' FUNCTION.
# DON'T ADD ANY 'print' FUNCTION.
"""

def get_subway_stations(json_file):
    json_data = json.loads(open(json_file, 'r').read())
    #
    # TODO:
    # Return a list of tuples of the form [[lat, lon, name], [lat, lon, name], ...]
    # containing the data of all Mexico City subway stations.
    # Variable 'json_data' is a dictionary with the data about subway stations.
    # See online documentation to check data format
    # https://datos.cdmx.gob.mx/dataset/lineas-y-estaciones-del-metro/resource/0869e0dd-6876-4446-a199-8f670a359c00
    #
    stations = []
    for record in json_data['records']:
        latlon  = record[2].split(",")
        lat,lon = float(latlon[0]), float(latlon[1])
        name = record[4]
        stations.append([lat, lon, name])
    return stations

print("Getting subway stations from file...")
stations = get_subway_stations('SubwayStations.json')
os.system("cp SubwayStations.json /dev/shm/SubwayStations.json")

def find_nearest_station(current_lat, current_lon, stations):
    #
    # TODO:
    # Find the nearest subway station given a current latitude and longitude (current_lat, current_lon)
    # and the list of all stations (see get_subway_stations() function).
    # Return a tuple of the form [lat, lon, name] with the nearest station data.
    #
    min_d = sys.maxsize
    nearest_station = None
    for [lat, lon, name] in stations:
        d = math.sqrt((current_lon - lon)**2 + (current_lat - lat)**2)
        if d < min_d:
            min_d = d
            nearest_station = [lat, lon, name]
    return nearest_station            

def generate_program_input():
    lat = round(numpy.random.uniform( 19.327111,  19.474453),6)
    lon = round(numpy.random.uniform(-99.043181, -99.183771),6)
    return ['--lat',str(lat), '--lon', str(lon), '--json', '/dev/shm/SubwayStations.json', '--grading']

def evaluate(program_input, program_output):
    program_output = program_output.strip().replace("\n","").split(",")
    try:
        [output_name, output_lat, output_lon]    = [program_output[0], float(program_output[1]), float(program_output[2])]
    except:
        [output_name, output_lat, output_lon]    = ["",0,0]
    [correct_lat, correct_lon, correct_name] = find_nearest_station(float(program_input[1]), float(program_input[3]), stations)
    correct = output_name == correct_name and abs(output_lat - correct_lat)<0.000001 and abs(output_lon - correct_lon)<0.000001
    expected = "%s,%f,%f"%(correct_name, correct_lat, correct_lon)
    return correct, expected
    

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
