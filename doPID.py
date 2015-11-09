#!/usr/bin/env python

# Homework 6 - ECE 590

# Jose Lucas Gomes Olavo 

import math
import numpy

Kp = 0.5
Ki = 0.1
Kd = 0.02

# Controller
def doPID(d_goal,D,err_old,temp_new,temp_old):
	
	err = -float(d_goal - D)
	integ = err + err_old
	if integ > 2.0:
		integ = 2.0
	deriv = float((err-err_old)/(temp_new-temp_old))

	c = float(Kp*err + Ki*integ + Kd*deriv)
	print 'P %f' % float(Kp*err)
	print 'I %f' % float(Ki*integ)
	print 'D %f' % float(Kd*deriv)

	if (c > 3.5):
		c = 3.5

	if (c < -3.5):
		c = -3.5

	err_old = integ
	return [c,err_old]

