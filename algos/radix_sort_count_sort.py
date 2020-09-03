#! /usr/bin/env python
# 3.7

import sys
import traceback            # traceback.print_stack(file=sys.stdout) to dump stack trace

from numpy.random import randint
from pprint import pprint
import math

# for visualization
# REF: https://www.pygame.org/docs/ref/pygame.html
import pygame
pygame.init()          # initialize all imported pygame modules
window_size_X = 1200 #640
window_size_Y = 600 #480
screen = pygame.display.set_mode((window_size_X,window_size_Y))

animation_timer = pygame.time.Clock()
print("Set caption")
pygame.display.set_caption("Radix Sort - Visualisation")
    
            
    
def visualise(win, data, data_max):
    global window_size_X, window_size_Y
    #print(f"visualise {win} len:{len(data)} max:{data_max}")

    win.fill((0,0,0))   # paint black
    scale = round(float(window_size_Y) / float(data_max),3)
    # TLHC = 0,0
    
    for x in data:
        #print((x, 0), (x, data[x]))
        pygame.draw.line(win, (255,255,255), (x, window_size_Y), (x, window_size_Y - int(data[x]*scale)))
                
    print(f"visualise {win} len:{len(data)} max:{data_max} - COMPLETE")
    
    


pool_size = 1024
data_pool = [0] * (pool_size)

for i in range(0,pool_size): # 2^11
    #print(i)
    data_pool[i] = i


unsorted = []
# redistribute
while len(data_pool):
    print(len(data_pool))
    if len(data_pool) == 1:
        unsorted.append(data_pool.pop(0))
        break
    unsorted.append(data_pool.pop(randint(0,len(data_pool)-1)))

print(unsorted)    

visualise(screen, unsorted, pool_size-1)
pygame.display.update()

# Using: implementation of count sort & radix sort to test understanding
# counting sort
# create and list of empty lists (base buckets) base 10 - ten buckets, binary 2 buckets
def count_sort(data, digit, base=2):
    pre_sorted = []
    
    # for b in range(0, base): pre_sorted.append([])
    pre_sorted.append([])   # 0's
    pre_sorted.append([])   # 1's
    
    mask = 0x1 << digit

    for i in range(0, len(data)):
        if data[i] & mask:
            pre_sorted[1].append(data[i])
        else:
            pre_sorted[0].append(data[i])
    
    sorted_data = pre_sorted[0]
    sorted_data.extend(pre_sorted[1])
    
    return(sorted_data)

def radix_sort(data, digits, base=2):
    global screen
    
    sorted_data = data
    
    for d in range(0,digits):
        sorted_data = count_sort(sorted_data, d, 2)    
        #visualise(screen, unsorted, pool_size-1)
        
    return sorted_data

new_data = radix_sort(unsorted, 11, 2)    

sorted_data = unsorted
u_no = 0
digit = 0
digits = 11
base = 2

while True:
        # check events queue
    for e in pygame.event.get():
        print(e)
        
        if e.type == pygame.QUIT:
            endLoop = True
    

    
    if digit < digits:
        print(f"digit: {digit}")
        sorted_data = count_sort(sorted_data, digit, base)    
        digit += 1
    
    visualise(screen, sorted_data, pool_size-1)
    
    animation_timer.tick(1) # ~ a_timer.wait(100ms)
    print(f"pygame.display.update > {u_no} <")
    pygame.display.update()
    u_no += 1
    # wait for ctrl-C    


# class Entry:        
#     size_mk = Assoc_Array.INITIAL_BUCKETS
# 
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value            
#         self.hash = None
#         
# 
#     def __str__(self):
#         return ("__str__")
# 
#     def __repr__(self):
#         return ("__repr__")
#     
#     def __hash__(self):
#         # hash calculated
#         if self.hash: return self.hash
#         
#         hash_val = 0
#         print(f"hashing: {self.key}")
#         for byte in bytearray(self.key):
#             hash_val = hash_val + byte
#             print(byte)
#         
#         self.hash = hash_val % Entry.size_mk
#         print(f"hash: {self.hash}")
#                     
#         return self.hash
        

if __name__ == '__main__':
    
    sys.exit(0)   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - EXIT < <

    # for b in bytearray(b'suasage'):
    #     print(b)    
    # key = 'cucumber'
    # for n in key: #.iterbytes():
    #     print(n)    
    # ba = bytearray(key,'utf8')    
    # for b in bytearray(key,'utf8'):
    #     print(b)

    # tpl = (5, 99)
    # print(type(tpl.__class__))
    # print(type(tpl))
    # print(tpl.__class__ == tuple)
    # key, value = tpl
    # print(key, value)
    # 
    # print(len(aa))

