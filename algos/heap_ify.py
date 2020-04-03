#! /usr/bin/env python
# 3.7

from numpy.random import randint
from pprint import pprint
import math

unsorted = []
#SIZE_N = 32
SIZE_N = 21
SIZE_N = 15

# check maths
for i in range(0, SIZE_N +1):               # using array positions 1-SIZE_N+1
    unsorted.append(randint(SIZE_N * 10))   # make algorith code more readable
                                            # easier to understand
ROOT_NODE = 1
SIZE_OF_HEAP = 0
unsorted[SIZE_OF_HEAP] = SIZE_N    # maintain heap size in apex

def heap_size():
    return unsorted[SIZE_OF_HEAP]

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
    

display_heap(unsorted)
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
    #print(f"max_heapify node:{node}")
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

build_max_heap(unsorted)

print('\n\n')
display_heap(unsorted)
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
# insert(x, into set S),  
# get max priority (of set S),  
# extract_max (of set S),  			get max and remove it!
# inc_key(in set S, increase element x's key, to value k)
# and  
# get min priority (of set S),  
# delete, change priority in Q.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# bubble value up through the tree
def swap_with_smaller_parent(node):
    # if parent lower value swap nodes    
    parent = int(node/2)
    
    #print(f"swap_with_smaller_parent node:{node} parent:{parent}")
    
    if unsorted[parent] < unsorted[node]:
        unsorted[parent], unsorted[node] = unsorted[node], unsorted[parent]     # swap nodes
        if parent > 1:
            swap_with_smaller_parent(parent)

# isert value into correct position
# insert in 1st available leaf and bubble up
def insert(value):
    # if there are empty (0) leave insert there first

    found_empty_leaf = False
    # Note for array of **any** size: element A[n/2+1 . . n] are ALL leaves! 
    for i in range(int(len(unsorted)/2)+1,len(unsorted)):   # len(A)/2 first non leaf node
        if unsorted[i] == 0:
            unsorted[i] = value
            found_empty_leaf = True
            swap_from = i
    
    unsorted[SIZE_OF_HEAP] += 1 # or unsorted[SIZE_OF_HEAP] = len(unsorted) - 1   # since unsorted[SIZE_OF_HEAP] holde the heap size!
                
    if found_empty_leaf == False:
        unsorted.append(value)
        swap_from = unsorted[SIZE_OF_HEAP]        
    
    # print('\n\n')
    # display_heap(unsorted)    
    # print(f"unsorted[SIZE_OF_HEAP] {unsorted[SIZE_OF_HEAP]}")
    swap_with_smaller_parent(swap_from)
        
insert(494)
print('\n\n')
display_heap(unsorted)

insert(999)
print('\n\n')
display_heap(unsorted)


def get_max_priority():
    return unsorted[ROOT_NODE]

print('\n\nget_max_priority:', get_max_priority())

#def back_fill_to_node(node=1):  # default back fill to root
    # pick highest node from children
    
    

# extract_max
def pop_max():
    try:
        return_node = unsorted[ROOT_NODE]
        unsorted[SIZE_OF_HEAP] -= 1
    except IndexError: 
        return 0
    
    unsorted[ROOT_NODE] = 0
    max_heapify(unsorted, ROOT_NODE)
    
    # print('\n\nHEAP ARRAY - LEAVES FIRST - size:', len(unsorted), ROOT_NODE, -1)
    # for i in range(ROOT_NODE, len(unsorted)-1):
    #     print(unsorted[i])    
    # print(' - - - ')
    
    return return_node

max_node = pop_max()
while max_node != 0:
    # display_heap(unsorted)
    print('popped max:', max_node)
    max_node = pop_max()

# for i in range(0, 19):          
#     insert(randint(SIZE_N * 100))
# 
# display_heap(unsorted)
# 
# max_node = pop_max()
# while max_node != 0:
#     print(':', max_node, )
#     max_node = pop_max()
#                                 

