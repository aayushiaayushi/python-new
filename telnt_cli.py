#!/bin/python

import socket,os,commands,time,sys
import getpass 
import crypt
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
user=raw_input("enter user name:")
password=raw_input("enter password:")

s.sendto(user,("192.168.10.102",4444))
s.sendto(password,("192.168.10.102",4444))
print s.recvfrom(100)
while True:
	cmd=raw_input("ferf")
	s.sendto(cmd,("192.168.10.102",4444))
	print s.recvfrom(100)[0]
