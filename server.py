#!/usr/bin/python

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",2222))
while True:
	data=s.recvfrom(200)
	print "msg from clieny:",data[0]
	print "client address:",data[1][0]
