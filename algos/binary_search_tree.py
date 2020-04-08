#! /usr/bin/env python
# 3.7

import sys
import traceback            # traceback.print_stack(file=sys.stdout) to dump stack trace

from numpy.random import randint
from pprint import pprint
import math

class Node(object):     # sub classing (object) not required in 3.x
    
    def __init__(self, parent=None, lc=None, rc=None, key=None, val=None):
        self.paren = parent
        self.lc = lc
        self.rc = rc
        self.key = key
        self.val = val
        self.depth = None
        
    def __str__(self):
        #return f"{self.key}:{self.val}:{self.depth}"
        return f"{self.key}:{self.depth}"

    def __unicode__(self):
        return f"{u'{val}'}"

    def __repr__(self):
        return (key, val)
    

class BST:
    
    def __init__(self, node):
        self.root = node
        self.tree_size = 1

    def numNodes(self):
        return self.tree_size
        
    def __str__(self):
        return str(self.root)



SIZE_N = 15

for i in range(0, SIZE_N +1):              
    print( str(Node(key=randint(SIZE_N * 10))) )
                                           
    
bst = BST( Node(key=randint(SIZE_N * 10)) )

pprint(bst)
print(f"Nodes:{bst.numNodes}")
print(f"Nodes:{bst.numNodes()}")
print(bst)

sys.exit(0)   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - EXIT < <
# 
# 
# # A being an array implemnted heap
# SPACER = 10                             # padding around node number
# VERTICAL_SPACE = 0
# def display_heap(A):
#     depth = math.floor(math.log(len(A)-1,2)) +1 # math.log2(len(A))
#     heap_width = 2**(depth-1) * SPACER      #heap_width = 2**(depth-1) * SPACER
#     print('\ndepth:',depth, 'heap_width:', 2**(depth-1),  heap_width, 'heap_size:', heap_size(), 'len(A):',len(A))
#     
#     
#     for row in range(0,depth):
#         lbnd = 2**row
#         rbnd = 2**(row+1)
#         build_row = ''
#         row_spacer = int(heap_width / (2**row))  # spread nodes evenly
#         #print(f"lbnd:{lbnd} - rbnd{rbnd}")
#         
#         print('\n' * VERTICAL_SPACE)
#         for node in range(lbnd, rbnd):
#             #print('n:',node)
#             if node >= len(A):
#                 build_row = build_row + (f"{node}: - ").center(row_spacer)
#             else:
#                 build_row = build_row + (f"{node}: {A[node]}").center(row_spacer)
#        
#         build_row = build_row.center( heap_width )
#         
#         print(f"{build_row}    - {row}:{depth} - {heap_width}")
#     
#     return depth
#     
# 
# display_heap(heap_array)