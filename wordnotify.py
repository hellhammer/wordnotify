#!/usr/bin/env python

import pynotify
import argparse
import random
import time
import csv
import os

mydict = {}
index = 0
iconpath = os.getcwd()
iconpath = os.path.join(iconpath, "wordnotify.png")
parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()
filename = args.filename

with open(filename, 'rb') as f:
    reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
    for line in reader:
        index += 1
        mydict[index] = line
f.close()

dictsize = len(mydict)

pynotify.init("init")
while True:
    randnumber = random.randrange(1, dictsize)
#    random.shuffle(mydict)
    line = mydict[randnumber]
    if len(line) < 3:
        eng, roma, jap = line[0], line[1], ''
    else:
        eng, roma, jap = line[0], line[1], line[2]

    print '%i/%i: %s -- %s -- %s' % (randnumber, dictsize, eng, roma, jap)

    desc = "<b><i>" + roma + "\n" + jap + "</i></b>"
    word = pynotify.Notification(eng, desc, iconpath)
    word.set_timeout(1000)
    word.show()
    time.sleep(2)