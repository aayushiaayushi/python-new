#! /usr/bin/python

import sys
import os
import os.path
s=sys.argv[1:]
for i in s:
	if os.path.isdir(i) :
		print "File exists"
	else:
		os.makedirs(i)
