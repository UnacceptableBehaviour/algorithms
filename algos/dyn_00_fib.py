#! /usr/bin/env python
# 3.7

from pprint import pprint
from collections import Counter
import timeit

# L19 MIT 6.006 - Dynamic Programing - Fibonacci Series
# F0 = 0
# F1 = 1
# Fn = Fn-1 + Fn-2
# 0 1 2 3 4 5 6 7  8  9  10 11
# 0 1 1 2 3 5 8 13 21 34 55 89 . . . 



# https://docs.python.org/3/library/timeit.html
# https://stackoverflow.com/questions/8220801/how-to-use-timeit-module
# timeit() parameters used with 
#
# timeit.timeit(stmt, setup,timer, number)
#
# stmt:  code you want to measure 
# setup: setup details that need to be executed before stmt
# timer: timer value, timeit() already has a default value set, and we can ignore it.
# number: number of executions to be timed

# Dynamic Programming

# Computing Fibonacci

# Memoized
# function memoizing - TODO - add notes - example code
#@cache
#def get_some_data(from_source, search)
class cache(object):

    def __init__(self, fn):
        self.fn = fn
        self._cache = {}
        functools.update_wrapper(self, fn)

    def __call__(self, *args, **kwargs):
        key = str(args) + str(kwargs)
        if key in self._cache:
            ret = self._cache[key]
        else:
            ret = self._cache[key] = self.fn(*args, **kwargs)

        return ret

    def clear_cache(self):
        self._cache = {}
    
        



# Approches
# Naive - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
call_stack = 0
call_stack_highwatermark = 0
c = Counter()
def fib_naive_i(n):                                
    # instrumentation - - - - - 
    global call_stack, call_stack_highwatermark    
    call_stack += 1
    if call_stack > call_stack_highwatermark:
        call_stack_highwatermark = call_stack
    f = f"n:{n}"                                 
    c.update([f])                                
    tab = '\t' * call_stack                     
    print(f"{tab}{call_stack}-{f}")             
                                                 
    # algo - - - - - 
    if n <= 2: f=1                               
    else:
        f = fib_naive_i(n-1) + fib_naive_i(n-2)
    call_stack -= 1
    return f

def fib_naive(n):                                
    if n <= 2: f=1                               
    else:
        f = fib_naive(n-1) + fib_naive(n-2)
    return f


# Memoized - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
memo = {}
def fib_memo(n):
    if n in memo: return memo[n]
        
    if n <= 2: f=1
    else:
        f = fib_memo(n-1) + fib_memo(n-2)
    memo[n] = f
    return f



# Bottom Up DP Algo - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
dp_fib_dict = {0: 0}
def fib_DP(n):

    for k in range(1, n+1):
        if n <= 2: f=1
        else:
            f = dp_fib_dict[n-2] + dp_fib_dict[n-1]
        dp_fib_dict[n] = f

    return dp_fib_dict[n]



	

if __name__ == '__main__':
    
    # for n in range(20):
    #     print(f"*****fib_naive_i({n}) = {fib_naive_i(n)} ^ ^ ^ Callstack Max:{call_stack_highwatermark}")
    #     call_stack_highwatermark = 0
    #     pprint(c)
    #     c = Counter()
        
        # *****fib_naive_i(19) = 4181 ^ ^ ^ Callstack Max:18
        # Counter({'n:2': 2584,
        #          'n:3': 1597,
        #          'n:1': 1597,
        #          'n:4': 987,
        #          'n:5': 610,
        #          'n:6': 377,
        #          'n:7': 233,
        #          'n:8': 144,
        #          'n:9': 89,
        #          'n:10': 55,
        #          'n:11': 34,
        #          'n:12': 21,
        #          'n:13': 13,
        #          'n:14': 8,
        #          'n:15': 5,
        #          'n:16': 3,
        #          'n:17': 2,
        #          'n:19': 1,
        #          'n:18': 1})        

    for n in range(20):     # grinds to a slow amble at 30, v slow by 36
        print(f"*****fib_naive({n}) = {fib_naive(n)}")
        
    for n in range(20):     # 1200 pops out instantly, 12000 not much slower!  <<<<< CACHING! 1st Prize
        print(f"*****fib_memo({n}) = {fib_memo(n)}")

    for n in range(20):   # 1200 pops out instantly, 12000 about 1 min?
        print(f"*****fib_DP({n}) = {fib_DP(n)}")
        
        
    #print(timeit.timeit(stmt, setup,timer, number))
    
 2222222222   print(timeit.timeit(fib_naive(28), number=1000))
