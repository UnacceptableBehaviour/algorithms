#! /usr/bin/env python
# 3.7

import sys
import traceback			# traceback.print_stack(file=sys.stdout) to dump stack trace
import time

import matplotlib
import matplotlib.pyplot as plt	 # diagnostics
from pprint import pprint


from numpy.random import randint
from pprint import pprint
import math

# REF: https://www.pygame.org/docs/ref/pygame.html
import pygame
pygame.init()		  # initialize all imported pygame modules
import pygame.freetype
pygame.freetype.init()
FONT = pygame.freetype.SysFont('Monaco', 10)

window_size_X = 800 #640
window_size_Y = 600 #480

screen = pygame.display.set_mode((window_size_X,window_size_Y))
pygame.display.set_caption("Random Map Generator")

animation_timer = pygame.time.Clock()


from queue import PriorityQueue
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
		node_str = f'{self.__class__.__name__}		  nodes - adjacency lists\n'
		for n in self.adj.keys():
			node_str += f"{n.name} ".rjust(22)
			node_str += ','.join([item.name for item in self.adj[n]])
			node_str += "\n"
		return node_str

class Node:
	def __init__(self, name, x, y, population=1):
		self.name = name
		self.pos = (x, y)
		self.adj = []
		self.population = population

	def distance(self, node):
		x, y = self.pos
		x1, y1 = node.pos
		dx,dy = abs(x-x1), abs(y-y1)
		return( int(math.sqrt((dx*dx)+(dy*dy))) )
	
	def __str__(self):
		return(self.name)
	
	def __lt__(self, n):
		return(self.population < n.population)

	def __gt__(self, n):
		return(self.population > n.population)
	
	def __le__(self, n):
		return(self.population <= n.population)

	def __ge__(self, n):
		return(self.population >= n.population)

	def __repr__(self):					# so networkx displays meaningful name on the node!
		return self.name

def generate_graph(num_nodes, connections):
	nodes = []
	for n in range(num_nodes):
		x = randint(window_size_X)
		y = randint(window_size_Y)
		nodes.append(Node(f"{x}_{y}",x,y))
	
	q = PriorityQueue()
	for from_node in nodes:
		for to_node in nodes:
			if from_node == to_node: continue	
			d = from_node.distance(to_node)
			#print(f"d:{d}{d.__class__} - node:{to_node}{to_node.__class__}")
			q.put( (d, to_node) )
		print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - S-0")
		pprint(q)		
		for c in range(connections):		# get 6 nearest connections
			a_node = q.get()
			print(f"a_node: {a_node}")
			from_node.adj.append(a_node)
		while not q.empty():
			print(f"r_node: {q.get()}")
		print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - E-0")

	#pprint(nodes)
	return(nodes)	
	
	
def recentre(xy, n):
	return (xy[0]+n/2,xy[1]+n/2)

def label_pos(xy,dx,dy):
	return (xy[0]+dx,xy[1]+dy)


def draw_window(win):
	citi_dot = 6
	
	nodes = generate_graph(260, 5)

	# print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - S-1")	
	# for i in range(len(nodes)):		# get 6 nearest connections
	# 	a_node = nodes[i]
	# 	print(f"a_node: {a_node}")		
	# 	for i in range(len(a_node.adj)):
	# 		print(f"adj_node: {a_node.adj}")
	# print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - E-1")

	win.fill((0,0,0))
	
	for node in nodes:
		for adj_tup in node.adj:
			#print(f"adj_tup: {adj_tup.__class__}")
			#pprint(adj_tup)
			#                      COLOUR                 FROM                         TO
			pygame.draw.line(win, (255,255,255), recentre(node.pos,citi_dot), recentre(adj_tup[1].pos,citi_dot))
						
		#               surface  colour        posision        size
		pygame.draw.ellipse(win, (190,10,10), (node.pos,(citi_dot,citi_dot)) )			# render node
	
	for node in nodes:	
		#           surface  posision          offset  text   colour
		FONT.render_to(win, label_pos(node.pos, 10,-2), node.name, (200, 50, 255))     	# render label
		


endLoop = False

while not endLoop:
		
	# check events queue
	for e in pygame.event.get():
		print(e)
		
		if e.type == pygame.MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()
			bla = input("Check graph - GOOD?")
		
		if e.type == pygame.QUIT:
			endLoop = True
		
		if e.type == pygame.VIDEORESIZE:
			window_size_X = e.w
			window_size_Y = e.h
		
	# draw scene
	draw_window(screen)

	# limit to 10 FPS
	animation_timer.tick(10) # ~ a_timer.wait(100ms)

	# update display	
	pygame.display.update()

	  





sys.exit(0)   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - EXIT < <

