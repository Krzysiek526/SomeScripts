#!/usr/bin/python 

from socket import * 
from string import * 

# Create socket and bind to address 
UDPSock = socket(AF_INET,SOCK_DGRAM) 
UDPSock.bind(("",1964)) 

# Receive messages 
while 1: 
	data,addr = UDPSock.recvfrom(1964) 
	if not data: 
		print("Program has exited!") 
		break 
	else: 
		print( addr[0],data.decode() )

# Close socket 
UDPSock.close() 

