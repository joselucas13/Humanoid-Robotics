#!/usr/bin/env python

# Homework 4 - ECE 590

# Jose Lucas Gomes Olavo 

import math
import numpy

l1 = 0.24551
l2 = 0.282575
l3 = 0.3127375
l4 = 0.0635

class stru:
    def __init__(self):
        self.x = 0
        self.y = 0
	self.z = 0
	self.thetax = 0
	self.thetay = 0
	self.thetaz = 0

# LEFT SIDE
# K_LSP
K_LSP = stru()
K_LSP.y = l1
K_LSP.thetay = 1

# K_LSR
K_LSR = stru()
K_LSR.thetax = 1

# K_LSY
K_LSY = stru()
K_LSY.thetaz = 1

# K_LEP
K_LEP = stru()
K_LEP.z = -l2
K_LEP.thetay = 1

# K_LWR
K_LWR = stru()
K_LWR.z = -l3
K_LWR.thetaz = 1

# K_LWP
K_LWP = stru()
K_LWP.thetax = 1

# K_LED
K_LED = stru()
K_LED.z = -l4


# RIGHT SIDE
# K_RSP
K_RSP = stru()
K_RSP.y = -l1
K_RSP.thetay = 1

# K_RSR
K_RSR = stru()
K_RSR.thetax = 1

# K_RSY
K_RSY = stru()
K_RSY.thetaz = 1

# K_REP
K_REP = stru()
K_REP.z = -l2
K_REP.thetay = 1

# K_RWR
K_RWR = stru()
K_RWR.z = -l3
K_RWR.thetaz = 1

# K_RWP
K_RWP = stru()
K_RWP.thetax = 1

# K_RED
K_RED = stru()
K_RED.z = -l4

