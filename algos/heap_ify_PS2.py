#! /usr/bin/env python
# 3.7

import sys
import traceback            # traceback.print_stack(file=sys.stdout) to dump stack trace

from numpy.random import randint
from pprint import pprint
import math



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
    print('\ndepth:',depth, 'heap_width:', 2**(depth-1),  heap_width, 'heap_size:', A[0], 'len(A):',len(A))
    
    
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
    

# display_heap(heap_array) - EG output
#
# depth: 4 heap_width: 8 80 heap_size: 15 len(A): 16
# 
#                                      1: 143                                         - 0:4 - 80
# 
#                  2: 94                                   3: 28                      - 1:4 - 80
# 
#        4: 140              5: 134              6: 10               7: 21            - 2:4 - 80
# 
#   8: 140    9: 29    10: 149   11: 127    12: 4     13: 93   14: 116   15: 140      - 3:4 - 80

    

ROOT_NODE = 1
SIZE_OF_HEAP = 0
class PriorityQueue:
    """Array-based priority queue implementation."""
    def __init__(self):
        """Initially empty priority queue."""
        self.heap_array = []
        self.heap_array.append(SIZE_OF_HEAP)    # maintain heap size in apex
        # self.queue = []        
        self.min_index = None
    
    def __len__(self):
        # Number of elements in the queue.
        return self.heap_array[SIZE_OF_HEAP]
        #return len(self.queue)

    def inc_heap_size(self):
        self.heap_array[SIZE_OF_HEAP] += 1        
        return self.heap_array[SIZE_OF_HEAP]
    
    def dec_heap_size(self):
        if self.heap_array[SIZE_OF_HEAP] > 0:
            self.heap_array[self.heap_array[SIZE_OF_HEAP]] = 0    # erase content
            self.heap_array[SIZE_OF_HEAP] -= 1
            
        return self.heap_array[SIZE_OF_HEAP]

    # pre-condition of this is that both the left and right children of node are max heaps
    # which is why the build_max_heap start with the first node above the leaves since
    # the leaves are by definintion sorted max_heaps
    #
    # navigating heap
    # root i=1  
    # parent = i/2  
    # left child = 2i  
    # right child = 2i+1  
    def max_heapify(self, node):
        #print(f"max_heapify node:{node} - heap_size:{heap_size()}")
        if node <= 0:
            traceback.print_stack(file=sys.stdout)
            return
        
        try:
            left_child = self.heap_array[node*2]          # left child
        except IndexError:                  # out of range - node has no children => leaf
            left_child = 0
    
        try:
            right_child = self.heap_array[node*2 +1]      # right child
        except IndexError:                  # out of range - node has no children => leaf
            right_child = 0
    
        if left_child + right_child == 0:      # assumes values are positive or 0
            return                             # both children empty
        
        #print(f"lc:{left_child}")
        #print(f"rc:{right_child}")
        if left_child >= right_child:                       # choose direction - left or right tree
            if left_child > self.heap_array[node]:                        # swap node with left_child if left_child is larger
                self.heap_array[node], self.heap_array[node*2] = self.heap_array[node*2], self.heap_array[node]     # swap
                self.max_heapify(node*2)
        else:           
            if right_child > self.heap_array[node]:            # swap with right_child if right_child is larger            
                self.heap_array[node*2 +1], self.heap_array[node] = self.heap_array[node], self.heap_array[node*2 +1]
                self.max_heapify(node*2 +1)
    


    def swap_with_smaller_parent_max_heap(self, node):
        final_position = node
        
        # if parent lower value swap nodes    
        parent = int(node/2)
        print(f"swap_with_smaller_parent_MAX_HEAP node:{node} parent:{parent}")
        
        if parent >= 1:
            self.max_heapify(parent)
            final_position = self.swap_with_smaller_parent_max_heap(parent)
        
        return final_position
    
    def append(self, value):
        """Inserts an element in the priority queue."""
        if value is None:
            raise ValueError('Cannot insert None in the queue')
        
        # insert value add end of heap ()
        # heap_size() replaced with len(self)
        try:                                         # no memory management so may have already allocated array space
            self.heap_array[len(self)+1] = value     # try and see if assigning value works
        except IndexError:
            self.heap_array.append(value)            # if not append it
    
        self.inc_heap_size()
        
        self.swap_with_smaller_parent_max_heap(len(self))         # O(n Log n)
        # if key is None:
        #     raise ValueError('Cannot insert None in the queue')
        # self.queue.append(key)
        # self.min_index = None
    
    # def find_min():
    # min must be in a leaf node    
    def min(self):
        """The smallest element in the queue."""
        min_val = self.heap_array[ROOT_NODE]
        leaf = ROOT_NODE
        
        # Note for array of **any** size: element A[n/2+1 . . n] are ALL leaves! - We're using 0 to store size
        for i in range(math.ceil(len(self)/2),len(self)+1):
            #print(f"leaf: {i} - {heap_array[i]}")
            if min_val > self.heap_array[i]:
                min_val = self.heap_array[i]
                leaf = i
    
        self.min_index = leaf
        
        #return (leaf, min_val)
        return min_val
        # if len(self.queue) == 0:
        #     return None
        # self._find_min()
        # return self.queue[self.min_index]

    # swap node with last leaf
    # reduce heap size (delete last leaf)
    # max_heapify at node
    def delete_node(self, del_n):                   # TODO
        ret_deleted = None
        try:
            ret_deleted = self.heap_array[del_n]
        except IndexError:
            return ret_deleted
        
        last_leaf = len(self)                       # O(1)
        self.heap_array[del_n] = self.heap_array[last_leaf]   # O(1)
        self.dec_heap_size()                        # O(1)
        self.max_heapify(del_n)                     # O(logn)
        
        return ret_deleted

    
    def pop(self):      #
        """Removes the minimum element in the queue.
    
        Returns:
            The value of the removed element.
        """
        popped_key = None
        if len(self) == 0:
            return popped_key
        
        self.min()
        
        popped_key = self.delete_node(self.min_index)

        return popped_key    
        # if len(self.queue) == 0:
        #     return None
        # self._find_min()
        # popped_key = self.queue.pop(self.min_index)
        # self.min_index = None
        # return popped_key
    
    def _find_min(self):
        # Computes the index of the minimum element in the queue.
        #
        # This method may crash if called when the queue is empty.
        # if self.min_index is not None:
        #     return
        # min = self.queue[0]
        # self.min_index = 0
        # for i in range(1, len(self.queue)):
        #     key = self.queue[i]
        #     if key < min:
        #         min = key
        #         self.min_index = i
        pass


priority_Q = PriorityQueue()
print(f"created - {len(priority_Q)}")

data = [8, 20, 16, 1, 25, 18, 99]
pprint(data)

for e in data:
    print(f"append: {e} - {len(priority_Q)}")
    priority_Q.append(e)
    print(f"done: {e} - {len(priority_Q)}")

display_heap(priority_Q.heap_array)

print(f"priority_Q.min = {priority_Q.min()}")
print(f"len = {len(priority_Q)}")

max_cnt = 0
while (len(priority_Q) > 0):
    e = priority_Q.pop()
    print(e)
    max_cnt += 1
    if max_cnt > 10: break 




                
sys.exit(0)   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - EXIT < <


# 
# 
# class PriorityQueue:
#     """Array-based priority queue implementation."""
#     def __init__(self):
#         """Initially empty priority queue."""
#         self.queue = []
#         self.min_index = None
#     
#     def __len__(self):
#         # Number of elements in the queue.
#         return len(self.queue)
#     
#     def append(self, key):
#         """Inserts an element in the priority queue."""
#         if key is None:
#             raise ValueError('Cannot insert None in the queue')
#         self.queue.append(key)
#         self.min_index = None
#     
#     def min(self):
#         """The smallest element in the queue."""
#         if len(self.queue) == 0:
#             return None
#         self._find_min()
#         return self.queue[self.min_index]
#     
#     def pop(self):
#         """Removes the minimum element in the queue.
#     
#         Returns:
#             The value of the removed element.
#         """
#         if len(self.queue) == 0:
#             return None
#         self._find_min()
#         popped_key = self.queue.pop(self.min_index)
#         self.min_index = None
#         return popped_key
#     
#     def _find_min(self):
#         # Computes the index of the minimum element in the queue.
#         #
#         # This method may crash if called when the queue is empty.
#         if self.min_index is not None:
#             return
#         min = self.queue[0]
#         self.min_index = 0
#         for i in range(1, len(self.queue)):
#             key = self.queue[i]
#             if key < min:
#                 min = key
#                 self.min_index = i
# 
# 
# priority_Q = PriorityQQueue()
# 
# data = [8, 20, 16, 1, 25, 18, 99]
# 
# for e in data:
#     priority_Q.append(e)
# 
# print(f"priority_Q.min = {priority_Q.min()}")
#     
# while (len(priority_Q) > 0):
#     e = priority_Q.pop()
#     print(e)

