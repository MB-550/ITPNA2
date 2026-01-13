#This is our staff application that updates our information
import requests

URL = "http://localhost:1231/predepartureInfo"

status = True

while status == True:
    menu = input("Would you like to Add,Update or Exit \n Type add or exit: ")
    
    #Check if the user wants to add a record
    if menu.lower() == "add":
        status2 = True
        while status2 == True:
            command= input("Would you like to add a new record? Type Y or N: ")
            
            if command.lower()== "y":
                
                #Create a user interface to allow staff to specify the new info to be updated
                new_info = {"Action": "add",
                    "Aircraft status": input("Enter Aircraft status: "),
                    "Passenger boarding number": input("Enter Passenger boarding number: "),
                    "Fuelling": input("Enter Fuelling status: "),
                    "Door state": input("Enter Door state: "),
                    "Push back time": input("Enter Push back time: ")
                }
    
                response = requests.post(URL, json=new_info)
                
                if response.status_code == 200:
                    print(response.json()["message"])
                    
                else:
                    print("Failed to read Command.")
                    
                status2 = False
                
            elif command.lower()=="n":
                status2 = False
                print("Goodbye")
            
            else:
                print("!Incorrect command!\n")
    
    elif menu.lower() == "update":
        
        status3 = True
        while status3 == True:
            #Print menu to see which record user wants to update
            #Take note that the port number must match the one in question 1.3_server
            response = requests.get(URL) #this is the address of the server made in 1.1
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
                 
                #Get the users choice of which record they wish to update    
                selected_record = int(input("Type the record number you want to select: "))-1
                
                if selected_record >= 0 and selected_record < len(data): #checks the length of the data set::
                    print(f"You selected record No: {selected_record+1} to update")
                    #Now we need to access the dictionary record and update information the only information that won't change is the boarding number
                    key_list=["Action","Aircraft status","Passenger boarding number","Fuelling","Door state","Push back time"]
                    for key in key_list:
                        if key == "Action":
                            data[selected_record][key] = "update"
                            
                        if key != "Passenger boarding number" and key != "Action":
                            data[selected_record][key] = input(f"Please input the new {key}: ")
                            
                        if key == "Passenger boarding number":
                            print(f"The {key} is {data[selected_record][key]}")
                            
                        
                    
                    #next is to send the updated data to the server
                    respond = requests.post(URL, json=data[selected_record])
                    
                    if respond.status_code == 200:
                        print(respond.json()["message"])
                        
                    else:
                        print("Failed to read Command.")
                        
                    status3 = False
                else:
                    print("Invalid record selected try again")
            else:
                status3 = False
                print("Failed to retrieve Pre-Departure information from server")

        
    elif menu.lower() == "exit":
        print("Goodbye")
        status = False
        
    else:
        print("**Incorrect Menu Option**\n")
        
    
        

