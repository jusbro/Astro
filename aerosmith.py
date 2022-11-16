import requests
import json
from pprint import pprint
import math

#METHODS
def callApi():
    response = requests.get('https://ssd-api.jpl.nasa.gov/cad.api?dist-max=10LD&date-min=2022-10-01&diameter=true&pha=true&sort=dist')
    response.raise_for_status()  # check for errors
    print(response.status_code)
    # Load JSON data into a Python variable.
    jsonData = json.loads(response.text)
    return jsonData


def determineSize():
#diameter can be determined by the magnitude (h) and the albedo (p)
#The equation can be found here: http://www.physics.sfasu.edu/astro/asteroids/sizemagnitude.html
#D = (1329/sqrt(p))*10^-0.2h
#typical albedo (p) ranges from 0.05 to 0.25 for minor planets/asteroids
    magnitude = 15
    D = (1329/math.sqrt(0.1))*10**(-.2*magnitude)
    print("Calculated Diameter: ",D)
print("Welcome to the Potentially Hazardous Asterioids Dashboard\n")
print("This script will display any potentially hazardous asteriods near Earth\n\n")
input("Press ENTER to begin download of data")
callApi()
determineSize()
