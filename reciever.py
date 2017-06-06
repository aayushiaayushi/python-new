#!/usr/bin/python


import socket
import base64

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverip="192.168.10.102"
serverport=9999
s.bind(("192.168.10.102",9999))
while True:
	data=s.recvfrom(100)	
	a=base64.b64decode(data[0])
	print a
	print "msg from client :",data[0]
	print "client address:",data[1][0]
