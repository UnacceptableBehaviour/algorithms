#! /usr/bin/env python
# 3.7

import sys
import traceback            # traceback.print_stack(file=sys.stdout) to dump stack trace

from numpy.random import randint
from pprint import pprint
import math

class Node(object):     # sub classing (object) not required in 3.x
    
    def __init__(self, parent=None, lc=None, rc=None, key=None, val=None):
        self.parent = parent        # parent node
        self.lc = lc                # left child
        self.rc = rc                # right child
        self.key = key              # sorting criteria
        self.val = val              # object
        self.depth = None           # depth of node in tree
        self.n = None               # position of node in tree (null nodes are counted)
        
    def __str__(self):                      # print
        return f"{self.key}:{self.depth}"

    # def __unicode__(self):                # pythons 2.x - not needed? for 3.x
    #     return f"{u'{val}'}"

    def __repr__(self):                     # pprint repr()
        #return f"({self.n},{self.depth},{self.key})"
        return f"{self.n}:{self.key}"
    

class BST:
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


    # compare keys
    # if smaller than this node add to the left child (lc),
    # if larger than this node add to right child
    def insert_node(self, node_to_add, node=None,  depth=1):
        if node == None: node = self.root   
        final_depth = depth+1
        
        if node_to_add.key <= node.key:     # go left
            if node.lc:                     # left child exists continue check
                final_depth = self.insert_node(node_to_add, node.lc, final_depth)
            else:                
                node.lc = node_to_add
                node.lc.depth = final_depth                

        if node_to_add.key > node.key:      # go right
            if node.rc:                     # right child exists continue check
                final_depth = self.insert_node(node_to_add, node.rc, final_depth)
            else:                
                node.rc = node_to_add
                node.rc.depth = final_depth
        
        if final_depth > self.tree_depth: self.tree_depth = final_depth
        
        return final_depth

    def is_valid_bst(self, node=None):        
        if node == None: node = self.root
        valid = True

        if node.lc:        
            if node.lc.key <= node.key:     # valid
                valid = self.is_valid_bst(node.lc)
            else:
                valid = False
        
        if node.rc:
            if node.rc.key > node.key:
                valid = self.is_valid_bst(node.rc)
            else:
                valid = False
        
        return valid
        
        
    def add_node(self, node_to_add, node=None,  depth=1):
        final_depth = self.insert_node(node_to_add, node, depth)
        self.tree_size += 1
        return (final_depth, self.tree_size, node_to_add.key)


    # used to display tree
    #
    # this builds an array locating the nodes in the array as in heap numbering
    #
    # decending tree     
    # node numebr = node number shift left then if child was left + 0  right +1
    #                  node_num ** 2     + 0 if left chile or +1 if right child
    #                                                                                       
    #                                      1: 143                                         - 0:4 - 80
    # 
    #                  2: 94                                   3: 28                      - 1:4 - 80
    # 
    #        4: 140              5: 134              6: 10               7: 21            - 2:4 - 80
    # 
    #   8: 140    9: 29    10: 149   11: 127    12: 4     13: 93   14: 116   15: 140      - 3:4 - 80
    LEFT = 0
    RIGHT = 1
    def enum_nodes(self, node, previous_n, left_or_right=LEFT):
        previous_n = previous_n << 1    # next row 1 deeper
        
        if node.lc:                     # left child exists continue numbering
            node.lc.n = previous_n + BST.LEFT
            self.node_enum[node.lc.n] = node.lc
            self.enum_nodes(node.lc, node.lc.n)

        if node.rc:                     # right child exists continue numbering
            node.rc.n = previous_n + BST.RIGHT
            self.node_enum[node.rc.n] = node.rc
            self.enum_nodes(node.rc, node.rc.n)
        

    def init_node_enum(self):
        self.node_enum = [None] * (2 ** self.tree_depth)    # allocate storage,  even for blanks        
        self.node_enum[BST.ROOT_NODE] = self.root           # inserts root node        
        self.enum_nodes(self.root, self.root.n, BST.LEFT)   # insert node refs in appropriate pos [n]

    # tree_size can be accessed directly - dislpay binding uing print
    def numNodes(self):
        return self.tree_size
                        
    SPACER = 5                             # padding around node number
    VERTICAL_SPACE = 0
    def __str__(self):
        tree_as_string =''

        self.init_node_enum()        

        depth = self.tree_depth
        tree_width = 2**(depth-1) * BST.SPACER      
        tree_as_string = f"\ndepth: {depth} - tree_width: {tree_width} - tree_size: {self.tree_size}"
        
        print("__str__")
        #pprint(self.node_enum)             # < < - see nodes & blanks in array
        
        for row in range(0,depth):
            lbnd = 2**row
            rbnd = 2**(row+1)
            build_row = ''
            row_spacer = int(tree_width / (2**row))  # spread nodes evenly
            #print(f"lbnd:{lbnd} - rbnd{rbnd}")
            
            print('\n' * BST.VERTICAL_SPACE)
            for node in range(lbnd, rbnd):
                #print('n:',node)
                if self.node_enum[node]:
                    build_row = build_row + (f"{self.node_enum[node]}").center(row_spacer)
                else:
                    build_row = build_row + (f"-").center(row_spacer)
           
            build_row = build_row.center( tree_width )
            
            #print(f"{build_row}    - {row}:{depth} - {tree_width}")
            print(f"{build_row}")
        
        return tree_as_string        
        

if __name__ == '__main__':

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
    print(f"VALID BST?:{bst.is_valid_bst()}")
    
    
    
    sys.exit(0)   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - EXIT < <
    


