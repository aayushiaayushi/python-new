#! /usr/bin/python
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",9999))
while True:
	data=s.recvfrom(100)
	print "msg from client :",data[0]
	print "client address :",data[1][0]
