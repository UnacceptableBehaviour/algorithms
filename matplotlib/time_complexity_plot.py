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
  
          
#     start = time.clock() 
#     algorithm_to_time(a) 
#     end = time.clock() 
#     print(len(a), "algorithm took ", end-start)


elements = []
cos = []
linear = []
logn = []
nlogn = []
quadratic = []
nsqrd = []
facto = []


for i in range(1, 1500):
    elements.append(i)
    linear.append(i)
    #cos.append(math.cos(np.rad2deg(i)) * linear[i-1])
    cos.append(math.cos(np.deg2rad(i)) * linear[i-1])
    logn.append(np.log(i))
    nlogn.append(i * np.log(i))
    quadratic.append(i*i)
    #facto.append(math.factorial(i))


plt.xlabel('elements') 
plt.ylabel('operations')
# plt.xscale('log')               # set x scale logarithmic
# plt.yscale('log')               # set y scale logarithmic

#plt.plot(n, cos, label ='Graph of Cosine')
plt.plot(elements, linear, label ='linear O(n)')
plt.plot(elements, logn, label ='logarithmic O(log n)')
plt.plot(elements, nlogn, label ='quasilinear O(n log n)')
#plt.plot(elements, quadratic, label ='quadratic O(n^2)')
#plt.plot(n, facto, label ='factorial O(n!)')
plt.grid() 
plt.legend()

plt.show() 