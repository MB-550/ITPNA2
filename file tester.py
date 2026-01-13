#This portion retrives the information from the file and collects it in a list of dictionaries
with open(r"C:\Users\bbggm\OneDrive\Documents\EDUVOS Year 2\ITPNA2\block 2\project\question 1\predeparture_info.txt",'r') as fileData:
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