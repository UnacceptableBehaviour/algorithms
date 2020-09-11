#! /usr/bin/env python
# 3.7

import sys
import traceback            # traceback.print_stack(file=sys.stdout) to dump stack trace

from numpy.random import randint
from pprint import pprint
import math

from collections import Counter

# # # interesting way to produce primes - aldo demos setdefault
#
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/
def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}
    
    # The running integer that's checked for primeness
    q = 2
    
    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q
            D[q * q] = [q]
            pprint(D)
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        
        q += 1
#
# # #

# another method for generating primes
def isPrime(n):
    if n < 2 or n % 1 > 0:
        return False
    elif n == 2 or n == 3:
        return True
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True

def getPrimes(value = 1):    
    while True:
        if isPrime(value):
            yield value
        value += 1



# types = "dough, bread, sandwich, sauce, supplement, beverage, snack, breakfast, brunch, homegrown, salad, soup, component, amuse, side, starter, sushi, fish, lightcourse, main, crepe, dessert, p4, cheese, comfort, low_cal, serve_cold, serve_rt, serve_warm, serve_hot"
# 
# sushi = "snack, breakfast, brunch, component, amuse, side, starter, sushi, fish, lightcourse, comfort, low_cal, serve_rt"
# 
# lightcourse = "tapas, meze, snack, brunch, salad, soup, component, amuse, side, starter, fish, lightcourse, crepe, cheese, comfort, low_cal, serve_cold, serve_rt, serve_warm, serve_hot"
# 
# salad = "homegrown, snack, brunch, salad, component, amuse, side, starter, lightcourse, low_cal, serve_rt"
# 
# broth_soup = "brunch, homegrown, salad, soup, amuse, fish, lightcourse, main, comfort, low_cal, serve_warm, serve_hot"
# 
# sauce = "sauce, component, amuse, serve_rt , serve_warm"
# 
# pasta = "pasta, snack, brunch, soup, component, amuse, side, starter, lightcourse, main, comfort, low_cal, serve_warm, serve_hot"
# 
# meal = "brunch, fish, lightcourse, main, comfort, low_cal, serve_cold, serve_rt, serve_warm, serve_hot"
# 
# packed_lunch = "snack, brunch, salad, low_cal, serve_rt"

# Notes on Python Dict
# https://stackoverflow.com/questions/327311/how-are-pythons-built-in-dictionaries-implemented
# https://hg.python.org/cpython/file/52f68c95e025/Include/dictobject.h#l51
# https://hg.python.org/cpython/file/52f68c95e025/Objects/dictobject.c#l296

# MIT 6.006 L8 - 3 methods of Hashing + L9/R9 Karp-Rabin rolling hash
def hash_div(key, m):
    '''
    n - total number of keys
    m - table size - should be > n, prime (minimise collisions), 
    key - key to hash
    Every key in K that shares a common factor with the number of buckets m will be hashed to a
    bucket that is a multiple of this factor.

    Therefore, to minimise collisions, it is important to reduce the number of common factors
    between m and the elements of K. How can this be achieved? By choosing m to be a number that
    has very few factors: IE a prime number.
    CLRS 11.3.1
    '''
    return (key%m)

def hash_mult(key, m):
    '''
    a should be random, odd, and in the range 2^(r-1) < a < 2^r, and NOT close to a power of 2.  
    w number of bits in key range
    m = 2^r (table size)
    CLRS 11.3.2
    '''
    w = (key | 0xFF).bit_length()                       #
    #print(f"bitlength of key({key}) = {w} : {hex(key)}")
    r = int(math.log2(m))
    if r<=0: r=1
    # put it in the middle of the range & bit wise OR it with 1 to make it odd
    # a = ( (2**r) - ((2**r)-(2**(r-1))/2) ) | 1       # a lot of compute
    a = ( (2<<r) - ((2<<r)-(2<<(r-1))>>2) ) | 1         # bitwise shift for power calcs
    print(f"r:{r} bits(key)=w:{w} a:{a} key:{key} m:{m}")
    return ( (a * key) % (2**w) ) >> (w - r)

# 6.046; [CLRS 11.3.3]
def hash_UH():
    return 0

# # # # # #
# # # # # #
# parameter that can be commented in / out to get a feel for collisions
# HASH method: DIV / MULT  (Universal Hash not implements yet)
# TABLE size: outer for loop: no_of_entries
# TABLE size: use PRIME no / or incrementing counter
# Data rage: key_low, key_high

if __name__ == '__main__':

    s = 'well'
    t = 'cardamom donuts go really well as dumplings in a stew'
    
    for i in range(len(t)-len(s)):
        print(f"{i} {t[i]} {s==t[i:i+len(s)]}" )

    print("examine_setdefault")
    p1 = gen_primes()      # hold generator in p1 - I assume this is done to maintain a reference count on the generator object?
    for no_of_primes in range(1,100):
        print(f"prime #{no_of_primes}> - - - - - - - - - - - - - - - - - - - - - - - - \ ")
        print(f"prime #{no_of_primes} = ( {next(p1)} ) - - - - - - - - / \n")
        

    # hold generator in p2 
    p2 = getPrimes()       # START primes from 1
    #p2 = getPrimes(100)   # START primes from 100
    
    print("StartSet")      # search for this in console to find start of output
    collisions = Counter()

    key_low, key_high = 1, 100
    for no_of_entries in range(1,100):
    #for no_of_entries in range(100,200):
        #table_size_m = next(p2)                 # using PRIMES for table size for each run
        table_size_m = no_of_entries            # using incremental numbers
        
        for key in range(key_low, key_high):
            collisions[hash_div(key, table_size_m)] += 1        # DIVISION method
            #collisions[hash_mult(key, table_size_m)] += 1      # MULTIPLICATION method
            
        print(f"m={table_size_m} - collisions keys range: L:{key_low} - H:{key_high}")
        pprint(collisions)
        # store here for matplot
        collisions = Counter()
    
    # use matplot / pillow to save image
    

    
    sys.exit(0)   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - EXIT < <

