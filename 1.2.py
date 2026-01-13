#For 1.2 we will create an application that gets info from our 1.1 server:
import requests

#Take note that the port number must match the one in question 1.1
response = requests.get("http://localhost:1230/predepartureInfo") #this is the address of the server made in 1.1
if response.status_code == 200:
    data = response.json()
    print("Pre-Departure Information:")
    print("*"*45)
    count = 1
    for item in data:
        print(f"Predeparture No: {count}")
        count +=1
        for key, value in item.items():
            print(f"{key}: {value}")
        print("="*45)
else:
    print("Failed to retrieve Pre-Departure information from server")
