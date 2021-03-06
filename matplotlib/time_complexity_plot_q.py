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
quasilinear = []
polylogarithmic = []
logn = []
sqrtn = []
nlogn = []
quadratic = []
polynomial = []
polynomial2 = []
exponential = []
exponential2 = []
nsqrd = []
facto = []

combination = []

c_val = 3

#for n in range(3, 50000000, 10000):
#for n in range(3, 1500):
for n in range(3, 150):
    elements.append(n)                  # X-axis
    linear.append(n*10000000)
    #cos.append(math.cos(np.rad2deg(n)) * linear[n-1]) < ERR
    #cos.append(math.cos(np.deg2rad(n)) * linear[n-1])
    quasilinear.append(n**(0.999999) * np.log(n))
    #polylogarithmic.append()
    logn.append(np.log(n))    
    sqrtn.append(np.sqrt(n))    
    nlogn.append(n**(0.999999) * np.log(n))
    polynomial.append(n**(0.999999))
    polynomial2.append(n**(1.000001))
    quadratic.append(n**2)    
    exponential.append((1.000001)**n)
    exponential2.append(n**(np.sqrt(n)))
    #facto.append(math.factorial(n))
    n_f = math.factorial(n)
    nm2_f = 2 * ( math.factorial(n-2) )
    last = c_val    
    c_val = (n_f / nm2_f)
    diff = c_val - last
    print(n, n_f, nm2_f, c_val, diff)
    combination.append(c_val)


plt.xlabel('elements') 
plt.ylabel('operations')
# plt.xscale('log')               # set x scale logarithmic
# plt.yscale('log')               # set y scale logarithmic

#plt.plot(n, cos, label ='Graph of Cosine')
#plt.plot(elements, linear, label ='linear O(n)')
#plt.plot(elements, quasilinear, label ='quasilinear O(n log n)')
#plt.plot(elements, polylogarithmic, label ='polylogarithmic O(n)')
#plt.plot(elements, logn, label ='logarithmic O(log n)')
#plt.plot(elements, sqrtn, label ='root O(root n)')
#plt.plot(elements, nlogn, label ='quasilinear O(n log n)')
#plt.plot(elements, quadratic, label ='quadratic O(n^2)')
#plt.plot(elements, polynomial, label ='polynomial O(n^c)')
#plt.plot(elements, polynomial2, label ='polynomial2 O(n^c)')
#plt.plot(elements, quadratic, label ='quadratic O(n^2)')
#plt.plot(elements, exponential, label ='exponential O(c^n)')
#plt.plot(elements, exponential2, label ='exponential O(c^n)')
plt.plot(elements, combination, label ='nCr')

#plt.plot(n, facto, label ='factorial O(n!)')
plt.grid() 
plt.legend()

plt.show() 