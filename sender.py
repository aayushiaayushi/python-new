#! /usr/bin/python

import socket
import base64
serverip="192.168.10.102"
serverport=9999
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg=base64.b64encode(raw_input("enter your message:"))
s.sendto(msg,(serverip,serverport))
