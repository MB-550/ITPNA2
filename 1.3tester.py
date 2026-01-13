import requests
#Create a user interface to allow staff to specify the new info to be updated

#print a menu:    
#Take note that the port number must match the one in question 1.1
response = requests.get("http://localhost:1229/predepartureInfo") #this is the address of the server made in 1.3_server
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

info_chosen = input("Please select which predeparture info you want to update by typing in a number or new for a new record")
    
new_info = {
    "Push back time": "15:00",
    "Passenger boarding number": "135",
    "Fuelling": "In Progress"
}
