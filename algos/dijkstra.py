#! /usr/bin/env python
# 3.7

# https://networkx.org/documentation/stable/tutorial.html
# http://snap.stanford.edu/snappy/index.html
# https://towardsdatascience.com/loading-data-from-openstreetmap-with-python-and-the-overpass-api-513882a27fd0
#
# data sets
# https://snap.stanford.edu/data/

from collections import deque	# simple queue no t prioritised
from Queue import PriorityQueue

# dijsktra pseudo code
# from S0
# enque addacent nodes input min heap (riority Q bytearray distance)
# for node in Q - Q changes use get min
# while nextNode = getmin != None:
# 	for node in nextNode[adjacent]:
# 		d = Compute distance
# 		enque node by distance if
# 			node isinstance not input queue ord distance is less than node input queue

# g - graph 
# S - source node
# T - Target node
def dka(g,S,T):
	pass
			
# 			

if __name__ == '__main__':

	# implement me
	q = deque()
	q.append(("plaice", 70))
	q.append(("cucumber", 15))
	q.append(("seeded dough", 227))
	q.append(("guinea fowl", 193))
	q.append(("radishes", 16))	
	q.append(("sunchokes", 73))
	q.append(("haggis yorkie", 271))
	q.append(("mixed chips", 469))

	print("\n\ndeque()\n")
	for node in range(len(q)):
		print(q.pop())
			
			
	q = PriorityQueue()	
	q.put(("plaice", 70))
	q.put(("cucumber", 15))
	q.put(("seeded dough", 227))
	q.put(("guinea fowl", 193))
	q.put(("radishes", 16))	
	q.put(("sunchokes", 73))
	q.put(("haggis yorkie", 271))
	q.put(("mixed chips", 469))
	
	print("\n\nPriorityQueue() - alphabetical\n")
	while not  q.empty():
		print(q.get())
		
			
	q = PriorityQueue()	
	q.put((70, "plaice"))
	q.put((15, "cucumber"))
	q.put((227, "seeded dough"))
	q.put((193, "guinea fowl"))
	q.put((16, "radishes"))	
	q.put((73, "sunchokes"))
	q.put((271, "haggis yorkie"))
	q.put((469, "mixed chips"))
	
	print("\n\nPriorityQueue() - by cals\n")
	while not  q.empty():
		print(q.get())		