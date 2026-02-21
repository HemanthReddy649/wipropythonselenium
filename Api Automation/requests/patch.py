import requests

try:
    data={
   "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    #make a get request to api endpoint
    response = requests.patch("https://api.restful-api.dev/objects/ff8081819c5368bb019c55a589b90475",json=data)
    print(response)
#check if type is 200 k
    if response.status_code==200:
        print("Status code is 200k")
        #prase the json file
        data = response.json()
        print(data)
    else:print(f"Error : recevied status code:{response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred:{e}")