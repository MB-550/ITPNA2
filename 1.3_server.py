#First we need to import some modules and classes for our HTTP server to work
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


#This is our HTTP class that will retrieve information from our file and send it to any http client as a json response

class HTTP_System(BaseHTTPRequestHandler):
    #This function has remained unchanged from 1.1
    def do_GET(self):
        if self.path == "/predepartureInfo":
            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.end_headers()

            try:
                with open(r"predeparture_info.txt", 'r') as fileData:
                    singleData = fileData.readlines()
                    dataUser = []

                    for line in singleData:
                        Aircraft_status, Passenger_boardingNo, Fuelling, DoorState, Push_back_time = line.strip().split(',')
                        dataUser.append({
                            "Aircraft status": Aircraft_status.split(';')[1],
                            "Passenger boarding number": Passenger_boardingNo.split(';')[1],
                            "Fuelling": Fuelling.split(';')[1],
                            "Door state": DoorState.split(';')[1],
                            "Push back time": Push_back_time.split(";")[1] 
                        })

                    self.wfile.write(json.dumps(dataUser).encode())

            except FileNotFoundError:
                self.wfile.write(json.dumps("ERROR: File not found").encode())
        #1.4 section:        
        if self.path=="/InFlightInfo":
            self.send_response(200)
            self.send_header("content-type","application/json")
            self.end_headers()
            
            try:
                #This portion retrives the information from the file and collects it in a list of dictionaries
                with open(r"InFlight_info.txt",'r') as fileData:
                    singleData = fileData.readlines()
                    
                    dataUser = []
                    
                    for line in singleData:
                        Autopilot_status,Cabin_pressure,WiFi_usage = line.strip().split(';')
                        dataUser.append({"Auto-Pilot Status" :Autopilot_status.split(':')[1],
                                         "Cabin pressure":Cabin_pressure.split(':')[1],
                                         "WiFi usage":WiFi_usage.split(':')[1]
                                         })
                       
                    print(dataUser)    
                    self.wfile.write(json.dumps(dataUser).encode())
                    
            except FileNotFoundError:
                self.wfile.write(json.dumps("ERROR file not found").encode())
                
    #This is our new function that implements the updated information
    def do_POST(self):
        if self.path == "/predepartureInfo":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            new_info = json.loads(post_data)
            print(new_info)
            
            #Create a condition statement to check if the new_info action equals add
            if new_info.get("Action") == "add":
                
                try:

                    # Read existing data
                    with open(r"predeparture_info.txt", 'r') as fileData:
                        singleData = fileData.readlines()
        
                    updated_lines = []
                    for line in singleData:
                        #This maintains current information
                        updated_lines.append(line)
                        
                        #This uses an existing entry to add new information while retaining the existing information
                        Aircraft_status, Passenger_boardingNo, Fuelling, DoorState, Push_back_time = line.strip().split(',')
        
                        updated_entry = {
                            "Aircraft status": new_info.get("Aircraft status", Aircraft_status.split(';')[1]),
                            "Passenger boarding number": new_info.get("Passenger boarding number", Passenger_boardingNo.split(';')[1]),
                            "Fuelling": new_info.get("Fuelling", Fuelling.split(';')[1]),
                            "Door state": new_info.get("Door state", DoorState.split(';')[1]),
                            "Push back time": new_info.get("Push back time", Push_back_time.split(";")[0])
                        }
        
                    updated_lines.append(f"Aircraft status;{updated_entry['Aircraft status']},"+
                                         f"Passenger boarding number;{updated_entry['Passenger boarding number']},"+
                                         f"Fuelling;{updated_entry['Fuelling']},"+
                                         f"Door state;{updated_entry['Door state']},"+
                                         f"Push back time;{updated_entry['Push back time']}\n")
        
                    # Write updated data back to file
                    with open(r"predeparture_info.txt", 'w') as fileData:
                        
                        fileData.writelines(updated_lines)
        
                    self.send_response(200)
                    self.send_header("content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps({"message": "Pre-Departure information updated successfully!"}).encode())
        
                except FileNotFoundError:
                    self.send_response(500)
                    self.end_headers()
                    self.wfile.write(json.dumps({"error": "File not found"}).encode())
                    
            #next add the elif to check if a record needs to be updated:
            elif new_info.get("Action") == "update":
                try:
    
                    # Read existing data
                    with open(r"predeparture_info.txt", 'r') as fileData:
                        singleData = fileData.readlines()
        
                    updated_lines = []
                    
                    for line in singleData:
                        dic = {key.strip():value.strip() for key, value in (item.split(";")for item in line.split(","))}
                        
                        #This uses an existing entry to add new information while retaining the existing information
                        Aircraft_status, Passenger_boardingNo, Fuelling, DoorState, Push_back_time = line.strip().split(',')
                        updated_entry = {
                            "Aircraft status": new_info.get("Aircraft status", Aircraft_status.split(';')[1]),
                            "Passenger boarding number": new_info.get("Passenger boarding number", Passenger_boardingNo.split(';')[1]),
                            "Fuelling": new_info.get("Fuelling", Fuelling.split(';')[1]),
                            "Door state": new_info.get("Door state", DoorState.split(';')[1]),
                            "Push back time": new_info.get("Push back time", Push_back_time.split(";")[1])
                        }
                        
                        new_line = str(f"Aircraft status;{updated_entry['Aircraft status']},"+
                                         f"Passenger boarding number;{updated_entry['Passenger boarding number']},"+
                                         f"Fuelling;{updated_entry['Fuelling']},"+
                                         f"Door state;{updated_entry['Door state']},"+
                                         f"Push back time;{updated_entry['Push back time']}\n")
                        
                        
                        if dic["Passenger boarding number"] != updated_entry["Passenger boarding number"]:
                            
                            updated_lines.append(line)
                        
                    updated_lines.append(new_line) 
                            
                    # Write updated data back to file
                    with open(r"predeparture_info.txt", 'w') as fileData:
                        
                        fileData.writelines(updated_lines)
        
                    self.send_response(200)
                    self.send_header("content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps({"message": "Pre-Departure information updated successfully!"}).encode())
                
                except FileNotFoundError:
                    self.send_response(500)
                    self.end_headers()
                    self.wfile.write(json.dumps({"error": "File not found"}).encode())

def display(serverClass=HTTPServer, handler_class=HTTP_System, port=1231):
    server_address = ('', port)
    httpValue = serverClass(server_address, handler_class)
    print(f"Server is running on port: {port}")
    httpValue.serve_forever()

display()


