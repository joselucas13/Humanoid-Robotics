# from ctypes import *
from ctypes import Structure,c_uint16,c_double,c_ubyte,c_uint32,c_int16

class V_REF(Structure):
    _pack_ = 1
    _fields_ = [("ref",    c_double*1),
		("sim",    c_double*1)]

CHAN_1   = 'example-chan-1'
CHAN_2   = 'example-chan-2'
CHAN_3   = 'example-chan-3'
