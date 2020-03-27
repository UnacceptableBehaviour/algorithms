#! /usr/bin/env python
# 3.7

from numpy.random import randint
from pprint import pprint
import math

unsorted = []
SIZE_N = 19

for i in range(0, SIZE_N):
    unsorted.append(randint(SIZE_N * 10))

for i in range(0,10):
    lbnd = 2**i
    rbnd = 2**(i+1) - 1
    print(i, "{0:b}".format(lbnd),lbnd, '-', "{0:b}".format(rbnd),rbnd, '-', math.log(lbnd,2), round(math.log(rbnd,2),1), math.floor(math.log(rbnd,2))  )    

print('\n\n')

# A being an array implemnted heap
SPACER = 6
SPACE_TAB = ' ' * SPACER
def display_heap(A):
    depth = math.floor(math.log(len(A),2))  # math.log2(len(A))
    print('depth:',depth)
    
    for row in range(0,depth):
        #print((SPACE_TAB * (ro) )
        lbnd = 2**row
        rbnd = 2**(row+1)
        build_row = ''
        print(f"lbnd:{lbnd} - rbnd{rbnd}")
        
        for node in range(lbnd, rbnd):
            print(node)
            build_row = build_row + str(A[node]).center(SPACER)
        
        print(f"{row} - {build_row}")
    
    return depth
    

display_heap(unsorted)

print('\n\n')

