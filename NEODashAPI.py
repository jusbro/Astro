import requests
import json
from pprint import pprint

# Call an API
response = requests.get('https://ssd-api.jpl.nasa.gov/cad.api?dist-max=1LD&date-min=2022-10-01&sort=h')
response.raise_for_status()  # check for errors
print(response.status_code)
# Load JSON data into a Python variable.
jsonData = json.loads(response.text)
pprint(jsonData)
