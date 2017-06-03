#!/usr/bin/python

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto("hhiii",("192.168.10.102",2222))
