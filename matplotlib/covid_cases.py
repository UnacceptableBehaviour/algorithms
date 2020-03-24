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
from pathlib import Path
import sys
from pprint import pprint
  
CONFIRMED_CASES_CSV = Path('/Users/simon/a_syllabus/repos/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
DEATHS_CSV = Path('/Users/simon/a_syllabus/repos/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
import csv

countries = ['United Kingdom', 'Spain', 'US', 'Italy']

cv_dat = {}
fieldnames = {}
fieldnames_arr = []
    
c = 0
with CONFIRMED_CASES_CSV.open('r') as f:
    csv_data_confirmed = csv.DictReader(f,delimiter=',')

    for counter, fieldname in enumerate(csv_data_confirmed.fieldnames):
        fieldnames_arr.append(fieldname)
        fieldnames[counter] = fieldname
        print(fieldname)

    pprint(fieldnames)

                            # key = country
    for row in csv_data_confirmed:
        spacer = '-'
        if row['Province/State'] == '': spacer = ''
        print(f">{row['Country/Region']}{spacer}{row['Province/State']}<")
        
        cv_dat[f"{row['Country/Region']}{spacer}{row['Province/State']}"] = []
        
        for index,field in fieldnames.items():
            cv_dat[f"{row['Country/Region']}{spacer}{row['Province/State']}"].append(row[field])
        
        
    #     c += 1
    #     if c >4: break
    #     
    # pprint(cv_dat)

#columns = {fieldname: [row.get(fieldname) for row in reader] for fieldname in reader.fieldnames}

for country in countries:
    pprint(cv_dat[country])

pprint(fieldnames)




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
it_population = 60500000    # 60.5M
it_area = 301300            # km^2
es_population = 46660000    # 46.66M
es_area = 506000            # km^2
us_population = 327200000   # 327.2M
us_area = 9834000           # km^2
uk_population = 66400000    # 66.4M
uk_area = 243000            # km^2

dates = []
us_d = []
ddx_us_d = []

for n in range(4, len(cv_dat['US'])):
    if int(cv_dat['US'][n]) < 15: continue
    dates.append(fieldnames[n])
    us_d.append(int(cv_dat['US'][n]))

    m = n-1
    if n==4: m = 4    
    ddx_us_d.append(int(cv_dat['US'][n]) - int(cv_dat['US'][m]))


pprint(dates)
pprint(us_d)

plt.xlabel('date') 
plt.ylabel('infected')
plt.plot(dates, us_d, label='US')
plt.plot(dates, ddx_us_d, label='USaccel')
#plt.grid() 
plt.legend()
plt.show() 


sys.exit()



dates = []

us_d = []
ddx_us_d = []

for country in countries:
    cnt_d = { country: [] }
    
    
    for n in range(4, len(cv_dat['US'])):
        dates.append(fieldnames[n])
        us_d.append(int(cv_dat['US'][n]))
        try:
            ddx_us_d.append(int(cv_dat['US'][n+1]) - int(cv_dat['US'][n]))
        except:
            pass









for n in range(1, 1500):
    elements.append(n)
    linear.append(n)
    #cos.append(math.cos(np.rad2deg(n)) * linear[n-1])
    cos.append(math.cos(np.deg2rad(n)) * linear[n-1])
    logn.append(np.log(n))
    nlogn.append(n * np.log(n))
    quadratic.append(n*n)
    #facto.append(math.factorial(n))


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