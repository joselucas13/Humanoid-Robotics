#!/usr/bin/env python

# Homework 4 - ECE 590

# Jose Lucas Gomes Olavo

import math
import numpy

# Get Position
def get_Pos(T):
	
	x = T[0,3]
	y = T[1,3]
	z = T[2,3]

	thetax = math.atan2(T[2,2],T[2,1])
	thetay = math.atan2((T[2,1]**2 + T[2,2]**2),-T[2,0])
	thetaz = math.atan2(T[0,0],T[1,0])
	
	print [x,y,z,thetax,thetay,thetaz]
	return [x,y,z,thetax,thetay,thetaz]
	
