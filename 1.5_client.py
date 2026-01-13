#First we need to import some modules and classes for our HTTP server to work
from http.server import BaseHTTPRequestHandler,HTTPServer
import json
import time
import threading
#This is our HTTP class that will retrieve information from our file and send it to any http client as a json response
class HTTP_System(BaseHTTPRequestHandler):
    def do_GET(self):
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
def update_inflight_info():
    """Update the in-flight information a fixed number of times before stopping."""
    #This allows the program to stop so the loop doesn't run in the background
    max_updates = 5  # Number of times to update before stopping
    count = 0

    while count < max_updates:
        with open("InFlight_info.txt", 'w') as fileData:
            fileData.write("Auto-Pilot Status:Off;Cabin pressure:14.7;WiFi usage:ACTIVE for first class\n")
        print(f"Updated In-Flight Events! ({count + 1}/{max_updates})")
        time.sleep(5)  # Wait for 5 seconds
        count += 1

    print("Completed all updates. Stopping now.")

#This is our display function which runs our client HTTP server to view the json information                
def display(serverClass=HTTPServer, handler_class=HTTP_System, port=1234):
    server_address = ('', port)
    httpValue = serverClass(server_address, handler_class)
    print(f"Server is running on port: {port}")

    # Start the file update task in a separate thread
    updater_thread = threading.Thread(target=update_inflight_info, daemon=True)
    updater_thread.start()
    #This allows the program to stop so the loop doesn't run in the background
    
    # Run the HTTP server
    httpValue.serve_forever()
display()
