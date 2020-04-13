#! /usr/bin/env python
# 3.7

import sys
import traceback            # traceback.print_stack(file=sys.stdout) to dump stack trace

from numpy.random import randint
from pprint import pprint
import math

from binary_search_tree import Node, BST
    

class AVL(BST):
    ROOT_NODE = 1
    
    def __init__(self, node):
        self.root = node            # check type Node - raise if not
        self.root.depth = 1
        self.root.n = BST.ROOT_NODE

        self.tree_size = 1
        self.tree_depth = 1
        
        # for display purposes
        self.node_enum = []                     # create an array of objects
        #self.node_enum[BST.ROOT_NODE] = node


      
        



SIZE_N = 9
# for i in range(0, SIZE_N +1):              
#     print( str(Node(key=randint(SIZE_N * 10))) )
                                           
bst = BST( Node(key=randint(SIZE_N * 10)) )

for i in range(0, SIZE_N +1):              
    print( bst.add_node(Node(key=randint(SIZE_N * 10))) )


pprint(bst)
print(f"Nodes:{bst.numNodes}")
print(f"Nodes:{bst.numNodes()}")
print(f"Depth:{bst.tree_depth}")
print(bst)



sys.exit(0)   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - EXIT < <



