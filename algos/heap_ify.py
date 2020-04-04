#! /usr/bin/env python
# 3.7

import sys
import traceback            # traceback.print_stack(file=sys.stdout) to dump stack trace

from numpy.random import randint
from pprint import pprint
import math

# heap_array = []
# #SIZE_N = 32
# SIZE_N = 15
# 
# 
# # using array positions 1-SIZE_N+1
# # make algorith code more readable
# # easier to understand
# # maintain heap size in apex (position 0 in array)
# ROOT_NODE = 1
# SIZE_OF_HEAP = 0
# # initialize / __init__
# def build_rnd_heap(size):
#     # heap_array = [0] * SIZE_N                     # create list of SIZE_N init to 0
#     for i in range(0, len(heap_array)):             # in case we're reusing large heap
#         heap_array[i] = 0
#     
#     for i in range(ROOT_NODE, size+1):
#         try:
#             heap_array[i] = randint(SIZE_N * 10)
#         except IndexError:
#             heap_array.append(randint(SIZE_N * 10))
#                                                     
#     heap_array[SIZE_OF_HEAP] = size                 
#     
# build_rnd_heap(SIZE_N)


heap_array = []
#SIZE_N = 32
SIZE_N = 21
SIZE_N = 15

for i in range(0, SIZE_N +1):                  # using array positions 1-SIZE_N+1
    heap_array.append(randint(SIZE_N * 10))    # make algorith code more readable
                                               # easier to understand
ROOT_NODE = 1
SIZE_OF_HEAP = 0
heap_array[SIZE_OF_HEAP] = SIZE_N    # maintain heap size in apex

def heap_size():
    return heap_array[SIZE_OF_HEAP]

def inc_heap_size():
    heap_array[SIZE_OF_HEAP] += 1
    return heap_array[SIZE_OF_HEAP]

def dec_heap_size():
    if heap_array[SIZE_OF_HEAP] > 0:
        heap_array[SIZE_OF_HEAP] -= 1
    return heap_array[SIZE_OF_HEAP]

# check maths
# lbnd - left bound: start of treee row
# rbnd - right bound: end item of the row
for i in range(0,10):
    lbnd = 2**i
    rbnd = 2**(i+1) - 1
    print(i, "{0:b}".format(lbnd),lbnd, '-', "{0:b}".format(rbnd),rbnd, '-', math.log(lbnd,2), round(math.log(rbnd,2),1), math.floor(math.log(rbnd,2))  )    

# 0 1 1 - 1 1 - 0.0 0.0 0
# 1 10 2 - 11 3 - 1.0 1.6 1
# 2 100 4 - 111 7 - 2.0 2.8 2
# 3 1000 8 - 1111 15 - 3.0 3.9 3
# 4 10000 16 - 11111 31 - 4.0 5.0 4
# 5 100000 32 - 111111 63 - 5.0 6.0 5
# 6 1000000 64 - 1111111 127 - 6.0 7.0 6
# 7 10000000 128 - 11111111 255 - 7.0 8.0 7
# 8 100000000 256 - 111111111 511 - 8.0 9.0 8
# 9 1000000000 512 - 1111111111 1023 - 9.0 10.0 9

print('\n\n')

# A being an array implemnted heap
SPACER = 10                             # padding around node number
VERTICAL_SPACE = 0
def display_heap(A):
    depth = math.floor(math.log(len(A)-1,2)) +1 # math.log2(len(A))
    heap_width = 2**(depth-1) * SPACER      #heap_width = 2**(depth-1) * SPACER
    print('\ndepth:',depth, 'heap_width:', 2**(depth-1),  heap_width, 'heap_size:', heap_size(), 'len(A):',len(A))
    
    
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
    

display_heap(heap_array)
# depth: 4 heap_width: 8 80 heap_size: 15 len(A): 16
# 
#                                      1: 143                                         - 0:4 - 80
# 
#                  2: 94                                   3: 28                      - 1:4 - 80
# 
#        4: 140              5: 134              6: 10               7: 21            - 2:4 - 80
# 
#   8: 140    9: 29    10: 149   11: 127    12: 4     13: 93   14: 116   15: 140      - 3:4 - 80

#print('\n\n')

# pre-condition of this is that both the left and right children of node are max heaps
# which is why the build_max_heap start with the first node above the leaves since
# the leaves are by definintion sorted max_heaps
#
# navigating heap
# root i=1  
# parent = i/2  
# left child = 2i  
# right child = 2i+1  
def max_heapify(A, node):
    #print(f"max_heapify node:{node} - heap_size:{heap_size()}")
    if node <= 0:
        traceback.print_stack(file=sys.stdout)
        return
    
    try:
        left_child = A[node*2]          # left child
    except IndexError:                  # out of range - node has no children => leaf
        left_child = 0

    try:
        right_child = A[node*2 +1]      # right child
    except IndexError:                  # out of range - node has no children => leaf
        right_child = 0

    if left_child + right_child == 0:      # assumes values are positive or 0
        return                             # both children empty
    
    #print(f"lc:{left_child}")
    #print(f"rc:{right_child}")
    if left_child >= right_child:                       # choose direction - left or right tree
        if left_child > A[node]:                        # swap node with left_child if left_child is larger
            A[node], A[node*2] = A[node*2], A[node]     # swap
            max_heapify(A, node*2)
    else:           
        if right_child > A[node]:            # swap with right_child if right_child is larger            
            A[node*2 +1], A[node] = A[node], A[node*2 +1]
            max_heapify(A, node*2 +1)
    
    
# start at deepest(lowest) non-leaf node
# for a 16 node tree that would be 8
def build_max_heap(A):
    # Note for array of **any** size: element A[n/2+1 . . n] are ALL leaves! 
    for i in range(int(len(A)/2),0,-1):   # len(A)/2 first non leaf node
        #print(i)
        max_heapify(A,i)

build_max_heap(heap_array)

print('\n\n')
display_heap(heap_array)
print('\n\n')
# depth: 4 heap_width: 8 80 heap_size: 15 len(A): 16
# 
#                                      1: 149                                         - 0:4 - 80
# 
#                  2: 143                                  3: 140                     - 1:4 - 80
# 
#        4: 140              5: 134              6: 93               7: 116           - 2:4 - 80
# 
#   8: 140    9: 29     10: 94   11: 127    12: 4     13: 10    14: 28    15: 21      - 3:4 - 80


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# From L4 - Priority Queue
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Implements a set of elements associated with a key - methods:
# insert(x, into set S),                                        DONE
# get max priority (of set S),                                  DONE
# extract_max (of set S),  			get max and remove it!      DONE
# inc_key(in set S, increase element x's key, to value k)       DONE
# and  
# get min priority (of set S),  
# delete, change priority in Q.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# test against lecture notes - SEEMS to work well PROOF?
# bubble value up through the tree - initial idea
def swap_with_smaller_parent(node):
    final_position = node
    # if parent lower value swap nodes
    parent = int(node/2)    
    print(f"swap_with_smaller_parent node:{node} parent:{parent}")

    if parent >= 1:    
        if heap_array[parent] < heap_array[node]:
            heap_array[parent], heap_array[node] = heap_array[node], heap_array[parent]     # swap nodes    
            final_position = swap_with_smaller_parent(parent)
            print(f'swap_with_smaller_parent: {final_position}')
    
    return final_position

# from lecture notes
def swap_with_smaller_parent_max_heap(node):
    final_position = node
    
    # if parent lower value swap nodes    
    parent = int(node/2)
    print(f"swap_with_smaller_parent_MAX_HEAP node:{node} parent:{parent}")
    
    if parent >= 1:
        max_heapify(heap_array, parent)
        final_position = swap_with_smaller_parent_max_heap(parent)
    
    return final_position


# isert value into correct position
# insert in 1st available leaf and bubble up
def insert(value):
    # insert value add end of heap ()
    try:                                    # no memory management so may have already allocated array space
        heap_array[heap_size()+1] = value   # try and see if assigning value works
    except IndexError:
        heap_array.append(value)            # if not append it

    inc_heap_size()
    
    swap_with_smaller_parent_max_heap(heap_size())         # O(n Log n)
    #swap_with_smaller_parent(heap_size())                 # O(n)   # just swap no max_heapify -


print('\n\n')
iv = 49
print(f"insert({iv})")
insert(iv)
display_heap(heap_array)

print('\n\n')
iv = 294        
print(f"insert({iv})")
insert(iv)
display_heap(heap_array)

print('\n\n')
iv = 599
print(f"insert({iv})")
insert(iv)
display_heap(heap_array)

print("\n\n\n - - - - extracting max - - - - - - - - - < <")


def get_max_priority():
    return heap_array[ROOT_NODE]

print('\n\nget_max_priority:', get_max_priority())

    
    
# extract_max
# swap ROOT_NODE with last LEAF
# reduce size of heap (remove last LEAF)
# max_heapify(ROOT_NODE) to reposition leaf inserted at ROOT_NODE
def pop_max():
    return_node = 0
    
    if heap_size() >= 1:        
        return_node = heap_array[ROOT_NODE]                 # get max
        heap_array[ROOT_NODE] = heap_array[heap_size()]     # replace with last LEAF
        heap_array[heap_size()] = 0                         # 'remove' leaf
        dec_heap_size()
        max_heapify(heap_array, ROOT_NODE)                  # sort
        
    return return_node

max_node = pop_max()
print('popped max:', max_node)
while max_node != 0:
    #display_heap(heap_array)    
    max_node = pop_max()
    print('popped max:', max_node)

display_heap(heap_array)

print("\n\n\n - - - - build using insert - - - - - - - - - < <")

for i in range(0, 19):          
    insert(randint(SIZE_N * 100))

display_heap(heap_array)

max_node = pop_max()
print('popped max:', max_node)
while max_node != 0:
    #display_heap(heap_array)    
    max_node = pop_max()
    print('popped max:', max_node)
                                
                                
print("\n\n\n - - - - increase a node key - - - - - - - - - < <")                                

def inc_key(node, value):
    final_position = -1
    
    if value > 0:
        if node >= 1 and node <= heap_size():
            heap_array[node] = value
            
            # correct - doesn't stop after finding correct position keeps going to top - returns 1 as final position
            # a lot of extra work! :/
            #final_position = swap_with_smaller_parent_max_heap(node)
            
            # correct - stops after finding correct position - returns tt position            
            final_position = swap_with_smaller_parent(node)
            
    return final_position

# rebuild fresh heap
heap_array = []
for i in range(0, SIZE_N +1):              
    heap_array.append(randint(SIZE_N * 10))
heap_array[SIZE_OF_HEAP] = SIZE_N
build_max_heap(heap_array)
display_heap(heap_array)

target_node = 11
new_value = 99
print(f'\ninc_key({target_node}, {new_value})')

fin_pos = inc_key(target_node, new_value)

display_heap(heap_array)

print(f'\ninc_key({target_node}, {new_value}) final position = {fin_pos}')

sys.exit(0)   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - EXIT < <