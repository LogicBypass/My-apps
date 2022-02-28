#!/bin/python3

import socket
import sys
from datetime import datetime


def banner():
	print("\n")
	print("██╗      ██████╗  ██████╗ ██╗ ██████╗    ██████╗ ██╗   ██╗██████╗  █████╗ ███████╗███████╗")
	print("██║     ██╔═══██╗██╔════╝ ██║██╔════╝    ██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝")
	print("██║     ██║   ██║██║  ███╗██║██║         ██████╔╝ ╚████╔╝ ██████╔╝███████║███████╗███████╗")
	print("██║     ██║   ██║██║   ██║██║██║         ██╔══██╗  ╚██╔╝  ██╔═══╝ ██╔══██║╚════██║╚════██║")
	print("███████╗╚██████╔╝╚██████╔╝██║╚██████╗    ██████╔╝   ██║   ██║     ██║  ██║███████║███████║")
	print("╚══════╝ ╚═════╝  ╚═════╝ ╚═╝ ╚═════╝    ╚═════╝    ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝")
	print("== Terrible port scanner that don't know about threading for testing programing skills ==")
	print("https://github.com/LogicBypass")
	print("\n")



#syntax: python3 scanner.py <hostname or ip>
#                  arg0          arg1
#"sys.argv" == "$1" in bash


#Define target
banner()
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])     #Translate hostname to IPv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <hostname or IP>")
	print("Example: python3 scanner.py 192.168.100.1")

#Scaninfo
print("*"*50)
print("Scanning target ", target)
print("Time started: ",datetime.now())
print("*"*50)
print("\n")

try:
	for port in range(1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(0.01)
		result= s.connect_ex((target,port))         #return an error indicator, if open = 0 if not = 1
		#print("Check the port {}".format(port))    #Trubleshooting speed and ports ratio
		if result == 0:
			print('Port {} is open'.format(port))
		s.close
except KeyboardInterrupt:
	print("\nExiting program")
	sys.exit()
except socket.gaierror:
	print("Hostname could not be ressolved.")
	sys.exit()
except socket.error:
	print("Couldn't connect to server.")
	sys.exit()