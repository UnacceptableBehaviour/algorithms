#! /usr/bin/env python
# 3.7

from collections import deque

class BFSResult:
	def __init__(self):
		self.level = {}
		self.parent = {}
	
	def __repr__(self):
		node_str = f'{self.__class__.__name__}          levels - node in level\n'
		for n in self.level.keys():
			node_str += f"{n.name} ".rjust(22)
			try:
				node_str += f"{str(self.level[n])} - {self.parent[n]}"
			except:
				node_str += f"{str(self.level[n])} - None"			
			node_str += "\n"
		return node_str			

class Graph:
	def __init__(self):
		self.adj = {}

	def add_edge(self, u, v):
		#if self.adj[u] is None:
		if u not in self.adj:
			self.adj[u] = []
			
		if v not in self.adj[u]:
			self.adj[u].append(v)
	
	def __repr__(self):
		node_str = f'{self.__class__.__name__}          nodes - adjacency lists\n'
		for n in self.adj.keys():
			node_str += f"{n} ".rjust(22)
			node_str += ','.join([item.name for item in self.adj[n]])
			node_str += "\n"
		return node_str

# Matrix representation
#   A B C D E
# A 1 1 
# B
# C
# D
# E


class Node:
	def __init__(self, name):
		self.name = name
	def __repr__(self):					# so networkx displays meaningful name on the node!
		return self.name

def bfs(g, s):
	'''
	Queue-based implementation of BFS.		
	Args:
	g: a graph with adjacency list adj such that g.adj[u] is a list of u's
	neighbors.
	s: source.
	'''
	r = BFSResult()
	r.parent = {s: None}
	r.level = {s: 0}
	s.level = 0
	
	queue = deque()
	queue.append(s)

	while queue:
		u = queue.popleft()
		for n in g.adj[u]:
			if n not in r.level:
				r.parent[n] = u
				n.parent = u  					# maze
				r.level[n] = r.level[u] + 1
				n.level = r.level[n] 			# maze
				queue.append(n)

	return r



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
	
	# # create list random names
	# with open(DATAFILE,'r') as f:
	# 	text = f.read()
	# 
	# names = []
	# count = 0
	# for match in re.findall(r'information (.*?) \(', text, flags = re.MULTILINE | re.DOTALL):
	# 	r = random.randint(0,9)
	# 	count += 1
	# 	if r % 5 == 0:
	# 		print(f"{r}- {match}")
	# 		names.append(match)
	# 	if len(names) >30:
	# 		break
	# 		
	# print(count)
	# pprint(names)
	
	# create graph	
	node_names = ['semolina','hazelnut choc','picos blue',
				  'kaffir lime leaves','focaccia','tagliatelle','worcester sauce','maris piper potatoes',
				  'capers','roast lamb leg','salmon','salmon skirt','black fungus','sbs olive spread','scampi',
				  'soho tiger prawns','trout','haricot beans','oregano','xantham gum','octopus','rhubarb',
				  'green tabasco','white twix','cashew nuts','bran flakes','basa','porcinini mushrooms',
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
	bfs_result = bfs(g, source_node)
	
	pprint(bfs_result)
	
	print(f"Start node: {source_node.name}")

	nx.draw(G, with_labels=True) # , font_weight='bold')
	plt.show()
	