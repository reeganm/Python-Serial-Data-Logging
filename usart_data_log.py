#! /usr/bin/python
#this sketch logs data to a csv file
#it takes care of cleaning out special characters and adding new lines
#however data must be sent over serial in csv format
#also I am having issues with encoding special characters so I am only leting
#CAPITAL letters, numbers, and comma's through
import serial
import sys
import datetime

now = datetime.datetime.now()

#try: 
file = open('log' + str(now.year) + '_' + str(now.month) + '_' + str(now.day) + '_' + str(now.hour) + '_' + str(now.minute) + '_' + '.csv','w')
file.write("New log file" + str(now.isoformat()) + "\n\r")

ser = serial.Serial('COM5',115200,timeout=1)

not_accepted_chars = ['b', 'n', '\\', 'r', "'"]


   
while 1:
    line2 = ''
    line = str(ser.readline())
    for x in range(0,len(line)):
        if line[x] in not_accepted_chars:
            line2 = line2
        else:
            line2 = line2 + str(line[x])
    file.write(str(line2))
    file.write("\n\r")
    print(line2)

#except:
file.close()
ser.close()
