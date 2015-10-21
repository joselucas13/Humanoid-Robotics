#!/usr/bin/env python

# Homework 3 - ECE 590

# Jose Lucas Gomes Olavo 

import math
import numpy

from transformation_matrix import *
from get_position import *

# Forward Kinematics
def get_FK(theta):
	l1 = 0.3
	l2 = 0.2
	l3 = 0.1
	x = l1*math.cos(theta[0]) + l2*math.cos(theta[0]+theta[1]) + l3*math.cos(theta[0]+theta[1]+theta[2])
	y = l1*math.sin(theta[0]) + l2*math.sin(theta[0]+theta[1]) + l3*math.sin(theta[0]+theta[1]+theta[2])
	return numpy.array([x,y])

# Euclidian Distance
def get_dist(e,g):
	tam_e = len(e)
	tam_g = len(g)
	summ = 0
	if (tam_e == tam_g):
		for i in range (0,tam_e):
			summ = (e[i] - g[i])**2 + summ
		d = math.sqrt(summ)
	return d

# Jacobian
def get_J(d_theta, theta):
	e = get_FK(theta)
	J = numpy.zeros(shape=(len(e),len(theta)))
	for i in range (0,len(e)):
		for j in range (0,len(theta)):
			theta_new = theta
			theta_new[j] = theta_new[j] + d_theta
			de = get_FK(theta_new) - e
			J[i,j] = de[i]/d_theta
	return J

# Get next Point
def get_next_point_delta(e,g,stp):
	m = g - e
	#print m
	m = m/numpy.linalg.norm(m)
	#print m
	p = m*stp
	#print p
	return p

def wrapTo2Pi(ang):
    return ang % (2*math.pi)

##########################################################################################################

# MAIN

theta = numpy.array([0,0,0])   		# Initial Angle
g = numpy.array([0.00,0.15])		# Goal Position
err = 0.003	  			# Maximum Error
dd_theta = 0.01 			# Delta theta
stp = 0.003	  			# Step

e = get_FK(theta)

count = 0
while(get_dist(e,g) > err):
	J = get_J(dd_theta, theta)
	#print J
	Jp = numpy.linalg.pinv(J)
	#print Jp
	de = get_next_point_delta(e,g,stp)
	#print de
	d_theta = numpy.dot(Jp,numpy.transpose(de))
	#print d_theta
	theta = theta + numpy.transpose(d_theta)
	#print theta
	theta = wrapTo2Pi(theta)
    	e = get_FK(theta)
	print e

	count = count + 1
	print count
    	if (count > 20000):
		break
	
print ("GOAL POSITION: x = %f y = %f" % (g[0],g[1]))
print ("FINAL POSITION: x = %f y = %f" % (e[0],e[1]))
print ("ERROR %f" % get_dist(e,g))
print theta
print theta*180/math.pi
