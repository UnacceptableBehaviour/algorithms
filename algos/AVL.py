#! /usr/bin/env python
# 3.7

import sys
import traceback            # traceback.print_stack(file=sys.stdout) to dump stack trace

from numpy.random import randint
from pprint import pprint
import math

from binary_search_tree import Node, BST



class AVL_Node(Node):
    
    def __init__(self, parent=None, lc=None, rc=None, key=None, val=None):
        super().__init__(parent, lc, rc, key, val)
    
    def rotate_root_left(self):                  
        new_root =  self.rc                      #        1     
        move_node_to_left_tree = self.rc.lc      #   
                                                 #     -     2  
        if move_node_to_left_tree != None:       #   
            move_node_to_left_tree.parent = self #    -  -  -  3    
        self.rc = move_node_to_left_tree
        
        # make rc new root                       #        2     
        self.parent = new_root                   #   
        new_root.lc = self                       #     1     3  
        new_root.parent = None                   #   
                                                 #    -  -  -  -
        return new_root


    def rotate_root_right(self):
        new_root =  self.lc            
        move_node_to_right_tree = self.lc.rc
        
        if move_node_to_right_tree != None:
            move_node_to_right_tree.parent = self
        self.lc = move_node_to_right_tree
        
        # make rc new root
        self.parent = new_root
        new_root.rc = self          
        new_root.parent = None
        
        return new_root

    # important to remember pointers ALWAYS IN PAIRS!    parent>child   AND   child>parent!!
    def rotate_left(self):
        # right child move up into current node position
        # point parent to right child 
        self.parent.rc = self.rc
        # and vice versa
        self.rc.parent = self.parent

        # temp        
        new_parent = self.rc        
        # remove link to right_child from self
        self.rc = None  # check
        
        # make it parent
        self.parent = new_parent
        new_parent.lc = self
        

    def rotate_right(self):
        # right child move up into current node position
        # point parent to right child
        print(f"RR- P>{self.parent.lc} - PLC>{self.parent.lc} - L>{self.lc} R>{self.rc}")
        self.parent.lc = self.lc
        # and vice versa
        self.lc.parent = self.parent

        # temp        
        new_parent = self.lc        
        # remove link to right_child from self
        self.lc = None  # check
        
        # make it parent
        self.parent = new_parent
        new_parent.rc = self


    def rotate_right_dog_leg(self):         # X -2  right dogleg
        print(f"RR_DL-{self} - L>{self.lc} R>{self.rc}")
        # rotate rc right                   #  \
        self.rc.rotate_right()              #   Y 1
                                            #  /
        # rotate self left                  # Z 0
        self.rotate_left()
        

    def is_right_straight(self): # or right_zig_zag?     # X -2   right_straight
        right_is_straight = False                        #  \
                                                         #   Y -1
        if self.balance == -2 and self.rc.balance == -1: #    \
            right_is_straight = True                     #     Z 0
        
        return right_is_straight

    def rotate_left_dog_leg(self):         #   X 2  right dogleg
        # rotate lc left                   #  /
        self.lc.rotate_left()              # Y -1
                                           #  \
        # rotate self right                #   Z 0
        self.rotate_right()
        

    def is_left_straight(self): # or right_zig_zag?     #     X 2   left_straight
        left_is_straight = False                         #    /
                                                         #   Y 1
        if self.balance == 2 and self.lc.balance == 1:   #  /  
            left_is_straight = True                      # Z 0
        
        return left_is_straight

                
    def set_tree_height(self):
        hl = -1
        hr = -1
        first_unbalanced_node = None
        
        if self.lc:
            hl = self.lc.height
        
        if self.rc:
            hr = self.rc.height
        
        self.height = max(hl,hr) + 1
        self.balance = hl - hr      # if abs(hl - hr) >= 2 unbalance - rotation required
        if abs(self.balance) >= 2:
            first_unbalanced_node = self
                
        print(f"set_hgt: {repr(self)}")
        
        # propagate tree height - check balace on the way
        if self.parent != None:            
            unbalance_upstream = self.parent.set_tree_height()
            if first_unbalanced_node == None:
                first_unbalanced_node = unbalance_upstream
        
        return first_unbalanced_node
    

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
    
    # avl = AVL( AVL_Node(key=rnd_key) )    
    # for i in range(0, SIZE_N +1):
    #     rnd_key = randint(SIZE_N * 10)        
    #     print( avl.add_node(AVL_Node(key=(unbalance + rnd_key))) )
    
    #  requires right rotate
    build_data = [100, 50, 150, 200, 250]
    first_node = AVL_Node(key=build_data.pop(0))
    print("First AVL_Node \ ")
    print(repr(first_node))
    print("First AVL_Node / ")
    avl = AVL( first_node )    
    print(f"AVL:{id(avl)}")
    pprint(build_data)
    
    for i in build_data:                
        print( avl.add_node(AVL_Node(key=i)) )
        
    pprint(avl)
    
    avl.add_node(AVL_Node(key=300))
    pprint(avl)
    
    build_data = [100, 50, 125, 40, 30] #  requires left rotate
    avl = AVL( AVL_Node(key=build_data.pop(0)) )    
    pprint(build_data)
    
    for i in build_data:                
        print( avl.add_node(AVL_Node(key=i)) )
        
    pprint(avl)
    avl.add_node(AVL_Node(key=20))
    avl.add_node(AVL_Node(key=10))
    
                           #2   #1
                           #RL  #RR
    build_data = [100, 50, 150, 200, 175] #, requires 2 rotations
    avl = AVL( AVL_Node(key=build_data.pop(0)) )    
    pprint(build_data)
    
    for i in build_data:                
        print( avl.add_node(AVL_Node(key=i)) )
        
    pprint(avl)
    
    
    print(f"AVL_Nodes:{avl.numNodes}")
    print(f"AVL_Nodes:{avl.numNodes()}")
    print(f"Depth:{avl.tree_depth}")
    print(avl)
    print(f"VALID BST?:{avl.is_valid_bst()}")
    a_node = AVL_Node(key=5)
    print(type(AVL_Node))
    print(AVL_Node.__class__.__name__)
    print(AVL_Node.__class__)
    print(isinstance(a_node,AVL_Node))
    
    print(a_node)
    pprint(a_node)

    build_data = [0, 5, 10, 15, 20] #, requires 2 rotations
    avl = AVL( AVL_Node(key=build_data.pop(0)) )    
    pprint(build_data)
    
    for i in build_data:                
        print( avl.add_node(AVL_Node(key=i)) )
        
    pprint(avl)
    
    diagram_bst = AVL( AVL_Node(key=0) )
    for i in range(5, 65,5):        
        new_node = AVL_Node(key=i)
        diagram_bst.add_node(new_node)

    print(diagram_bst) 

    diagram_bst = AVL( AVL_Node(key=63) )
    for i in range(62, 0,-1):        
        new_node = AVL_Node(key=i)
        diagram_bst.add_node(new_node)

    print(diagram_bst)    
    sys.exit(0)   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - EXIT < <



