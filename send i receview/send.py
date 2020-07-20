#!/usr/bin/python

import socket 

def snd(data): 
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
	s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) 
	s.sendto(data, ('255.255.255.255', 1964)) 
	s.close()  

# Send messages 

while (1): 
	data = input('>>')
	if not data: 
		break 
	else: 
		snd(data.encode()) 

