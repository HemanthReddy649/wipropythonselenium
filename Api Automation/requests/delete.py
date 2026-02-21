import requests

try:

    #make a get request to a api endpoint
    response =requests.delete("https://videogamedb.uk:443/api/v2/videogame/1")
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