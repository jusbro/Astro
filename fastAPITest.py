#This Script is used to quickly test APIs

import requests
import json
from pprint import pprint

#Personal API Key for Justin Brown
APIKey = 'xZ1whndF87Tihw0ZM7VQgAKthFXbVZZZ22eazebC' 

#The base API request goes below
APIBase = 'https://api.nasa.gov/planetary/apod?api_key='

# Call an API
response = requests.get(APIBase+APIKey)

#Check for Errors
#Visit this site for more error details: https://www.moesif.com/blog/technical/monitoring/10-Error-Status-Codes-When-Building-APIs-For-The-First-Time-And-How-To-Fix-Them/
#200 - Got Data Successfully
#400 - Client Side Errors
    #404 - Not Found
    #401 - Unauthorized
    #403 - Forbidden
    #429 - Too Many Requests
#500 - Server Side Error
response.raise_for_status()  
print("Response Code: "+response.status_code)


# Load JSON data into a Python variable.
jsonData = json.loads(response.text)
#Use PrettyPrint to display the JSON file nicely
pprint(jsonData)
