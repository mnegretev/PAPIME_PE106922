# -*- coding: utf-8 -*-
# ESTRUCTURA DE DATOS Y ALGORITMOS I
# FACULTAD DE INGENIERÍA, UNAM, 2021-2
# A S S I G N M E N T   2 7
# Instructions:
# Write a program to find the path with the minimum number of subway stations between two geo points in Mexico City. 
# Geographic coordinates of subway stations can be found in the open data site of the Mexico City's government.
# Use the Breadth-First-Search algorithm to find the path.
#
# Modify only the functions marked with the TODO comment. 
# DON'T CHANGE THE 'main' FUNCTION.
# DON'T ADD ANY 'print' FUNCTION.
#

from collections import deque
import requests
import math
import sys
import json
import csv


def breadth_first_search(start, goal, stations, adjacency):
    #
    # TODO:
    #
    # Implement the Breadth-First-Search algorithm to find a path 
    # from the point (start_lat, start_lon) to the point (goal_lat, goal_lon).
    # Return the path as a list of the station names to be traversed.
    # Consider:
    # 'start' is the name of the start station
    # 'goal' is the name of the goal station
    # 'stations' is a list of all stations names: ['Zocalo', 'Allende', 'Bellas Artes' ... ]
    # 'adjacency' is a dictionary where the keys are the station names and each
    # value is a list of the stations the key is connected with. Example:
    # { 'Zocalo'   :[ 'Allende' 'Pino Suarez']
    #   'Chabacano':[ 'Viaducto', 'San Antonio Abad', 'Obrera', 'La Viga', 'Jamaica', 'Lazaron Cardenas'] }
    #
    # You can implement the Breadth-First-Search algorithm with the following steps:
    #
    # - Initialize open_list as an empty list
    # - Initialize closed_list as an empty list.
    # - For all nodes:
    #   - Set g_value to infinity. 
    #   - Set previous nodes to None
    # - Set g_value of start node to zero
    # - Add start node to open_list
    # - Set current_node to start_node
    # - While open_list is not empty and current_node is not the goal node:
    #     - Get the current node by dequeueing a node from the open list
    #       Add current node to the closed list.
    #     - For all adjacent nodes n of current_node:
    #         - if n is in the closed list:
    #             - continue
    #         - Calculate a temporal g_value
    #         - If g_value < g_value of n:
    #              g_value of n = g_value
    #              previous of n = current
    #         - If n is not in the open list and is not in the closed list:
    #             - Add n to open list
    #
    # - While current_node != None:
    #     - Insert current_node to resulting path
    #     - Set current_node to its previous
    # - Add current node to path
    # - Return path
    #
    # Hints:
    # * For storing the g_values, it is suggested to implement a dictionary where the key is the station name
    #   and the corresponding value is the g_value of that station.
    # * For storing the previous nodes, it is suggested to implement a dictionary where the key is the station name
    #   and the corresponding value is the name of the correspoding previous station.
    # * Use 'deque' to implement the open list and the functions 'append' and 'popleft'
    #   to enqueue and dequeue, respectively.

    open_list   = deque()
    closed_list = []
    g_values = {}
    previous = {}
    for n in stations:
        g_values[n] = 99999
        previous[n] = None
    path = []
    open_list.append(start)
    g_values[start] = 0
    current = None
    while current!= goal and len(open_list) > 0:
        current = open_list.popleft()
        closed_list.append(current)
        for n in adjacency[current]:
            if n in closed_list:
                continue
            g = g_values[current] + 1
            if g < g_values[n]:
                g_values[n] = g
                previous[n] = current
            if (n not in open_list) and (n not in closed_list):
                open_list.append(n)
    while current != None:
        path.insert(0, current)
        current = previous[current]
    return path


def get_subway_stations():
    #
    # This function returns a list of tuples of the form [[lat, lon, name], [lat, lon, name], ...]
    # containing the data of all Mexico City subway stations.
    #
    #url="https://datos.cdmx.gob.mx/api/records/1.0/search/?dataset=estaciones-metro&rows=200"
    json_response = open("SubwayStations.json",'r').read()
    json_response = json.loads(json_response)
    stations = []
    for record in json_response['features']:
        lat  = record['geometry']['coordinates'][1]
        lon  = record['geometry']['coordinates'][0]
        name = record['properties']['stop_name']
        try:
            name = name[0:name.index("_")]
        except:
            pass
        stations.append([lat, lon, name])
    return stations

def get_subway_lines():
    #
    # This function returns a list of the form:
    # [ [[lat,lon],[lat,lon],...,[lat,lon]],   [[lat,lon],[lat,lon],...,[lat, lon]], ... , [[lat,lon],[lat,lon],...,[lat,lon]] ]
    #   -------------------------------------   ------------------------------------       -----------------------------------
    #             Stations of line 0                      Stations of line 1                        Stations of line N-1
    # CdMx's subway lines API returns only the coordinates of each station, but not the name.
    # Thus, it is necessary to associate every geopoint with its corresponding name
    # Using the find_neares_station function
    #
    #url="https://datos.cdmx.gob.mx/api/records/1.0/search/?dataset=lineas-de-metro&rows=12"
    #json_response = requests.get(url).json()
    stations_csv = open("SubwayLines.csv",'r')
    csv_reader = csv.reader(stations_csv, delimiter=',')
    line_jsons = []
    for row in csv_reader:
        if row[2][0] != "{":
            continue
        line_jsons.append(json.loads(row[2]))
    lines = []
    for l in line_jsons:
        line_stations = []
        for p in l['coordinates']:
            line_stations.append(p)
        lines.append(line_stations)
    return lines

def build_adjacency(lines, stations):
    #
    # This function returns a dictionary where the keys are the station names and each
    # value is a list of the stations the key is connected with. Example:
    # { 'Zocalo'   :[ 'Allende' 'Pino Suarez']
    #   'Chabacano':[ 'Viaducto', 'San Antonio Abad', 'Obrera', 'La Viga', 'Jamaica', 'Lazaron Cardenas'] }
    # The resulting dictionary represents the adjacency matrix of the CdMx Subway Graph
    #
    A = {}
    for lat,lon,name in stations:
        A[name] = [] 
    for line in lines:
        next = find_nearest_station(line[1][1], line[1][0], stations)
        name = find_nearest_station(line[0][1], line[0][0], stations)
        A[name].append(next)
        for i in range(1, len(line)-1):
            prev = find_nearest_station(line[i-1][1], line[i-1][0], stations)
            next = find_nearest_station(line[i+1][1], line[i+1][0], stations)
            name = find_nearest_station(line[i  ][1], line[i  ][0], stations)
            A[name].append(prev)
            A[name].append(next)
        prev = find_nearest_station(line[len(line)-2][1], line[len(line)-2][0], stations)
        name = find_nearest_station(line[len(line)-1][1], line[len(line)-1][0], stations)
        A[name].append(prev)
    return A

def find_nearest_station(current_lat, current_lon, stations):
    #
    # This function returns the name of the nearest station to the
    # point [current_lat, current_lon], given a list of stations of the form
    # [[lat, lon, name], [lat, lon, name], ...]
    #
    min_d = sys.maxsize
    nearest_station = None
    for [lat, lon, name] in stations:
        d = math.sqrt((current_lon - lon)**2 + (current_lat - lat)**2)
        if d < min_d:
            min_d = d
            nearest_station = name
    return nearest_station

def main(start, goal):
    stations  = get_subway_stations()
    lines     = get_subway_lines()
    adjacency = build_adjacency(lines, stations)
    path      = breadth_first_search(start, goal, [name for [lat, lon, name] in stations], adjacency)
    print("The best path is:")
    for p in path:
        print(p)

if __name__ == '__main__':
    start = None
    goal  = None
    start_lat = None
    start_lon = None
    goal_lat  = None
    goal_lon  = None
    stations  = get_subway_stations()
    names     = [name for [lat, lon, name] in stations]

    if '--start' in sys.argv:
        start = sys.argv[sys.argv.index('--start')+1]
    if '--goal' in sys.argv:
        goal = sys.argv[sys.argv.index('--goal')+1]
    
    if '--start_lat' in sys.argv:
        start_lat = float(sys.argv[sys.argv.index('--start_lat')+1])
    if '--start_lon' in sys.argv:
        start_lon = float(sys.argv[sys.argv.index('--start_lon')+1])
    if '--goal_lat' in sys.argv:
        goal_lat = float(sys.argv[sys.argv.index('--goal_lat')+1])
    if '--goal_lon' in sys.argv:
        goal_lon = float(sys.argv[sys.argv.index('--goal_lon')+1])
    
    if start_lat != None and start_lon != None:
        start = find_nearest_station(start_lat, start_lon, stations)
    if goal_lat != None and goal_lon != None:
        goal  = find_nearest_station(goal_lat,  goal_lon , stations)
    
    if start == None:
        start = input('Enter the start station:  ')
    if goal  == None:
        goal  = input('Enter the goal station: ')

    if start not in names:
        print("Invalid start station")
        exit()
    if goal not in names:
        print("Invalid goal station")
        exit()
    main(start, goal)
