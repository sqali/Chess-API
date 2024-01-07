# Importing Libraries
import requests
import pandas as pd

# Link of the website
link = "https://www.chess.com"
response = requests.get(link)

# Function to check the status of the connection
def check_response(link):

    if response.status_code == 200:
        return "Connection Status is OK - {0}".format(response.status_code)
    
    elif response.status_code == 400:
        return "Connection Status is Bad request - {0}".format(response.status_code)
    
    elif response.status_code == 401:
        return "Connection Status is Unauthorized - {0}".format(response.status_code)
    
    elif response.status_code == 403:
        return "Connection Status is Forbidden - {0}".format(response.status_code)
    
    elif response.status_code == 404:
        return "Connection Status is Not found - {0}".format(response.status_code)
    
    elif response.status_code == 429:
        return "Connection Status is Too Many requests - {0}".format(response.status_code)
    
    elif response.status_code == 500:
        return "Connection Status is Internal server error - {0}".format(response.status_code)
    
    elif response.status_code == 504:
        return "Connection Status is Service Unavailable - {0}".format(response.status_code)