# -*- coding: utf-8 -*-
# DATA STRUCTURES AND ALGORITHMS I
# FI-UNAM-2022-2
# P R A C T I C E   0 2
# INTRODUCTION TO PYTHON - POSITIONS OF PLANETS
#
# Instructions:
# Complete the code to calculate the right ascension, declination, azimuth and
# elevation of the Sun, Moon, Mercury, Venus, Mars, Jupiter and Saturn, for a given date and time.
# Declination and Azimuth should be calculated for an observer located in Mexico City.
#
# Modify only the functions marked with the TODO comment. 
# DON'T ADD ANY 'print' FUNCTION.
#
# This work was supported by UNAM-DGAPA under grant PAPIME PE106922
#


import sys
import datetime
import math

#
# ORBITAL PARAMETERS
#
planet_params = {}
planet_params['sun']     = {'N':[0,0],
                            'i':[0,0]}
planet_params['moon']    = {}
planet_params['mercury'] = {}
planet_params['venus']   = {}
planet_params['mars']    = {}
planet_params['jupiter'] = {}
planet_params['saturn']  = {}

planet_params['moon'] = {
    'N' : [125.1228, - 0.0529538083 ], 
    'i' : [5.1454  , + 0.0          ],
    'w' : [318.0634, + 0.1643573223 ],
    'a' : 60.2666                   ,
    'e' : [0.054900, + 0.0          ],
    'M' : [115.3654, + 13.0649929509] 
    }

planet_params['mercury'] = {
    'N' : [48.3313 , + 3.24587E-5  ],
    'i' : [7.0047  , + 5.00E-8     ],
    'w' : [29.1241 , + 1.01444E-5  ],
    'a' : 0.3870980                 ,
    'e' : [0.205635, + 5.59E-10    ],
    'M' : [168.6562, + 4.0923344368]  
    }

planet_params['venus'] = {
    'N' : [76.6799 , + 2.46590E-5   ],
    'i' : [3.3946  , + 2.75E-8      ],
    'w' : [54.8910 , + 1.38374E-5   ],
    'a' : 0.7233300                  ,
    'e' : [0.006773, - 1.302E-9     ],
    'M' : [48.0052 , + 1.6021302244 ] 
    }

planet_params['earth'] = {
    'N' : [0.0     , + 0.0         ],
    'i' : [0.0     , + 0.0         ],
    'w' : [102.9404, 4.70935E-5    ],
    'a' : 1.000000                  ,
    'e' : [0.016709, - 1.151E-9    ],
    'M' : [356.0470, + 0.9856002585] 
    }

planet_params['mars'] = {
    'N' : [49.5574 , + 2.11081E-5  ],
    'i' : [1.8497  , - 1.78E-8     ],
    'w' : [286.5016, + 2.92961E-5  ],
    'a' : 1.523688                  ,
    'e' : [0.093405, + 2.516E-9    ],
    'M' : [18.6021 , + 0.5240207766] 
    }

planet_params['jupiter'] = {
    'N' : [100.4542, + 2.76854E-5  ],
    'i' : [1.3030  , - 1.557E-7    ],
    'w' : [273.8777, + 1.64505E-5  ],
    'a' : 5.20256                   ,
    'e' : [0.048498, + 4.469E-9    ],
    'M' : [19.8950 , + 0.0830853001] 
    }

planet_params['saturn'] = {
    'N' : [113.6634, + 2.38980E-5  ],
    'i' : [2.4886  , - 1.081E-7    ],
    'w' : [339.3939, + 2.97661E-5  ],
    'a' : 9.55475                   ,
    'e' : [0.055546, - 9.499E-9    ],
    'M' : [316.9670, + 0.0334442282] 
    }

def timestamp_to_ellapsed_days(timestamp):
    #
    # TODO:
    # Get the elapsed days for the given timestamp, since Dec 31, 1999, 00:00:00 GMT.
    # Use an online tool to obtain the time stamp 't0' for Dec 31, 1999, 00:00:00 GMT
    # Substract t0 from timestamp and divide by 86400 (number of seconds in a day)
    #
    return 0

def get_orbital_params(planet, d):
    p = planet_params[planet]
    N =  (p['N'][0] + p['N'][1] * d)*math.pi/180
    i =  (p['i'][0] + p['i'][1] * d)*math.pi/180
    w =  (p['w'][0] + p['w'][1] * d)*math.pi/180
    a =   p['a']
    e =   p['e'][0] + p['e'][1] * d
    M = ((p['M'][0] + p['M'][1] * d)%360)*math.pi/180
    return [N, i, w, a, e, M]

def calculate_eccentric_anomaly(M,e):
    #
    # TODO:
    # Given a Mean Anomaly 'M' and eccentricity 'e'
    # Calculate the the Eccentric Anomaly 'E'
    # Use Newton-Raphson to solve the equation:
    # E - e sinE - M = 0
    #
    
    return 0

def calculate_true_anomaly(E, e, a):
    #
    # TODO
    # Calculate the true Anomaly 'v', given an eccentric anomaly 'E',
    # an eccentricity 'e' and a semi-major axis 'a'.
    #
    return [0,0]

def rotate_on_z(x, y, z, theta):
    xr = x*math.cos(theta) - y*math.sin(theta)
    yr = x*math.sin(theta) + y*math.cos(theta)
    zr = z
    return [xr, yr, zr]

def rotate_on_y(x, y, z, theta):
    xr =  x*math.cos(theta) + z*math.sin(theta)
    yr =  y
    zr = -x*math.sin(theta) + z*math.cos(theta)
    return [xr, yr, zr]

def rotate_on_x(x, y, z, theta):
    xr = x
    yr = y*math.cos(theta) - z*math.sin(theta)
    zr = y*math.sin(theta) + z*math.cos(theta)
    return [xr, yr, zr]

def calculate_ecliptic_xyz(r, N, w, v, i):
    #
    # TODO:
    # Calculate coordinates XYZ w.r.t. ecliptic system, given a
    # true anomaly 'v', a radius 'r', and the orbital parameters 'w', 'N', and 'i'.
    #
    return [0,0,0]

def calculate_equatorial_coords(xeclip, yeclip, zeclip):
    #
    # TODO:
    # Given XYZ in ecliptic coordinates, calculate the Right Ascension and Declination.
    #
    return [0, 0]

def get_sideral_local_time(M_sun, w_sun, lon, timestamp):
    secs = timestamp % 86400
    return  M_sun + w_sun + lon + secs*2*math.pi/86400

def rad_to_HMS(a):
    #
    # TODO:
    # Given an angle 'a' in radians, return
    # the angle in hh:mm:ss format.
    #
    
    return "%02d:%02d:%02f"%(0,0,0)

def get_azimuth_elevation(RA, Dec, LST, lat):
    HA = LST - RA
    x = math.cos(HA) * math.cos(Dec)
    y = math.sin(HA) * math.cos(Dec)
    z = math.sin(Dec)
    [xhor, yhor, zhor] = rotate_on_y(x,y,z, -(math.pi/2-lat))
    azimuth  = math.atan2( yhor, xhor ) + math.pi
    altitude = math.atan2( zhor, math.sqrt(xhor*xhor+yhor*yhor) )
    return [azimuth, altitude]

def rad_to_DMS(a):
    #
    # TODO:
    # Given an angle 'a' in radians, return
    # the angle in dd°mm'ss'' format.
    #
    return "%02d°%02d'%02f"%(0,0,0)

def get_sun_position(lon, lat, timestamp):
    d = timestamp_to_ellapsed_days(timestamp)
    [N,i,w,a,e,M] = get_orbital_params('earth', d)
    E = calculate_eccentric_anomaly(M,e)
    [v,r] = calculate_true_anomaly(E, e, a)
    [xeclip, yeclip, zeclip] = calculate_ecliptic_xyz(r, N, w, v, i)
    [RA, Dec] = calculate_equatorial_coords(-xeclip, -yeclip, -zeclip)
    LST = get_sideral_local_time(M, w, lon, timestamp)
    [Az,delta] = get_azimuth_elevation(RA, Dec, LST, lat)
    return [RA, Dec, Az, delta]


def get_moon_position(lon, lat, timestamp):
    d = timestamp_to_ellapsed_days(timestamp)
    [N,i,w_earth,a,e,M_earth] = get_orbital_params('earth', d)
    [N,i,w,a,e,M] = get_orbital_params('moon', d)
    E = calculate_eccentric_anomaly(M,e)
    [v,r] = calculate_true_anomaly(E, e, a)
    [xeclip, yeclip, zeclip] = calculate_ecliptic_xyz(r, N, w, v, i)
    [RA, Dec] = calculate_equatorial_coords(xeclip, yeclip, zeclip)
    LST = get_sideral_local_time(M_earth, w_earth, lon, timestamp)
    [Az,delta] = get_azimuth_elevation(RA, Dec, LST, lat)
    return [RA, Dec, Az, delta]

def get_planet_position(planet, lon, lat, timestamp):
    d = timestamp_to_ellapsed_days(timestamp)
    [N,i,w_earth,a,e,M_earth] = get_orbital_params('earth', d)
    E = calculate_eccentric_anomaly(M_earth,e)
    [v,r] = calculate_true_anomaly(E, e, a)
    [x_earth, y_earth, z_earth] = calculate_ecliptic_xyz(r, N, w_earth, v, i)

    [N,i,w,a,e,M] = get_orbital_params(planet, d)
    E = calculate_eccentric_anomaly(M,e)
    [v,r] = calculate_true_anomaly(E, e, a)
    [x_planet, y_planet, z_planet] = calculate_ecliptic_xyz(r, N, w, v, i)

    x_planet -= x_earth
    y_planet -= y_earth
    z_planet -= z_earth
    [RA, Dec] = calculate_equatorial_coords(x_planet, y_planet, z_planet)
    LST = get_sideral_local_time(M_earth, w_earth, lon, timestamp)
    [Az,delta] = get_azimuth_elevation(RA, Dec, LST, lat)
    return [RA, Dec, Az, delta]


if __name__  == "__main__":
    lon = -99.1332*math.pi/180
    lat =  19.4326*math.pi/180
    td  = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S local time")
    ts  = datetime.datetime.now().timestamp()
    p   = "sun"
    for i in range(len(sys.argv)):
        if sys.argv[i] == "-d":
            td = sys.argv[i+1]
            ts = datetime.datetime.strptime(td, "%Y-%m-%dT%H:%M:%S%z").timestamp()
        elif sys.argv[i] == "--lon":
            lon = float(sys.argv[i+1])*math.pi/180
        elif sys.argv[i] == "--lat":
            lat = float(sys.argv[i+1])*math.pi/180
        elif sys.argv[i] == "--planet" or sys.argv[i] == "-p":
            p = sys.argv[i+1]
    print("Getting positions for " + p.upper() + " with:")
    print("Latitude  = " + rad_to_DMS(lat))
    print("Longitude = " + rad_to_DMS(lon))
    print("Date-Time = " + td)
    if p == 'sun':
        [RA, Dec, Az, Ele] = get_sun_position(lon, lat, ts)
    elif p == "moon":
        [RA, Dec, Az, Ele] = get_moon_position(lon, lat, ts)
    else:
        [RA, Dec, Az, Ele] = get_planet_position(p, lon, lat, ts)
    print("")
    print("The position of " + p.upper() + " is:")
    print("R. Ascension: " + rad_to_HMS(RA ))
    print("Declination:  " + rad_to_DMS(Dec))
    print("Azimuth:      " + rad_to_DMS(Az ))
    print("Elevation:    " + rad_to_DMS(Ele))
