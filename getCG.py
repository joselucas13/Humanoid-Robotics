import numpy as np

# Get Center of Gravity
def getCG(M):
	Tx = 0
	Ty = 0
	a = 0
	x = 0
	y = 0
	k1 = 5
	k2 = 2
	for y in range(0,np.shape(M)[0],k1):
		for x in range(0,np.shape(M)[1],k2):
			if (M[y,x] == 1):
				Tx = Tx + x
				Ty = Ty + y
				a = a + 1
	if (a != 0):
		x = Tx/a
		y = Ty/a
		return(x,y)
	else:
		return(0,0)
