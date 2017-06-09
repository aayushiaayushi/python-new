#! /usr/bin/python

import os
import sys
from stat import *
s=sys.argv[1:]
for i in s:
	if os.path.isfile(i):
		print "File exist"
		
	else:
		f=open(i,'a+')
		st=os.stat(i)
		atime=st[ST_ATIME]
		mtime=st[ST_MTIME]
		new_mtime=mtime+(4*3600)
		os.utime(i,(atime,new_mtime))
