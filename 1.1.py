#First we need to import some modules and classes for our HTTP server to work
from http.server import BaseHTTPRequestHandler,HTTPServer
import json

#This is our HTTP class that will retrieve information from our file and send it to any http client as a json response
class HTTP_System(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path=="/predepartureInfo":
            self.send_response(200)
            self.send_header("content-type","application/json")
            self.end_headers()
            
            try:
                #This portion retrives the information from the file and collects it in a list of dictionaries
                with open(r"predeparture_info.txt",'r') as fileData:
                    singleData = fileData.readlines()
                    
                    dataUser = []
                    
                    for line in singleData:
                        Aircraft_status,Passenger_boardingNo,Fuelling,DoorState,Push_back_time = line.strip().split(';')
                        dataUser.append({"Aircraft status" :Aircraft_status.split(':')[1],
                                         "Passenger boarding number":Passenger_boardingNo.split(':')[1],
                                         "Fuelling":Fuelling.split(':')[1],
                                         "Door state":DoorState.split(':')[1],
                                         "Push back time": Push_back_time.split(":")[1] +":"+Push_back_time.split(":")[2]})
                       
                    print(dataUser)    
                    self.wfile.write(json.dumps(dataUser).encode())
                    
            except FileNotFoundError:
                self.wfile.write(json.dumps("ERROR file not found").encode())

#This is our display function which runs our client HTTP server to view the json information                
def display(serverClass=HTTPServer, handler_class=HTTP_System, port = 1228):#It is important to note that everytime you run you might have to change the port number
    server_address=('',port)
    httpValue = serverClass(server_address,handler_class)
    print(f"Server is running on port: {port}")
    httpValue.serve_forever()
    
display()