#! /usr/bin/env python
# 3.7

import sys
import traceback            # traceback.print_stack(file=sys.stdout) to dump stack trace

from numpy.random import randint
from pprint import pprint
import math

# Using: hash table or a search tree
# 
# insert: value at key location 
# assign: replace a value @ key
# delete: remove a key value pair
# lookup: serach for and retrieve value based on key

class Collision_Chain:
    KEY = 0
    VALUE = 1
    
    def __init__(self, key, value):
        self.collisions = [(key, value)]

    # assign: replace a value @ key
    def assign(self, key, value):
        # if i in collision: overwrite          < search - scan
        # else: append kv pair                  < allocate mem        
        for i,kv_pair in enumerate(self.collisions):
            if kv_pair[Collision_Chain.KEY] == key:
                kv_pair[Collision_Chain.VALUE] = value
                return                          # found and assigned
        
        self.collisions.append((key, value))    # not found append
                        
            
    # delete: remove a key value pair           # EXPENSIVE scan to find, and shift remining by one!
    def delete(self, del_key):
        for i,kv_pair in enumerate(self.collisions):
            if kv_pair[Collision_Chain.KEY] == del_key:
                self.collisions.pop(i)
                return True
        return None
                
    # lookup: serach for and retrieve value based on key
    def get(self, get_key):
        for key,value in self.collisions:       # scan
            if key == get_key:
                return value
        return None
        
    def __str__(self):
        return ("__str__")

    def __repr__(self):
        rp = f"<{self.__class__} id({id(self)})> "
        for key,value in self.collisions:
            rp = rp + f"('{key}', '{value}') "
        return rp
    
    def __len__(self):
        return len(self.collisions)


class Assoc_Array:
    INITIAL_BUCKETS = 11
        
    def __init__(self): # ('lamb chop', 'butcher') ('smoothie', 'drink') ('chocolate', 'confectionary') ('jelly beans', 'confectionary')
        self.entries_n = 0
        self.size_mk = Assoc_Array.INITIAL_BUCKETS
        self.store = [None] * self.size_mk


    # insert: value at key location 
    def insert(key, value):
        success = False
        return success
    
    # assign: replace a value @ key
    def assign(key, value):
        success = False
        return success
            
    # delete: remove a key value pair
    def delete(key):
        success = False
        return success
    
    # lookup: serach for and retrieve value based on key
    def get(key):
        success = False
        return success
        
    def __str__(self):
        return ("__str__")

    def __repr__(self):
        rp = f"<{self.__class__} id({id(self)})>\n"
        for i,kv_pair in enumerate(self.store):
            rp = rp + f"[{i}]{repr(kv_pair)}\n"
        
        return rp 
    
    def __len__(self):
        return self.size_mk
    
class Entry:        
    size_mk = Assoc_Array.INITIAL_BUCKETS

    def __init__(self, key, value):
        self.key = key
        self.value = value            
        self.hash = None
        

    def __str__(self):
        return ("__str__")

    def __repr__(self):
        return ("__repr__")
    
    def __hash__(self):
        # hash calculated
        if self.hash: return self.hash
        
        hash_val = 0
        print(f"hashing: {self.key}")
        for byte in bytearray(self.key):
            hash_val = hash_val + byte
            print(byte)
        
        self.hash = hash_val % Entry.size_mk
        print(f"hash: {self.hash}")
                    
        return self.hash
        

if __name__ == '__main__':

    # Collision_Chain tests
    collisions = Collision_Chain('banana', 'fruit')
    pprint(collisions)
    
    print(collisions.delete('banana'))
    print(collisions.get('banana'))
    
    collisions.assign('lamb chop', 'butcher')
    collisions.assign('cabbage', 'veg')
    collisions.assign('smoothie', 'drink')    
    
    pprint(collisions)
    
    collisions.delete('cabbage')
    collisions.delete('cabbage')
    
    pprint(collisions)
    
    collisions.assign('chocolate', 'confectionary')
    collisions.assign('jelly beans', 'confectionary')
    pprint(collisions)
    
    print(f"get('banana') - {collisions.get('banana')}")
    print(f"get('jelly beans') - {collisions.get('jelly beans')}")
    
    # Assoc_Array
    
    aa = Assoc_Array()
    
    pprint(aa)
    
    sys.exit(0)   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - EXIT < <


