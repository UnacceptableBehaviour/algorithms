#! /usr/bin/env python
# 3.7

import sys
import traceback            # traceback.print_stack(file=sys.stdout) to dump stack trace

from numpy.random import randint
from pprint import pprint
import math

from binary_search_tree import Node, BST
    

class AVL(BST):
    
    def __init__(self, node):
        super().__init__(node)        # call baseclass ctor


    def add_node(self, node):
        super().add_node(node)
        node.set_tree_height()


if __name__ == '__main__':

    SIZE_N = 9
    
    rnd_key = randint(SIZE_N * 10)                                           
    unbalance = rnd_key            # use this to make all nodes larger than unbalance
    
    avl = AVL( Node(key=rnd_key) )
    
    for i in range(0, SIZE_N +1):
        rnd_key = randint(SIZE_N * 10)
        
        print( avl.add_node(Node(key=(unbalance + rnd_key))) )
    
    
    pprint(avl)
    print(f"Nodes:{avl.numNodes}")
    print(f"Nodes:{avl.numNodes()}")
    print(f"Depth:{avl.tree_depth}")
    print(avl)
    print(f"VALID BST?:{avl.is_valid_bst()}")
    a_node = Node(key=5)
    print(type(Node))
    print(Node.__class__.__name__)
    print(Node.__class__)
    print(isinstance(a_node,Node))
    
    
    
    sys.exit(0)   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - EXIT < <



