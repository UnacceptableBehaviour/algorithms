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
        
        unbalanced_node = node.set_tree_height()
        print(f">-----> unbalanced_node: {repr(unbalanced_node)}")
        
        print(self)

        while unbalanced_node:
            
            if unbalanced_node.balance <= -2:
                
                if unbalanced_node.parent == None:
                    self.root = unbalanced_node.rotate_root_left()
                    
                elif unbalanced_node.is_right_straight():
                    unbalanced_node.rotate_left()
                    
                else:
                    unbalanced_node.rotate_right_dog_leg()
                            
            elif unbalanced_node.balance >= 2:
                
                if unbalanced_node.parent == None:
                    self.root = unbalanced_node.rotate_root_right()
                    
                elif unbalanced_node.is_left_straight():                    
                    unbalanced_node.rotate_right()

                else:
                    unbalanced_node.rotate_left_dog_leg()                             
                                
            unbalanced_node = unbalanced_node.set_tree_height()
            print(f"w>-----> unbalanced_node: {repr(unbalanced_node)}")
            

    def __repr__(self):
        print(f"__repr__AVL:{id(self)}")
        return super().__repr__()
        

if __name__ == '__main__':

    SIZE_N = 9
    
    rnd_key = randint(SIZE_N * 10)                                           
    unbalance = rnd_key            # use this to make all nodes larger than unbalance
    
    # avl = AVL( Node(key=rnd_key) )    
    # for i in range(0, SIZE_N +1):
    #     rnd_key = randint(SIZE_N * 10)        
    #     print( avl.add_node(Node(key=(unbalance + rnd_key))) )
    
    #  requires right rotate
    build_data = [100, 50, 150, 200, 250]
    first_node = Node(key=build_data.pop(0))
    print("First Node \ ")
    print(repr(first_node))
    print("First Node / ")
    avl = AVL( first_node )    
    print(f"AVL:{id(avl)}")
    pprint(build_data)
    
    for i in build_data:                
        print( avl.add_node(Node(key=i)) )
        
    pprint(avl)
    
    avl.add_node(Node(key=300))
    pprint(avl)
    
    build_data = [100, 50, 125, 40, 30] #  requires left rotate
    avl = AVL( Node(key=build_data.pop(0)) )    
    pprint(build_data)
    
    for i in build_data:                
        print( avl.add_node(Node(key=i)) )
        
    pprint(avl)
    avl.add_node(Node(key=20))
    avl.add_node(Node(key=10))
    
                           #2   #1
                           #RL  #RR
    # build_data = [100, 50, 150, 200, 175] #, requires 2 rotations
    # avl = AVL( Node(key=build_data.pop(0)) )    
    # pprint(build_data)
    # 
    # for i in build_data:                
    #     print( avl.add_node(Node(key=i)) )
    #     
    # pprint(avl)
    # 
    
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
    
    print(a_node)
    pprint(a_node)
    
    sys.exit(0)   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - EXIT < <



