#! /usr/bin/env python
# 3.7

from numpy.random import randint
from pprint import pprint
import math

unsorted = []
SIZE_N = 19
#SIZE_N = 32
SIZE_N = 21

# check maths
for i in range(0, SIZE_N +1):               # using array positions 1-SIZE_N+1
    unsorted.append(randint(SIZE_N * 10))   # make algorith code more readable
                                            # easier to understand

for i in range(0,10):
    lbnd = 2**i
    rbnd = 2**(i+1) - 1
    print(i, "{0:b}".format(lbnd),lbnd, '-', "{0:b}".format(rbnd),rbnd, '-', math.log(lbnd,2), round(math.log(rbnd,2),1), math.floor(math.log(rbnd,2))  )    

print('\n\n')

# A being an array implemnted heap
SPACER = 10                             # padding around node number
VERTICAL_SPACE = 0
def display_heap(A):
    depth = math.floor(math.log(len(A)-1,2)) +1 # math.log2(len(A))
    heap_width = 2**(depth-1) * SPACER      #heap_width = 2**(depth-1) * SPACER
    print('\ndepth:',depth, 'heap_width:', 2**(depth-1),  heap_width, 'len(A):',len(A))
    
    
    for row in range(0,depth):
        lbnd = 2**row
        rbnd = 2**(row+1)
        build_row = ''
        row_spacer = int(heap_width / (2**row))  # spread nodes evenly
        #print(f"lbnd:{lbnd} - rbnd{rbnd}")
        
        print('\n' * VERTICAL_SPACE)
        for node in range(lbnd, rbnd):
            #print('n:',node)
            if node >= len(A):
                build_row = build_row + (f"{node}: - ").center(row_spacer)
            else:
                build_row = build_row + (f"{node}: {A[node]}").center(row_spacer)
       
        build_row = build_row.center( heap_width )
        
        print(f"{build_row}    - {row}:{depth} - {heap_width}")
    
    return depth
    

display_heap(unsorted)

#print('\n\n')

# pre-condition of this is that both the left and right children of node are max heaps
# which is why the build_max_heap start with the first node above the leaves since
# the leaves are by definintion sorted max_heaps
#
# navigating heap
# root i=1  
# parent = i/2  
# left = 2i  
# right = 2i+1  
def max_heapify(A, node):
    try:
        lc = A[node*2]    # left child
        rc = A[node*2 +1] # right child
    except:               # out of range - node has no children => leaf
        return 
    
    if lc >= rc:                    # choose direction
        if lc > A[node]:            # swap with lc if lc is larger
            temp = lc   
            A[node*2] = A[node]
            A[node] = lc
            max_heapify(A, node*2)
    else:           
        if rc > A[node]:            # swap with rc if rc is larger
            temp = rc
            A[node*2 +1] = A[node]
            A[node] = rc
            max_heapify(A, node*2 +1)
    
# max_heapify(unsorted, 8)
# display_heap(unsorted)
# max_heapify(unsorted, 4)
# display_heap(unsorted)
# max_heapify(unsorted, 2)
# display_heap(unsorted)
# print('\n\n')

# start at deepest(lowest) non-leaf node
# for a 16 node tree that would be 8
def build_max_heap(A):
    # Note for array of **any** size: element A[n/2+1 . . n] are ALL leaves! 
    for i in range(int(len(A)/2),0,-1):   # len(A)/2 first non leaf node
        #print(i)
        max_heapify(A,i)

build_max_heap(unsorted)

print('\n\n')
display_heap(unsorted)
print('\n\n')

