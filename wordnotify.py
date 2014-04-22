#!/bin/env python

import pynotify
import argparse
import random
import time
import os

mylist = []
iconpath = os.getcwd()
iconpath = os.path.join(iconpath, "wordnotify.png")
parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()
filename = args.filename

with open(filename) as f:
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
	if (len(randdata) > 2):
		randdesc = randdesc + "\n" + randdata[2]
	randdesc = "<b><i>" + randdesc + "</i></b>"
	word = pynotify.Notification(randword, randdesc, iconpath)
#	word.set_timeout(12)
	word.show()
	time.sleep(10)




