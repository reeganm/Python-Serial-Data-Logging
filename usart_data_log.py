#! /usr/bin/python

import serial
import sys
import datetime

now = datetime.datetime.now()

file = open(now.isoformat(),'w')
file.write("New log file" + now.isoformat() + "\n\r")

file.close()
