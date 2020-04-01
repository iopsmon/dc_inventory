#DESCRIPTION:This python script provides OS information 
#FILENAME:
#USAGE:python <script name>
#DATE:28/03/2020
#VERSION:0.1
#OWNER:Deepak Chohan
#Next IP 

#Import modules
import sys
import platform
import uuid 
import datetime
import os
import socket 

#custom variables
my_date = datetime.datetime.now()


#Functions

#This checks to see if the id.txt file exists, if not then create a file
# and generate the unique host ID 

#Gen ID Function 
def my_gen_id ():
    exists = os.path.isfile('/opt/splunk/etc/apps/DC_inventory/bin/scripts/id.txt')
    if exists:
        print("ID file exists")
        f = open("/opt/splunk/etc/apps/DC_inventory/bin/scripts/id.txt", "r")
        host_id = (f.read()) 
        print(f.read()) 
        print ("ID=",host_id)
    else:
        print("file not here creating new ID ")
        f = open("/opt/splunk/etc/apps/DC_inventory/bin/scripts/id.txt", "w")
        f.write(str(uuid.uuid1()))
        f.close()
        
#Main OS inventory Code Function
def my_open_log():
    #Reading Unique ID 
    print("Reading ID file")
    id_file_path ='/opt/splunk/etc/apps/DC_inventory/bin/scripts/id.txt'
    my_id_file = open(id_file_path,'r')
    my_id_file.read 
    id = my_id_file.readline()
    #Get IP 
    host_name = socket.gethostname() 
    host_ip = socket.gethostbyname(host_name) 
    #Generating Data into file
    print("Generating Inventory Data")
    f = open("/opt/splunk/etc/apps/DC_inventory/bin/scripts/os_inv.log", "w")
    f.write(my_date.strftime("%d %m %Y %H:%M:%S"))
    f.write(",")
    f.write("node=")
    f.write(platform.node()) 
    f.write(",")
    f.write("system=")
    f.write(platform.system()) 
    f.write(",")
    f.write("release=")
    f.write(platform.release()) 
    f.write(",")
    f.write("version=")
    f.write(platform.version()) 
    f.write(",")
    f.write("machine=")
    f.write(platform.machine()) 
    f.write(",")
    f.write("processor=")
    f.write(platform.processor()) 
    f.write(",")
    f.write("id=")
    f.write(id)
    f.write(",")
    f.write("ip=")
    f.write(host_ip)
    f.close()

#Call Functions 
my_gen_id()
my_open_log() 

