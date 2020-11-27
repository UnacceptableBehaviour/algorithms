#! /usr/bin/env python
# 3.7

from collections import deque
from collections.abc import Iterable, Iterator
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

	def add_edge(self, u, v):
		#if self.adj[u] is None:
		if u not in self.adj:
			self.adj[u] = []
			
		if v not in self.adj[u]:
			self.adj[u].append(v)
	
	def neighbors(self, v):
		return self.adj[v]
		
	def __iter__(self) -> NodeIter:			#  -> NodeIter is optional guide to coder & toolchain
		return NodeIter(list(self.adj.keys()))
	
	def __repr__(self):
		node_str = f'{self.__class__.__name__}          nodes - adjacency lists\n'
		for n in self.adj.keys():
			node_str += f"{n.name} ".rjust(22)
			node_str += ','.join([item.name for item in self.adj[n]])
			node_str += "\n"
		return node_str

class Node:
	def __init__(self, name):
		self.name = name
	def __repr__(self):					# so networkx displays meaningful name on the node!
		return self.name

class DFSResult:
	def __init__(self):
		self.parent = {}
		self.start_time = {}
		self.finish_time = {}
		self.edges = {} # Edge classification for directed graph.
		self.order = []
		self.t = 0
		self.components = []
		self.component = 1

	def __repr__(self):
		print('parent')
		pprint(self.parent)
		print('start_time')
		pprint(self.start_time)
		print('finish_time')
		pprint(self.finish_time)
		print('edges')
		pprint(self.edges)
		print('order')
		pprint(self.order)
		return "^ above ^"


def dfs(g):
	results = DFSResult()
	for vertex in g:
		if vertex not in results.parent:
			dfs_visit(g, vertex, results)
			results.components.append(vertex)	# label maze components
			results.component += 1 	 			# w/ numbers
	return results

def dfs_visit(g, v, results, parent = None):
	results.parent[v] = parent
	results.t += 1
	results.start_time[v] = results.t
	v.level = results.component 				# label maze components

	if parent:
		results.edges[(parent, v)] = 'tree'
	
	for n in g.neighbors(v):
		if n not in results.parent: # n is not visited.
			dfs_visit(g, n, results, v)
		elif n not in results.finish_time:
			results.edges[(v, n)] = 'back'
		elif results.start_time[v] < results.start_time[n]:
			results.edges[(v, n)] = 'forward'
		else:
			results.edges[(v, n)] = 'cross'
	
	results.t += 1
	results.finish_time[v] = results.t
	results.order.append(v)


def topological_sort(g):
	dfs_result = dfs(g)
	dfs_result.order.reverse()
	return dfs_result.order




if __name__ == '__main__':
	from pathlib import Path
	from pprint import pprint
	import re
	import random
	DATAFILE = Path('./scratch/food.txt')
	# to draw graph
	import networkx as nx
	# https://github.com/networkx/networkx
	# https://networkx.org/documentation/stable/tutorial.html
	# https://networkx.org/documentation/stable/reference/drawing.html#drawing
	import matplotlib.pyplot as plt
	
	# TODO try
	# https://graph-tool.skewed.de/
	# https://graph-tool.skewed.de/static/doc/quickstart.html
	G = nx.Graph()

	
	# create graph	
	node_names = ['semolina','hazelnut choc','picos blue',
				  'kaffir lime leaves','focaccia','tagliatelle','worcester sauce','maris piper potatoes',
				  'capers','roast lamb leg','salmon','salmon skirt','black fungus','sbs olive spread','scampi',
				  'soho tiger prawns','trout','haricot beans','oregano','xantham gum','octopus','rhubarb',
				  'green tabasco','dark chocolate','cashew nuts','bran flakes','basa','porcinini mushrooms',
				  'haggis','halloumi']
	
	nodes = []
	for i in node_names:
		node_to_add = Node(i) 
		nodes.append(node_to_add)		
		G.add_node(node_to_add)								# graphics representation
	
	C_LOW = 1	# 5
	C_HIGH = 3	# 15
	
	g = Graph()
	for i in nodes:
		# connect each node to at least 5 other nodes
		connections = random.randint(C_LOW,C_HIGH)
		for c in range(connections):
			rand_edge = random.randint(0,len(node_names)-1)
			g.add_edge(i,nodes[rand_edge])
			G.add_edge(i,nodes[rand_edge])					# graphics representation
		
	pprint(g)
	
	source_node = nodes[random.randint(0,len(node_names)-1)]
	
	print("> - - - - - - - - - - - - - - - - S")
	for cnt, vertex in enumerate(g):
		 print(f"{cnt} - {vertex}")
	print("> - - - - - - - - - - - - - - - E")
	
	pprint(g.adj)
	pprint(list(g.adj.keys()))
	k = list(g.adj.keys())
	print(f"Node by key:[{k[10]}] is <{type(k[10])}> adjacent to {g.adj[k[10]]}")
	pprint(g.adj[k[10]])
	
	dfs_result = dfs(g)
	# 
	pprint(dfs_result)
	# 
	print(f"Start node: {source_node.name}")
	# 
	nx.draw(G, with_labels=True) # , font_weight='bold')
	plt.show()
	