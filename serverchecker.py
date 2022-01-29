import paramiko
import time
import os
import json
import sys
from getpass import getpass

print("ServerChecker")
print("Check and command your linux server without knowing Linux")
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')

#Know if the program has been opened already:

f = open("data/1ststart", "r")
iststart = f.read()
f.close

if iststart == "0":
    print("Looks like you haven't started this program before. You have to fill the file located in 'data/info.txt'.")
    ok = input("If you have already done the setup, press enter and execute the program again. If you haven't, edit the file with the help of the manual.")
    f = open("data/1ststart", "w")
    iststart = f.write("1")
    f.close
    sys.exit()
    
#open json file with the server data
js = open("data/info.txt", "r")
jsondata = f.read()
file_path = "data/info.txt"
with open(file_path, 'r') as j:
     jdfp = json.loads(j.read())
#jdfp = json.loads(jsondata)
f.close

os.system('cls' if os.name == 'nt' else 'clear')

#Initial menu
print("Options avalible for the server: ")
print("1) Check server temperature")
print("2) Reboot the server")
print("3) Shut down the server (in 1 minute)")
print("4) Shut down the server (instantaniously)")
print("5) Custom command (check README)")

option = input("Type a number an then press enter: ")

#Enter the server
host = (jdfp["ip"])
port = (jdfp["port"])
username = (jdfp["user"])
password = getpass("Password for user " + username + ": ")

if option == "1":
    command = "echo wip"
elif option == "2":
    command = "sudo reboot"
elif option == "3":
    command = "sudo shutdown +1"
elif option == "4":
    command = "sudo shutdown now"
elif option == "5":
    command = (jdfp["custom_command"])
else:
    print("ERROR: No command selected. Program will close.")
    sys.exit()

#make contact with server and do operation
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()
print(lines)