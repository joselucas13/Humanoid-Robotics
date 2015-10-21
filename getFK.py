#!/usr/bin/env python

# Homework 4 - ECE 590

# Jose Lucas Gomes Olavo 

import math
import numpy

from parameters import *

# Rotation Matrix x
def R_x(theta):
	rot_x = numpy.matrix([[1,0,0],[0,math.cos(theta),-math.sin(theta)],[0,math.sin(theta),math.cos(theta)]])
	return rot_x

# Rotation Matrix y
def R_y(theta):
	rot_y = numpy.matrix([[math.cos(theta),0,math.sin(theta)],[0,1,0],[-math.sin(theta),0,math.cos(theta)]])
	return rot_y

# Rotation Matrix z
def R_z(theta):
	rot_z = numpy.matrix([[math.cos(theta),-math.sin(theta),0],[math.sin(theta),math.cos(theta),0],[0,0,1]])
	return rot_z

# Transformation Matrix
def get_T(theta,side):

	# LEFT SIDE
	if (side == 'L'):
		R1 = K_LSP.thetax*R_x(theta[0]) + K_LSP.thetay*R_y(theta[0]) + K_LSP.thetaz*R_z(theta[0])
		T1 = numpy.matrix([[R1[0,0],R1[0,1],R1[0,2],K_LSP.x],[R1[1,0],R1[1,1],R1[1,2],K_LSP.y],[R1[2,0],R1[2,1],R1[2,2],K_LSP.z],[0,0,0,1]])	
		#print T1

		R2 = K_LSR.thetax*R_x(theta[1]) + K_LSR.thetay*R_y(theta[1]) + K_LSR.thetaz*R_z(theta[1])
		T2 = numpy.matrix([[R2[0,0],R2[0,1],R2[0,2],K_LSR.x],[R2[1,0],R2[1,1],R2[1,2],K_LSR.y],[R2[2,0],R2[2,1],R2[2,2],K_LSR.z],[0,0,0,1]])	
		#print T2

		R3 = K_LSY.thetax*R_x(theta[2]) + K_LSY.thetay*R_y(theta[2]) + K_LSY.thetaz*R_z(theta[2])
		T3 = numpy.matrix([[R3[0,0],R3[0,1],R3[0,2],K_LSY.x],[R3[1,0],R3[1,1],R3[1,2],K_LSY.y],[R3[2,0],R3[2,1],R3[2,2],K_LSY.z],[0,0,0,1]])	
		#print T3

		R4 = K_LEP.thetax*R_x(theta[3]) + K_LEP.thetay*R_y(theta[3]) + K_LEP.thetaz*R_z(theta[3])
		T4 = numpy.matrix([[R4[0,0],R4[0,1],R4[0,2],K_LEP.x],[R4[1,0],R4[1,1],R4[1,2],K_LEP.y],[R4[2,0],R4[2,1],R4[2,2],K_LEP.z],[0,0,0,1]])	
		#print T4

		R5 = K_LWR.thetax*R_x(theta[4]) + K_LWR.thetay*R_y(theta[4]) + K_LWR.thetaz*R_z(theta[4])
		T5 = numpy.matrix([[R5[0,0],R5[0,1],R5[0,2],K_LWR.x],[R5[1,0],R5[1,1],R5[1,2],K_LWR.y],[R5[2,0],R5[2,1],R5[2,2],K_LWR.z],[0,0,0,1]])	
		#print T5

		R6 = K_LWP.thetax*R_x(theta[5]) + K_LWP.thetay*R_y(theta[5]) + K_LWP.thetaz*R_z(theta[5])
		T6 = numpy.matrix([[R6[0,0],R6[0,1],R6[0,2],K_LWP.x],[R6[1,0],R6[1,1],R6[1,2],K_LWP.y],[R6[2,0],R6[2,1],R6[2,2],K_LWP.z],[0,0,0,1]])	
		#print T6

		T7 = numpy.matrix([[1,0,0,K_LED.x],[0,1,0,K_LED.y],[0,0,1,K_LED.z],[0,0,0,1]])
		#print T7

		T = T1*T2*T3*T4*T5*T6*T7
		print T
		return T

	# RIGHT SIDE
	if (side == 'R'):
		R1 = K_RSP.thetax*R_x(theta[0]) + K_RSP.thetay*R_y(theta[0]) + K_RSP.thetaz*R_z(theta[0])
		T1 = numpy.matrix([[R1[0,0],R1[0,1],R1[0,2],K_RSP.x],[R1[1,0],R1[1,1],R1[1,2],K_RSP.y],[R1[2,0],R1[2,1],R1[2,2],K_RSP.z],[0,0,0,1]])	
		#print T1

		R2 = K_RSR.thetax*R_x(theta[1]) + K_RSR.thetay*R_y(theta[1]) + K_RSR.thetaz*R_z(theta[1])
		T2 = numpy.matrix([[R2[0,0],R2[0,1],R2[0,2],K_RSR.x],[R2[1,0],R2[1,1],R2[1,2],K_RSR.y],[R2[2,0],R2[2,1],R2[2,2],K_RSR.z],[0,0,0,1]])	
		#print T2

		R3 = K_RSY.thetax*R_x(theta[2]) + K_RSY.thetay*R_y(theta[2]) + K_RSY.thetaz*R_z(theta[2])
		T3 = numpy.matrix([[R3[0,0],R3[0,1],R3[0,2],K_RSY.x],[R3[1,0],R3[1,1],R3[1,2],K_RSY.y],[R3[2,0],R3[2,1],R3[2,2],K_RSY.z],[0,0,0,1]])	
		#print T3

		R4 = K_REP.thetax*R_x(theta[3]) + K_REP.thetay*R_y(theta[3]) + K_REP.thetaz*R_z(theta[3])
		T4 = numpy.matrix([[R4[0,0],R4[0,1],R4[0,2],K_REP.x],[R4[1,0],R4[1,1],R4[1,2],K_REP.y],[R4[2,0],R4[2,1],R4[2,2],K_REP.z],[0,0,0,1]])	
		#print T4

		R5 = K_RWR.thetax*R_x(theta[4]) + K_RWR.thetay*R_y(theta[4]) + K_RWR.thetaz*R_z(theta[4])
		T5 = numpy.matrix([[R5[0,0],R5[0,1],R5[0,2],K_RWR.x],[R5[1,0],R5[1,1],R5[1,2],K_RWR.y],[R5[2,0],R5[2,1],R5[2,2],K_RWR.z],[0,0,0,1]])	
		#print T5

		R6 = K_RWP.thetax*R_x(theta[5]) + K_RWP.thetay*R_y(theta[5]) + K_RWP.thetaz*R_z(theta[5])
		T6 = numpy.matrix([[R6[0,0],R6[0,1],R6[0,2],K_RWP.x],[R6[1,0],R6[1,1],R6[1,2],K_RWP.y],[R6[2,0],R6[2,1],R6[2,2],K_RWP.z],[0,0,0,1]])	
		#print T6

		T7 = numpy.matrix([[1,0,0,K_RED.x],[0,1,0,K_RED.y],[0,0,1,K_RED.z],[0,0,0,1]])
		#print T7

		T = T1*T2*T3*T4*T5*T6*T7
		print T
		return T
