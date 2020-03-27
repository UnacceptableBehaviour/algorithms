#! /usr/bin/env python
# 3.7

from numpy.random import randint
from pprint import pprint

unsorted = []
SIZE_N = 100

for i in range(0, SIZE_N):
    unsorted.append(randint(SIZE_N * 10))
    
    
# deque vs list - sidebar
# https://stackoverflow.com/questions/6256983/how-are-deques-in-python-implemented-and-when-are-they-worse-than-lists

# actual sort code
def merge(left,right):
    merged = []
    #print(f"merging: {left} - {right}")
    
    # 
    while(len(left) + len(right) > 0):
        if len(left) == 0:         # grab last value
            merged = merged + right
            break
        if len(right) == 0:
            merged = merged + left
            break
        
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))            
        
    #print('merged:', merged)
    return merged
    

# Q1 what's the stack limit? - how big a list can recursive approach be used for?
#   - auxiliary space
def merge_sort(items_to_sort, n=0):
    print('\n- - - -' + (' -' * n) ,n)
    print(items_to_sort)
    
    if len(items_to_sort) == 1: return items_to_sort
    
    mid = int(len(items_to_sort)/2)
    n += 1
    l_range = slice(0,mid)
    r_range = slice(mid,len(items_to_sort))
    
    print(mid, items_to_sort[l_range])
    print(mid,items_to_sort[r_range])
    
    left, right = items_to_sort[l_range], items_to_sort[r_range]
    
    if len(items_to_sort[l_range]) > 1:      # keep going
        left = merge_sort(items_to_sort[l_range],n)

    if len(items_to_sort[r_range]) > 1:      # keep going
        right = merge_sort(items_to_sort[r_range],n)
    
    #print(type(left), left, type(right), right)
    return merge(left, right)
    
    
print( merge([1],[2]) )
print( merge([3],[2]) )
print( merge([3,3],[2,6]) )

print(merge_sort([8,2,13,4,12,1]))

print("MERGE SORTING RANDOMISED LIST")
print(merge_sort(unsorted))


