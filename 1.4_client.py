#For 1.4 we will create an application that gets info from our 1.4 server:
import requests

#Take note that the port number must match the one in  1.4 server
response = requests.get("http://localhost:1231/InFlightInfo") #this is the address of the server made in 1.1
if response.status_code == 200:
    data = response.json()
    print("In-Flight Information:")
    print("*"*45)
    count = 1
    for item in data:
        print(f"In-Flight No: {count}")
        count +=1
        for key, value in item.items():
            print(f"{key}: {value}")
        print("="*45)
else:
    print("Failed to retrieve In-Flight information from server")


