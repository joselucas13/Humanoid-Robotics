#!/usr/bin/env python

import multiprocessing as mp
import random
import string
import diff_drive
import ach
import sys
import time
from ctypes import *
import socket
import cv2.cv as cv
import cv2
import numpy as np
import csv

L = 5
N = 4
dd = diff_drive

r = ach.Channel(dd.CHAN_1)
r.flush()
s = ach.Channel(dd.CHAN_2)
s.flush()
v = ach.Channel(dd.CHAN_3)
v.flush()

c = csv.writer(open("file.csv", "wb"))

# Define process 1
def process_1():
	ref = dd.V_REF()
	ref.ref[0] = 1.0
	freq1 = 1.0
	print 'Process 1: Running.....'
	while(True):
		t1 = time.time()
		ref.ref[0] = -1.0*ref.ref[0]
		r.put(ref)
		print ref.ref[0]
		t2 = time.time()
 		temp = 1/freq1 - (t2 - t1)
        	if temp < 0:
 			temp = 0
 		time.sleep(temp)
		

# Define process 2
def process_2():
	ref_in = dd.V_REF()
	ref_out = dd.V_REF()
	print 'Process 2: Running.....'
	while (True):
		[status, framesize] = r.get(ref_in, wait=True, last=True)
    		if status == ach.ACH_OK or status == ach.ACH_MISSED_FRAME or status == ach.ACH_STALE_FRAMES:
        		ref_out.ref[0] = 2.5*ref_in.ref[0]
			print ref_out.ref[0]
			s.put(ref_out)
    		else:
        		raise ach.AchException( v.result_string(status) )

# Define process 3
def process_3():
	ref_in = dd.V_REF()
	ref_out = dd.V_REF()
	freq2 = 50.0
	t1 = time.time()
	print 'Process 3: Running.....'
	while (True):
		t2 = time.time()
		[status, framesize] = s.get(ref_in, wait=False, last=True)
    		if status == ach.ACH_OK or status == ach.ACH_MISSED_FRAME or status == ach.ACH_STALE_FRAMES:
        		ref_out.ref[0] = (ref_out.ref[0]*(L-1) + ref_in.ref[0])/L
			#print ref_out.ref[0]			
    		else:
        		raise ach.AchException( v.result_string(status) )				
		t3 = time.time()
		ref_out.sim[0] = t3-t1
		v.put(ref_out)
 		temp = 1/freq2 - (t3 - t2)
        	if temp < 0:
 			temp = 0
 		time.sleep(temp)

# Define process 4
def process_4():
	ref_in1 = dd.V_REF()
	ref_in2 = dd.V_REF()
	ref_in3 = dd.V_REF()
	print 'Process 4: Running.....'
	while (True):
		[status, framesize] = v.get(ref_in3, wait=True, last=True)
    		if status == ach.ACH_OK or status == ach.ACH_MISSED_FRAME or status == ach.ACH_STALE_FRAMES:
			pass			
    		else:
        		raise ach.AchException( v.result_string(status) )

		[status, framesize] = r.get(ref_in1, wait=False, last=True)
    		if status == ach.ACH_OK or status == ach.ACH_MISSED_FRAME or status == ach.ACH_STALE_FRAMES:
			pass			
    		else:
        		raise ach.AchException( v.result_string(status) )

		[status, framesize] = s.get(ref_in2, wait=False, last=True)
    		if status == ach.ACH_OK or status == ach.ACH_MISSED_FRAME or status == ach.ACH_STALE_FRAMES:
			pass			
    		else:
        		raise ach.AchException( v.result_string(status) )
				
		c.writerow([ref_in3.sim[0],ref_in1.ref[0],ref_in2.ref[0],ref_in3.ref[0]])

	
# Process that are running
processes = [mp.Process(target=process_1), mp.Process(target=process_2), mp.Process(target=process_3),mp.Process(target=process_4)]

# Run processes
for p in processes:
    p.start()
    #print p


t_init = time.time()
t_end = t_init
while((t_end-t_init) <= 8.0):
	
	#print (t_end-t_init)
	t_end = time.time()
	

# Exit the completed processes
for p in processes:
    p.terminate()

# Close the connection to the channels
r.close()
s.close()
v.close()

