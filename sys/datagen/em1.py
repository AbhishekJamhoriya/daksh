import paho.mqtt.publish as publish
import os
import json
from datetime import datetime
from random import randint
import time
import csv
MQTT_SERVER = "10.6.0.71"
MQTT_PATH = "001"
d13=0;
"""
filename = "/home/pi/em1_csv.csv"
if os.path.exists(filename):
    
    f= open(filename,'r')
    d13= f.read()
    d13 =float(d13)
else:
    pass
d21 =0
d22 =0
"""
while True:
    
    d1 = randint(49,51)
    d2 = randint(220,250)
    d3 = randint(220,250)
    d4 = randint(220,250)
    d5 = randint(405,440)
    d6 = randint(405,440)
    d7 = randint(405,440)
    d8 = randint(70,100)
    d9 = randint(70, 100)
    d10 = randint(70, 100)
    d11 = (d8+d9+d10)/3
    d12 = 1.732*d5*d11/1000.0
    #if d21 < d22:
       # d13 = d13+0.1;
    """
        a1=d13;
        f= open(filename,'w')
        a1=str(a1)
        f.write(a1);
        d22 = 0;
        """
#    d21 = randint(1,10)
#
#    print(d21)
    
#    if d21 >= d22:
#        d22 = d22 +1;
   
    d14 = randint(85,100)/100.0
    d15 = randint(250,500)/100.0
    d16 =  randint(250,500)/100.0
    d17 =randint(250,500)/100.0
    d18 =randint(250,500)/100.0
    d19 =d13
    d20 = 0.0;
    

    
    data = json.dumps({ "ID":"001", "N1":d1,"N2":d2,"N3":d3,"N4":d4,"N5":d5,"N6":d6,"N7":d7,"N8":d8,"N9":d9,"N10":d10,"N11":d11,"N12":d12,"N13":d13,"N14":d14,"N15":d15,"N16":d16,"N17":d17,"N18":d18,"N19":d19,"N20":d20})
    print(data)

    publish.single(MQTT_PATH, data, hostname=MQTT_SERVER,port=1883,
        client_id="espclient1",
        qos=1,will=None, tls=None,
        transport="tcp")

    print("data sent")
    time.sleep((randint(85,130)/100.0))
   
   
    #publish.single(MQTT_PATH, MSG, hostname=MQTT_SERVER,port=1883,client_id="espclient",qos=0, auth={'username':"kamal", 'password':"23021991"} ,will=None, tls=None,
    #transport="tcp")
    
   
        
