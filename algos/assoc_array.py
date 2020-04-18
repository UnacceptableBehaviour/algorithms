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
# assign_or_append: replace a value @ key
# delete: remove a key value pair
# lookup: serach for and retrieve value based on key

class Collision_Chain:
    KEY = 0
    VALUE = 1
    
    def __init__(self, key, value):
        self.collisions = [(key, value)]

    # assign_or_append: replace a value @ key
    def assign_or_append(self, key, value=None):
        if value == None and key.__class__ == tuple:    
            key, value = key                    # allow passing in a tuple instead of key, value
            
        # if i in collision: overwrite          < search - scan
        # else: append kv pair                  < allocate mem        
        for i,kv_pair in enumerate(self.collisions):
            if kv_pair[Collision_Chain.KEY] == key:
                kv_pair[Collision_Chain.VALUE] = value
                return                          # found and assign_or_appended
        
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
        
    def __init__(self): 
        self.entries_n = 0
        self.size_mk = Assoc_Array.INITIAL_BUCKETS
        self.store = [None] * self.size_mk


    # insert: value at key location 
    def insert(self, key, value):
        success = False
        index = self.aa_hash(key)
        
        if self.store[index] == None:      # most likely case if well designed
            self.store[index] = (key, value)
            
        else:                       # overwrite or collision(with a tuple or a chain)
            if self.store[index].__class__ == tuple and self.store[index][0] == key:
                self.store[index][1] == value
                
            elif self.store[index].__class__ == Collision_Chain:
                self.store[index].assign_or_append(key, value)
                
            else:
                chain = Collision_Chain(key, value)         # store collision
                chain.assign_or_append(self.store[index])   # add resident value to chain
                self.store[index] = chain                   # store chain in place

        success = True
        self.entries_n += 1
        
        return success
    
    # assign: replace a value @ key
    # insert does this
    # def assign(key, value):
    #     success = False
    #     return success
            
    # delete: remove a key value pair
    def delete(self, key):
        success = False
        
        success = True
        self.entries_n -= 1
        
        return success
    
    # lookup: serach for and retrieve value based on key
    def get(self, key):        
        index = self.aa_hash(key)
        
        if self.store[index].__class__ == tuple:
            return self.store[index][1]
            
        elif self.store[index].__class__ == Collision_Chain:
            return self.store[index].get(key)
            
        else:        
            raise f"Unknown Error trying to retrive key '{key}'"

    def aa_hash(self, key):        
        hash_val = 0
        
        msg = f"hashing: {key}"
        for byte in bytes(key,'utf8'):
            hash_val = hash_val + byte
        
        hash_val = hash_val % self.size_mk

        print(f"{msg} - hash: {hash_val}")
                    
        return hash_val
        
        
    def __str__(self):
        return ("__str__")

    def __repr__(self):
        rp = f"<{self.__class__} id({id(self)})>\n"
        for i,kv_pair in enumerate(self.store):
            rp = rp + f"[{i}]{repr(kv_pair)}\n"
        
        return rp 
    
    def __len__(self):
        return self.size_mk
    
# class Entry:        
#     size_mk = Assoc_Array.INITIAL_BUCKETS
# 
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value            
#         self.hash = None
#         
# 
#     def __str__(self):
#         return ("__str__")
# 
#     def __repr__(self):
#         return ("__repr__")
#     
#     def __hash__(self):
#         # hash calculated
#         if self.hash: return self.hash
#         
#         hash_val = 0
#         print(f"hashing: {self.key}")
#         for byte in bytearray(self.key):
#             hash_val = hash_val + byte
#             print(byte)
#         
#         self.hash = hash_val % Entry.size_mk
#         print(f"hash: {self.hash}")
#                     
#         return self.hash
        

if __name__ == '__main__':

    # Collision_Chain tests
    collisions = Collision_Chain('banana', 'fruit')
    pprint(collisions)
    
    print(collisions.delete('banana'))
    print(collisions.get('banana'))
    
    collisions.assign_or_append('lamb chop', 'butcher')
    collisions.assign_or_append('cabbage', 'veg')
    collisions.assign_or_append('smoothie', 'drink')    
    
    pprint(collisions)
    
    collisions.delete('cabbage')
    collisions.delete('cabbage')
    
    pprint(collisions)
    
    collisions.assign_or_append('chocolate', 'confectionary')
    collisions.assign_or_append('jelly beans', 'confectionary')
    pprint(collisions)
    
    print(f"get('banana') - {collisions.get('banana')}")
    print(f"get('jelly beans') - {collisions.get('jelly beans')}")
    
    # Assoc_Array
    
    aa = Assoc_Array()
    
    pprint(aa)
    
    aa.insert('lamb chop', 'butcher')    
    pprint(aa)
    
    aa.insert('lamb chop', 'organic butcher')    
    pprint(aa)
    
    aa.insert('cabbage', 'veg')    
    pprint(aa)
    
    aa.insert('chocolate', 'confectionary')    
    pprint(aa)
    
    aa.insert('jelly beans', 'confectionary')
    pprint(aa)

    aa.insert('smoked garlic','herbs n spices')
    pprint(aa)
    aa.insert('bay leaf','herbs n spices')
    pprint(aa)
    aa.insert('chicken makhani','world foods')
    pprint(aa)
    aa.insert('sweet paprika','herbs n spices')
    pprint(aa)
    aa.insert('guinea fowl','poultry')
    pprint(aa)
    aa.insert('kiwi fruit','fruit')
    pprint(aa)
    aa.insert('tomato paste','herbs n spices')
    pprint(aa)
    aa.insert('cocktail beetroot','veg')
    pprint(aa)
    aa.insert('lamb shoulder','butcher')
    pprint(aa)
    
    find = 'jelly beans'
    print(f"{find} = ", aa.get(find))
    find = 'chocolate'
    print(f"{find} = ", aa.get(find))
    find = 'cabbage'
    print(f"{find} = ", aa.get(find))
    find = 'chicken makhani'
    print(f"{find} = ", aa.get(find))
    find = 'kiwi fruit'
    print(f"{find} = ", aa.get(find))
    find = 'lamb chop'
    print(f"{find} = ", aa.get(find))

    
    sys.exit(0)   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - EXIT < <

    # for b in bytearray(b'suasage'):
    #     print(b)    
    # key = 'cucumber'
    # for n in key: #.iterbytes():
    #     print(n)    
    # ba = bytearray(key,'utf8')    
    # for b in bytearray(key,'utf8'):
    #     print(b)

    # tpl = (5, 99)
    # print(type(tpl.__class__))
    # print(type(tpl))
    # print(tpl.__class__ == tuple)
    # key, value = tpl
    # print(key, value)
    # 
    # print(len(aa))

