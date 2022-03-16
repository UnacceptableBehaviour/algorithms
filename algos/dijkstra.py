#! /usr/bin/env python
# 3.7

# https://networkx.org/documentation/stable/tutorial.html
# http://snap.stanford.edu/snappy/index.html
# https://towardsdatascience.com/loading-data-from-openstreetmap-with-python-and-the-overpass-api-513882a27fd0
#
# data sets
# https://snap.stanford.edu/data/

from collections import deque	# simple queue no t prioritised
from queue import PriorityQueue
from collections.abc import Iterable, Iterator
import math

from pprint import pprint

class NodeIter(Iterator):
	'''
	Iterator to go through ALL graph vertices for DFS
	'''
	def __init__(self, vertices):
		self._index = 0
		self.vertices = vertices

	def __iter__(self):				# use?
		return self
	
	def __next__(self):
		try:
			return_item = self.vertices[self._index]
			self._index += 1
	
		except IndexError:
			raise StopIteration()

		return return_item
	

class Graph(Iterable):
	def __init__(self):
		self.adj = {}

	# nodes connected in BOTH directions
	#def add_edge(self, u, v, distance):
	def add_edge(self, u, v):
		if u not in self.adj:
			self.adj[u] = [v]
		else:
			self.adj[u].append(v)
			
		if v not in self.adj:
			self.adj[v] = [u]
		else:
			self.adj[v].append(u)

	def add_edge_unidirectional(self, u, v):
		if u not in self.adj:
			self.adj[u] = []
			
		if v not in self.adj[u]:
			#self.adj[u].append((distance,v)) #TODO-49 comment in
			self.adj[u].append(v)
	
	def reset_all_nodes_distance_from_source_to_inf(self):
		for node,adj_list in self.adj.items():
			node.dist_S_to_node = math.inf					
	
	def neighbors(self, u):
		return self.adj[u]
		
	def __iter__(self) -> NodeIter:			#  -> NodeIter is optional guide to coder & toolchain
		return NodeIter(list(self.adj.keys()))
	
	def __repr__(self):
		node_str = f'{self.__class__.__name__}		  nodes - adjacency lists\n'
		for n in self.adj.keys():
			node_str += f"{n.name} ".rjust(22)
			#node_str += ','.join([item[1].name for item in self.adj[n]]) #TODO-49 comment in
			node_str += "\n"
		return node_str

class Node:
	def __init__(self, name, x, y, population=1):
		self.name = name
		self.pos = (x, y)
		self.adj = []
		self.population = population
		self.pi = None						# predecessor node - refered to as symbol PI in notes
		self.dist_S_to_node = math.inf		# delta - shortest route - relaxation data

	def distance(self, node):
		#pprint(node)
		x, y = self.pos
		x1, y1 = node.pos
		dx,dy = abs(x-x1), abs(y-y1)
		return( int(math.sqrt((dx*dx)+(dy*dy))) )
	
	def __str__(self):
		return f"{self.name} - {self.dist_S_to_node}"
	
	def __lt__(self, n):
		return(self.dist_S_to_node < n.dist_S_to_node)

	def __gt__(self, n):
		return(self.dist_S_to_node > n.dist_S_to_node)
	
	def __le__(self, n):
		return(self.dist_S_to_node <= n.dist_S_to_node)

	def __ge__(self, n):
		return(self.dist_S_to_node >= n.dist_S_to_node)

	# def __eq__(self, n):
	# 	return(self.dist_S_to_node == n.dist_S_to_node)

	def __repr__(self):					# so networkx displays meaningful name on the node!
		return f"{self.name} - {self.dist_S_to_node}"


# dijsktra pseudo code
# data structures
# graph - hold the vertices w/ edge weights
# PriorityQueue - holds all nodes to be processed prioritising by distance from S
# dict - holds vertices already visited



# g - graph
# q - processing priorityQ
# S - new source -in path
# parent - dict of parent paths
# def djk_processQ(g,q,S,parent):
# 	distanceS, nodeS = S
# 	for adj_node in g.neighbors(nodeS):					# start w/ immediate neighbours
# 		distanceAdj, nodeAdj = adj_node
# 		q.put((distanceS+distanceAdj, nodeAdj))			# reQue node with added distance
# 		if nodeS not in parent:
# 			parent[nodeAdj] = nodeS
# 		

# g - graph 
# S - source node
# T - Target node
# vertex_list - debug / show search
def dijkstra(g,S,T,vertex_list):
	print(f"dijkstra from:{S} to:{T}")	
	path = []
	visited = {}
	
	q = PriorityQueue()
	S.dist_S_to_node = 0					# set start node distance to self
	q.put(S)
	visited[S] = S.dist_S_to_node	
	
	while T not in visited:
		node = q.get()		
		for adj_node in node.adj:
			# calc delta from source to adjacent
			path_weight = node.dist_S_to_node + node.distance(adj_node)
			
			print(f"f:{node}-[{node.dist_S_to_node}] > t:{adj_node}-[{adj_node.dist_S_to_node}] PW:{path_weight} < ADJ_S:{adj_node.dist_S_to_node} = {path_weight < adj_node.dist_S_to_node}")
			
			# if its smaller update - relax
			if path_weight < adj_node.dist_S_to_node:
				adj_node.dist_S_to_node = path_weight
				adj_node.pi = node
				q.put(adj_node)
				vertex_list.append([node, adj_node])
				print(f"\tf:{adj_node}-[{adj_node.dist_S_to_node}] > p:{adj_node.pi}")
		
			visited[adj_node] = adj_node.dist_S_to_node
		
	
	path.append(T)
	parent = T.pi
	while S not in path:
		path.append(parent)
		parent = parent.pi
	
	
	print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - S-D1")	
	print(path)
	print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - E-D1")	
	
	return path
			
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
	while not q.empty():
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
	while not q.empty():
		print(q.get())
		
	q = PriorityQueue()
	n = Node("a", 20,30)
	n.dist_S_to_node = 10
	q.put(n)
	n = Node("b", 20,30)
	n.dist_S_to_node = 1
	q.put(n)
	n = Node("c", 20,30)
	n.dist_S_to_node = 100
	q.put(n)
	n = Node("d", 20,30)
	n.dist_S_to_node = 19
	q.put(n)
	n = Node("e", 20,30)
	n.dist_S_to_node = 99
	q.put(n)
	n = Node("i", 20,30)
	q.put(n)
	print("\n\nPriorityQueue() - node distand from source\n")
	while not q.empty():
		print(q.get())
		
	pairs = [1,2,3,4,5,6,7,8,9]
	print("\n\nIterating a list as consecutive pairs. . .")
	print(f"list = {pairs}")
	
	def pairwise(iterable):		# function: generator
		it = iter(iterable)
		a = next(it, None)		# retrieve next item in iterable - or a = next(it) raises StopIteration 
	
		for b in it:			# continue iterating
			yield (a, b)        # yield a tuple 
			a = b
	
	for tup in pairwise(pairs):
		print(tup)
