#! /usr/bin/env python
# 3.7

from pprint import pprint
from collections import Counter
import timeit

# R19 MIT 6.006 - Dynamic Programing - Shorest Path
# https://courses.csail.mit.edu/6.006/fall11/rec/rec19.pdf
# https://courses.csail.mit.edu/6.006/spring11/lectures/lec18.pdf

# In the following Python implementation, we do not transform the graph.
# We just use the tuple (k, v) as the key in the dictionaries for memoization.




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


class ShortestPathResult(object):
    def __init__(self):
        self.d = {}
        self.parent = {}

def shortest_path(graph, s):
    '''Single source shortest paths using DP on a DAG.
    Args:
        graph: weighted DAG.
        s: source
    '''
    result = ShortestPathResult()
    result.d[s] = 0
    result.parent[s] = None

    for v in graph.itervertices():
        sp_dp(graph, v, result)
        
    return result

def sp_dp(graph, v, result):
    '''Recursion on finding the shortest path to v.    
    Args:
        graph: weighted DAG.
        v: a vertex in graph.
    result: for memoization and keeping track of the result.
    '''
    if v in result.d:
        return result.d[v]

    result.d[v] = float('inf')
    result.parent[v] = None

    for u in graph.inverse_neighbors(v): # Theta(indegree(v))
        new_distance = sp_dp(graph, u, result) + graph.weight(u, v)

        if new_distance < result.d[v]:
            result.d[v] = new_distance
            result.parent[v] = u
    return result.d[v]


def shortest_path_bottomup(graph, s):
    '''Bottom-up DP for finding single source shortest paths on a DAG.    
    Args:
        graph: weighted DAG.
        s: source
    '''
    order = topological_sort(graph)
    result = ShortestPathResult()
    
    for v in graph.itervertices():
        result.d[v] = float('inf')
        result.parent[v] = None
    result.d[s] = 0

    for v in order:
        for w in graph.neighbors(v):
            new_distance = result.d[v] + graph.weight(v, w)
            if result.d[w] > new_distance:
                result.d[w] = new_distance
                result.parent[w] = v
    return result        
        
        

if __name__ == '__main__':
    
    print("S")
    
