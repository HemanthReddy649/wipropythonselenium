import requests
from requests.auth import HTTPBasicAuth
from werkzeug.datastructures import Headers

try:
    headers = {
        "User-Agent": "MyApp/1.0",
        "Accept": "application/json"
    }
    
    #make a get request to a api endpoint
    response =requests.get("https://videogamedb.uk:443/api/v2/videogame",auth=HTTPBasicAuth('username','password'),timeout=5,headers=headers)
    print(response)

#check if type status is 200 k
    if response.status_code==200:
        print("status code is 200 k")
        #parse the json file
        data = response.json()
        print(data)
    else:
        print(f"Error: Received status code{response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred:{e}")