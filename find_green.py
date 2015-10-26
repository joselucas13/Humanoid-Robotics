#!/usr/bin/env python

# Homework 5 - ECE 590

# Jose Lucas Gomes Olavo

import numpy as np

p_gh = 255
p_gl = 50

p_bh = 50
p_bl = 0

p_rh = 50
p_rl = 0


# Find Green
def find_green(img):
	k1 = 5
	k2 = 2
	G = np.zeros(shape = (np.shape(img)[0],np.shape(img)[1]))
	for y in range(40,np.shape(img)[0]-180,k1):
		for x in range(0,np.shape(img)[1],k2):
			p = img[y,x]
			if ((p_gh > p[1] > p_gl) and (p_bh > p[0] > p_bl) and (p_rh > p[2] > p_rl)):
				G[y,x] = 1
	return G
