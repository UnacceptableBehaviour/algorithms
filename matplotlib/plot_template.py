#! /usr/bin/env python
# 3.7
# time complexity plot
# something not quite right - needs work

import time 
from numpy.random import seed 
from numpy.random import randint
import numpy as np
import matplotlib.pyplot as plt 
import math
from pprint import pprint

from pathlib import Path

IMAGE_SCRATCH = Path('../scratch')    # scratch space not maintained by git
# NOTE to save jpg using matplotlib
#> pip install pillow
# plt.plot([1, 2])
# plt.savefig(IMAGE_SCRATCH.join('image.jpg'))

          
#     start = time.clock() 
#     algorithm_to_time(a) 
#     end = time.clock() 
#     print(len(a), "algorithm took ", end-start)


elements = []
cos = []
zero_2pow_zero = []

SCALE = 40.0

for n in range(0, 720):
    elements.append(n)    
    cos.append(math.cos(np.deg2rad(n)) * SCALE)

#float_range  = np.arange(1, 0.1, -0.1)
#float_range  = np.arange(1, 0.01, -0.01)
#float_range  = np.arange(1, 0.001, -0.001)
float_range  = np.arange(1, 0.0001, -0.0001)
float_range = [round(x, 4) for x in float_range]    # 4 decimal places is enough for fun!
pprint(float_range)

elements = []
for n in float_range:
    #print(n)
    elements.append(n)
    zero_2pow_zero.append(pow(n, n))    # pow(n,n) == n**n
    

plt.xlabel('elements') 
plt.ylabel('operations')
# plt.xscale('log')               # set x scale logarithmic
# plt.yscale('log')               # set y scale logarithmic

#plt.plot(elements, cos, label = "Graph of Cos (n deg to rads)")
plt.plot(elements, zero_2pow_zero, label="Limits n^n n->0 (zero ^ zero)")

plt.grid() 
plt.legend()
plt.savefig( IMAGE_SCRATCH.joinpath('matplot_graph.jpg') )
plt.show()






