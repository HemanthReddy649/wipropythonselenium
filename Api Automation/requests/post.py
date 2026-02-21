import requests

try:
    data={
  "category": "Platform",
  "name": "Mario",
  "rating": "Mature",
  "releaseDate": "2012-05-04",
  "reviewScore": 85
}
    #make a get request to a api endpoint
    response =requests.post("https://videogamedb.uk:443/api/v2/videogame",json=data)
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