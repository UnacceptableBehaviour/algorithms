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
        #self.depth = None           # depth of node in tree - can be calculated from n
        self.height = 1             # height of subtree inc node
        self.n = None               # position of node in tree (null nodes are counted)
        self.balance = 0
        self.duplicate_key = None   # allow insert of node with same key
                                    # point to duplicate node if needed - linked list
        
    def __str__(self):                      # print
        #return f"[{self.key}:{self.depth}:{self.height},{self.balance}]"
        return f"[{self.key}:{self.n}:{self.height},{self.balance}]"

    # def __unicode__(self):                # pythons 2.x - not needed? for 3.x
    #     return f"{u'{val}'}"

    def __repr__(self):                     # pprint repr()
        #return f"({self.n},{self.depth},{self.key})"
        hl = -1
        hr = -1
        
        if self.lc:
            hl = self.lc.height
        
        if self.rc:
            hr = self.rc.height
            
        #return f"{self.__class__} P:{id(self.parent)} N:{id(self)} LC:{id(self.lc)} RC:{id(self.rc)} K:{self.key} CBal:L-R({hl},{hr}) = H:{self.height},B:{self.balance}"
        return f"{self.__class__} P:{self.parent} N:{self} LC:{self.lc} RC:{self.rc} K:{self.key} CBal:L-R({hl},{hr}) = H:{self.height},B:{self.balance}"
    
    def min(self, dbg=''):
        node = self
        if self.lc != None:
            node = self.lc.min()            
        return node

    def max(self, dbg=''):
        node = self
        if self.rc != None:
            node = self.rc.max()            
        return node
    
    def is_leaf(self):
        return (self.rc is None and self.lc is None)


class BST:
    ROOT_NODE = 1
    
    def __init__(self, node):
        self.root = node            # check type Node - raise if not
        self.root.parent = None
        self.root.height = 1
        self.root.depth = 1
        self.root.n = BST.ROOT_NODE

        self.tree_size = 1
        self.tree_depth = 1
        
        # for display purposes
        self.node_enum = []                     # create an array of objects
        self.narrow_tree = True # False         # narrow tree shows less node info
        #self.node_enum[BST.ROOT_NODE] = node


    # compare keys
    # if smaller than this node add to the left child (lc),
    # if larger than this node add to right child
    # use add_node to insert a node into tree
    # add_node - calls this which then recurses
    def __insert_node(self, node_to_add, node=None,  depth=1):
        if node == None: node = self.root   
        final_depth = depth+1
        
        if node_to_add.key < node.key:      # go left
            if node.lc:                     # left child exists continue check
                final_depth = self.__insert_node(node_to_add, node.lc, final_depth)
            else:                
                node.lc = node_to_add
                node.lc.parent = node
                node.lc.depth = final_depth                

        if node_to_add.key > node.key:      # go right
            if node.rc:                     # right child exists continue check
                final_depth = self.__insert_node(node_to_add, node.rc, final_depth)
            else:                
                node.rc = node_to_add
                node.rc.parent = node
                node.rc.depth = final_depth
        
        if node_to_add.key == node.key:      # store in node.duplicate_key
            node_to_add.parent = node.parent
            node_to_add.rc = node.rc
            node_to_add.lc = node.lc
            node_to_add.depth = node.depth
            # find last node in duplicates list - and insert there
            if node.duplicate_key == None:
                node.duplicate_key = node_to_add
            else:
                next_duplicate_node = node.duplicate_key
                while (type(next_duplicate_node) == Node) and (type(next_duplicate_node.duplicate_key) == Node):
                    next_duplicate_node = next_duplicate_node.duplicate_key
                next_duplicate_node.duplicate_key = node_to_add
        
        if final_depth > self.tree_depth: self.tree_depth = final_depth
        
        return final_depth
                

    def add_node(self, node_to_add, node=None,  depth=1):
        final_depth = self.__insert_node(node_to_add, node, depth)
        self.tree_size += 1
        return (final_depth, self.tree_size, node_to_add.key, node_to_add)

    def find_node(self, node_to_find, node=None):
        if node == None: node = self.root 
        
        if node_to_find.key < node.key:      # go left
            if node.lc:                     # left child exists continue check
                node = self.find_node(node_to_find, node.lc)
            else:                
                return None

        if node_to_find.key > node.key:      # go right
            if node.rc:                     # right child exists continue check
                node = self.find_node(node_to_find, node.rc)
            else:                
                return None
            
        if node_to_find.key == node.key: 
            return node
        
        return None

    # successor - next_larger - next in thr right direction
    # case 1 - node has rc
    # return rc.min
        
    # case 2 - node has no rc (dont care about lc always smaller)
    #        - has rp (left of parent : node == node.parent.left)
    # return parent    
    
    # case 3 - node has no rc or rp
    #        - right of parent : node == node.parent.right
    # go up parent until one has a right parent
    # return that

    # case 3 covers case 2 since the first

    # see R5 35m-42m
    def successor(self, node):
        if node.rc != None:
            return node.rc.min()
        
        if node.parent == node.parent.lc:       # has rp
            return node.parent
        
        current = node
        while current.parent is not None and current is current.parent.rc:        # looking for 1st rp to return
            current = current.parent
        
        return current.parent
    

    def predecessor(self, node):
        if node.lc != None:
            return node.lc.max()
        
        if node.parent == node.parent.lc:       # has lp
            return node.parent
        
        current = node
        while current.parent is not None and current is current.parent.lc:        # looking for 1st lp to return
            current = current.parent
                        
        return current.parent

    # delete(key) see R5 42m - 3 cases to be aware of
    # case 1: leaf
    # 	simply delete
    # 
    # case 2: delete single node with only one sub-tree
    # 	replace parent pointer to node to point at subtree
    # 	straight or zig/zag its the same
    # 
    # case 3: deleting a node that has 2 subtrees
    # 	replace node with successor - smallest element in right subtree
    # 	successor may have a subtree so need to call delete on it first
    # 	replace original deleted node with it
    # 	(from R5-44m50)
    # 
    # 
    # 	running time 
    # 		find key O(h) +
    # 		delete - possible 2 subtrees O(h)
    # 		link swaps constant time O(1)
    # 		= O(h) + O(h) + O(1) = 2 * O(h) + O(1) = O(h)
    
    # find key
    # if leaf? delete - done
    # has one subtree - repoint parent to tree
    # has two subtrees - find successor, call delete on it, insert into tree    
    def delete(self, del_node):
        print(f"- - -delete({del_node.key})")
        node = self.find_node(del_node)                         # O(h) = O(logn)
        print(f"- - -delete found({repr(node)})")
        print(f"- - -       parent:({repr(node.parent)}) PRE")
        
        
        if node.is_leaf():                                      # O(1)
            # has rp (left of parent : node == node.parent.left)            
            if node == node.parent.lc:
                node.parent.lc = None                
            else:
                node.parent.rc = None
            node.parent = None
            print(f"- - -       parent:({repr(node.parent)}) LEAF")
            return node

        # single subtree - point parent at subtree & vice versa
        if node.lc == None or node.rc == None:            
            if node == node.parent.lc:              # this is a left child
                if node.rc == None:
                    node.parent.lc = node.lc        # w/ a left branch
                    node.lc.parent = node.parent
                else:
                    node.parent.lc = node.rc        # w/ a right branch
                    node.rc.parent = node.parent
                    
            else:                                   # this is a right child
                if node.rc == None:
                    node.parent.rc = node.lc        # w/ a left branch
                    node.lc.parent = node.parent
                else:
                    node.parent.rc = node.rc        # w/ a right branch
                    node.rc.parent = node.parent
            
            print(f"- - -       parent:({repr(node.parent)}) 1 SUBTREE")
            return node
        
        # two subtrees - substitute successor for deleted node
        else:
            successor = self.successor(node)
            print(f"- - -       successor:({repr(successor)}) PRE - 2 SUBTREEs")            
            self.delete(successor)
            node.key, successor.key = successor.key, node.key
            print(f"- - -       node:({repr(node)}) POST - 2 SUBTREEs")            
            return successor
            
        
                        

    def is_valid_bst(self, node=None):        
        if node == None: node = self.root
        valid = True

        if node.lc:        
            if node.lc.key < node.key:     # valid
                valid = self.is_valid_bst(node.lc)
            else:
                valid = False
        
        if node.rc:
            if node.rc.key > node.key:
                valid = self.is_valid_bst(node.rc)
            else:
                valid = False
        
        return valid
    
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

        try:
            if node.lc:                     # left child exists continue numbering
                node.lc.n = previous_n + BST.LEFT
                self.node_enum[node.lc.n] = node.lc
                self.enum_nodes(node.lc, node.lc.n)
    
            if node.rc:                     # right child exists continue numbering
                node.rc.n = previous_n + BST.RIGHT
                self.node_enum[node.rc.n] = node.rc
                self.enum_nodes(node.rc, node.rc.n)
        except IndexError as e:
            print(f"idx------:{node.rc}<")
        finally:
            # print('> - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -<S')
            # for i in self.node_enum:
            #     print(f"node_enum[{i}] ")
            #     #print(f"set_hgt: {id(self.parent)}:{id(self)}-{id(self.lc)}-{id(self.rc)} {self.key}-({hl},{hr})={self.height},{self.balance}")
            # print('> - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -<E') 
            pass

    def init_node_enum(self):
        self.node_enum = [None] * (2 ** self.tree_depth)    # allocate storage,  even for blanks        
        self.node_enum[BST.ROOT_NODE] = self.root           # inserts root node        
        self.enum_nodes(self.root, 1, BST.LEFT)             # insert node refs in appropriate pos [n]

    # tree_size can be accessed directly - dislpay binding uing print
    def numNodes(self):
        return self.tree_size
                        
    SPACER = 8                             # padding around node number
    VERTICAL_SPACE = 0
    def __str__(self):
        tree_as_string =''

        self.init_node_enum()        

        depth = self.tree_depth
        if self.narrow_tree:
            tree_width = 2**(depth-1) * 3
        else:
            tree_width = 2**(depth-1) * BST.SPACER
            
        tree_as_string = f"\ndepth: {depth} - tree_width: {tree_width} - tree_size: {self.tree_size}"
        
        print("__str__ TREE representation ascii art")
        print("NODE: " + "[key:tree_n:height,balance] -ve balance RIGHT Heavy")
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
                    if self.narrow_tree:
                        build_row = build_row + (f"{self.node_enum[node].key}").center(row_spacer)
                    else:
                        build_row = build_row + (f"{self.node_enum[node]}").center(row_spacer)
                else:
                    build_row = build_row + (f"-").center(row_spacer)
           
            build_row = build_row.center( tree_width )
            
            #print(f"{build_row}    - {row}:{depth} - {tree_width}")
            print(f"{build_row}")
        
        # print("Raw node_enum:")
        # for i in self.node_enum:
        #     print(i, repr(i))
        print("Tree END _ _ ___________________________________________________________")
        
        return tree_as_string        
        

if __name__ == '__main__':

    SIZE_N = 20
    # for i in range(0, SIZE_N +1):              
    #     print( str(Node(key=randint(SIZE_N * 10))) )
                                               
    #bst = BST( Node(key=randint(SIZE_N * 10)) )
    bst = BST( Node(key=randint(99)) )
    
    node_vals = []
    for i in range(0, SIZE_N +1):
        #new_node = Node(key=randint(SIZE_N * 10))
        new_node = Node(key=randint(99))
        node_vals.append(new_node)
        print( bst.add_node(new_node) )
        print(bst.root.min())
    
    
    # successor predecesor test
    pprint(bst)
    print(f"Nodes:{bst.numNodes}")
    print(f"Nodes:{bst.numNodes()}")
    print(f"Depth:{bst.tree_depth}")
    print(bst)
    #bst.narrow_tree = False
    #print(bst)
    print(f"VALID BST?:{bst.is_valid_bst()}")
    for k in node_vals:
        node = bst.find_node(k)
        print(node.key)
        # successor test
        print(f"successor of {node} - {bst.successor(node)}")
        # predecessor test
        print(f"predecessor of {node} - {bst.predecessor(node)}")

 #                                               67                                               
 # 
 #                       45                                             129                       
 # 
 #           15                      57                     104                     158           
 # 
 #     -           29          -           66          82         116         138         184     
 # 
 #  -     -     17    35    -     -     -     -     77   103    -     -    134   141   175    -   
 # 
 # -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  90 -  -  -  -  -  -  -  -  -  -  -  -  - 
    def reset_bst():
        key_set = [67,45,129,15,57,104,158,29,66,82,116,138,184,17,35,77,103,134,141,175,90]
        
        bst = BST( Node(key=key_set.pop(0)) )
        
        for i in key_set:
            new_node = Node(key=i)
            print( bst.add_node(new_node) )
        
        return bst

    bst = reset_bst()
    print("*** NON random node allocation DELETE test ***")
    print(bst)

    def find_n_show(k):
        node = bst.find_node(Node(key=k))
        print(f"{node}, is_leaf:{node.is_leaf()}")
        print(repr(node))
    
    # is_leaf check
    find_n_show(17)
    find_n_show(35)
    find_n_show(66)
    find_n_show(67)
    find_n_show(57)
    find_n_show(82)
    find_n_show(15)
    
    # delete leaf
    bst.delete(Node(key=17))
    bst.delete(Node(key=35))
    bst.delete(Node(key=29))
    print(bst)
    bst = reset_bst()
    print(bst)
    
    # delete node w single sub-tree
    bst.delete(Node(key=15))        
    print(bst)
    
    bst.delete(Node(key=184))
    print(bst)
    bst.delete(Node(key=175))
    print(bst)    
    bst.delete(Node(key=158))
    print(bst)
    bst.delete(Node(key=129))
    print(bst)
    bst.delete(Node(key=67))
    print(bst)
    
    
    # delete three leaves

    #bst.delete(Node(key=17))
    #bst.delete(Node(key=17))
 
    # diagram_bst = BST( Node(key=0) )
    # for i in range(0, 27):        
    #     new_node = Node(key=i)
    #     diagram_bst.add_node(new_node)
    # 
    # print(diagram_bst)
        
    sys.exit(0)   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - EXIT < <
    


