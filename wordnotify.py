#!/bin/env python

import pynotify
import random
import time

mylist = []

with open("jap.txt") as f:
	for line in f:
		mylist.append(line)
f.close()

listsize = len(mylist)

pynotify.init("init")
while True:
	randnumber = random.randrange(0, listsize)
	randline = mylist[randnumber]
	print randnumber, randline
	randdata = randline.split(":")
	randword = randdata[0]
	randdesc = randdata[1]
	randdesc = "<i>" + randdesc + "</i>"
	word = pynotify.Notification(randword, randdesc, "dialog-information")
	word.show()
	time.sleep(10)




