#!/usr/bin/python

import serial
import math
import time
import sys
import multiprocessing as mp
import random
import string
import common
import ach
import sys
import time
from ctypes import *
import socket
import cv2.cv as cv
import cv2
import numpy as np
import csv

dd = common
ref = dd.ServoPosition()
r = ach.Channel(DYNAMIXEL_CHANNEL)
r.flush()

def rad2tick(r):
	r += 150 * math.pi / 180.0
	ticks = r * 0x3ff / (300 * math.pi / 180.0)
	return int(math.floor(ticks))

def tick2rad(ticks):
	r = ticks * (300 * math.pi / 180.0) / 1023.0
	r -= 150 * math.pi / 180.0
	return r

def write_register(ser, dev_id, address, value):
	value_l = value & 0xff
	value_h = (value & 0xff00) >> 8
	# ID, length, instruction, address, value_l, value_h, cksum
	# length is byte count of instruction + payload + cksum
	# WRITE_DATA instruction id 0x03
	data = [dev_id, 5, 0x03, address, value_l, value_h]
	checksum = ~reduce(lambda x,y: x+y, data) & 0xff
	packet = b'\xff\xff' + bytearray(data) + bytearray([checksum])
	ser.write(packet)

def set_position(ser, dev_id, angle):
	# Goal Position is a 16-bit, little-endian number at address 0x1e
	write_register(ser, dev_id, 0x1e, rad2tick(angle))


high_angle = 120.0 * (math.pi/180.0)
low_angle = -120.0 * (math.pi/180.0)

def wait_angles():
	dynamixel = serial.Serial('/dev/ttyUSB0', baudrate=1000000)
	while(True):
		[status, framesize] = r.get(ref, wait=True, last=True)
    		if status == ach.ACH_OK or status == ach.ACH_MISSED_FRAME or status == ach.ACH_STALE_FRAMES:
			
			if (ref.pos[dd.POS_x] > high_value):
				ref.pos[dd.POS_x] = high_value
			if (ref.pos[dd.POS_x] < low_value):
				ref.pos[dd.POS_x] = low_value    		
			set_position(dynamixel,1,ref.pos[dd.POS_x])

			if (ref.pos[dd.POS_y] > high_value):
				ref.pos[dd.POS_y] = high_value
			if (ref.pos[dd.POS_y] < low_value):
				ref.pos[dd.POS_y] = low_value
			set_position(dynamixel,2,ref.pos[dd.POS_y])

    		else:
        		raise ach.AchException( v.result_string(status) )
		

#if (len(sys.argv) < 2):
#	print "Error: must specify USB to Dynamixel device"
#	sys.exit(1)
#	print "Talking to dynamixels on", sys.argv[1]
#	dynamixel = serial.Serial(sys.argv[1], baudrate=1000000)

#try:
#	while True:
#		args = input()
#		set_position(dynamixel, args[0], args[1])
#except KeyboardInterrupt:
#	dynamixel.close()
