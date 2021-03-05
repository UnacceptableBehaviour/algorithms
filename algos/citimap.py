#! /usr/bin/env python
# 3.7

from dijkstra import dijkstra, Node, Graph

import sys
import traceback			# traceback.print_stack(file=sys.stdout) to dump stack trace
import time

import matplotlib
import matplotlib.pyplot as plt	 # diagnostics
from pprint import pprint


from numpy.random import randint
from pprint import pprint
import math

welcome_msg ='''
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  Right click to REGENERATE GRAPH

  Left click on 2 different nodes to run Dijkstra on the network

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
'''

print(welcome_msg)

# REF: https://www.pygame.org/docs/ref/pygame.html
import pygame
pygame.init()		  # initialize all imported pygame modules
import pygame.freetype
pygame.freetype.init()
NODE_FONT = pygame.freetype.SysFont('Monaco', 10)
PATH_FONT = pygame.freetype.SysFont('Monaco', 14)
LEFT_MB = 1
MIDDLE_MB = 2
RIGHT_MB = 3
SCROLL_UP_MB = 4
SCROLL_DN_MB = 5
ROUTE_COLS = {
		'line': (255, 0, 0),
		'dot':  (190, 10, 10),
		'font': (150, 210, 50),
	}

EDGE_LIST_COLS = {
		'line': (255, 235, 75),
		'dot':  (0, 0, 0),
		'font': (255, 235, 175),
	}

window_size_X = 1200
window_size_Y = 700

screen = pygame.display.set_mode((window_size_X,window_size_Y))
pygame.display.set_caption("Random Map Generator")

animation_timer = pygame.time.Clock()

# build citymap
from queue import PriorityQueue


def generate_list_of_connected_nodes(num_nodes, connections):
	nodes = []
	for n in range(num_nodes):
		x = randint(window_size_X)
		y = randint(window_size_Y)
		p = randint(10000000)
		nodes.append(Node(f"{x}_{y}",x,y,p))
	# 					# O(V**2) - but we're jsut building test data.
	# 					# could divide into regions for bigger data
	for from_node in nodes:
		q = PriorityQueue()
		#print(f"outer {(from_node)}")		
		for to_node in nodes:
			#print(f"inner A {from_node}-{to_node}")
			if id(from_node) == id(to_node): continue
			d = from_node.distance(to_node)
			q.put( (d, to_node) )
			#print(f"inner B {(d, to_node)}")
		# links = int(math.ceil(math.log(from_node.population)))
		# print(f"pop:{from_node.population} - lnk:{links}")
		# for c in range(links):		# get nearest connections
		for c in range(connections):		# get 6 nearest connections
			a_node_tuple = q.get()
			from_node.adj.append(a_node_tuple[1])

	return(nodes)	

def generate_graph_from_node_list(g, nodes):
	for node in nodes:
		for n in node.adj:
			#distance, path_node = n
			#g.add_edge(node, path_node, distance)
			g.add_edge(node, n)
			
	
def recentre(xy, n):
	return (xy[0]-n/2,xy[1]-n/2)

def node_label_pos(xy,dx,dy):
	return (max(xy[0]+dx,0), max(xy[1]+dy,0))  # was return (xy[0]+dx,xy[1]+dy) but FONT NO cope with negative numbers

def line_label_pos(n1,n2,dx=0,dy=0):
	x1,y1 = n1.pos
	x2,y2 = n2.pos
	xl = x1 + ((x2 - x1) / 2)
	yl = y1 + ((y2 - y1) / 2)
	return (xl+dx,yl+dy)

def nearest_node(nodes, pos):
	x,y = pos[0],pos[1]
	mouse_node = Node(f"{x}_{y}",x,y)
	q = PriorityQueue()
	for to_node in nodes:		
		d = mouse_node.distance(to_node)
		q.put( (d, to_node) )
		
	return q.get()[1]

def draw_node_list(win, nodes, citi_dot = 6, colors={}):
	cols = {
		'line': (255, 255, 255),
		'dot':  (190, 10, 10),
		'font': (200, 50, 255),
	}
	cols.update(colors)

	# print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - S-1")	
	# for i in range(len(nodes)):		# get 6 nearest connections
	# 	a_node = nodes[i]
	# 	print(f"a_node: {a_node}")		
	# 	for i in range(len(a_node.adj)):
	# 		print(f"adj_node: {a_node.adj}")
	# print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - E-1")
	
	for node in nodes:
		for adj_node in node.adj:
			#print(f"adj_tup: {adj_tup.__class__}")
			#pprint(adj_tup)
			#                      COLOUR        FROM         TO
			pygame.draw.line(win, cols['line'], node.pos, adj_node.pos)
						
		#               surface  colour                 posision              size
		pygame.draw.ellipse(win, cols['dot'], (recentre(node.pos,citi_dot),(citi_dot,citi_dot)) )			# render node
	
	for node in nodes:
		#               surface  position(dest)          offset    text        colour
		NODE_FONT.render_to(win, node_label_pos(node.pos, 10,-2), node.name, cols['font'])     	# render label



def pairwise(iterable):		# function: generator
	it = iter(iterable)
	a = next(it, None)		# retrieve next item in iterable - or a = next(it) raises StopIteration 

	for b in it:			# continue iterating
		yield (a, b)        # yield a tuple 
		a = b

def plot_route_from_node_list(win, nodes, citi_dot = 6, colors={}):
	cols = {
		'line': (255, 255, 255),
		'dot':  (190, 10, 10),
		'font': (200, 50, 255),
	}
	cols.update(colors)
	
	for node in nodes:
		print(f"node: {node.__class__}")
		pprint(node)
		for adj_node in node.adj:
			print(f"\tadj_node: {adj_node.__class__} - {adj_node}")
	
	for from_node,to_node in pairwise(nodes):

		#                      COLOUR        FROM         TO            WIDTH
		pygame.draw.line(win, cols['line'], from_node.pos, to_node.pos, 2)

		#               surface  colour                 posision              size
		pygame.draw.ellipse(win, cols['dot'], (recentre(from_node.pos,citi_dot),(citi_dot,citi_dot)) )			# render node
						
		#               surface  colour                 posision              size
		pygame.draw.ellipse(win, cols['dot'], (recentre(to_node.pos,citi_dot),(citi_dot,citi_dot)) )			# render node
		
		# distance
		#                 surface  posision                         offset    text                       colour
		PATH_FONT.render_to(win, line_label_pos(from_node, to_node, 0,0), str(to_node.dist_S_to_node), cols['font'])     	# render label		



nodes = None
g = None
number_of_nodes = 20
connections_each = 5

def create_new_nodeset_graph_and_paint(screen, num_of_nodes, connections_per_node):
	global nodes, g
	#nodes = generate_list_of_connected_nodes(260, 5)
	nodes = generate_list_of_connected_nodes(num_of_nodes, connections_per_node)
	#nodes = generate_list_of_connected_nodes(160, 2)
	g = Graph()
	generate_graph_from_node_list(g, nodes)
	
	screen.fill((0,0,0))
	
	draw_node_list(screen, nodes)

	return g

# build network to run dijkstra on 
create_new_nodeset_graph_and_paint(screen, number_of_nodes, connections_each)

endLoop = False
start_node = None
end_node = None
end_next = False

while not endLoop:
	route = None
	checked_edges = []
	# check events queue
	for e in pygame.event.get():
		print(e)
		
		if (e.type == pygame.MOUSEBUTTONUP) and (e.button == LEFT_MB):
			pos = pygame.mouse.get_pos()
			mouse_node = nearest_node(nodes, pos)
			print(f"pos: {pos} - {mouse_node}")
			
			if end_next == False:
				start_node = mouse_node
				end_next = True
				print(f"START NODE SELECTED: {start_node}")
			else:
				end_node = mouse_node 
				end_next = False
				print(f"END NODE SELECTED: {end_node}")
				route = dijkstra(g, start_node, end_node, checked_edges)
		
		if e.type == pygame.MOUSEBUTTONUP and (e.button == RIGHT_MB):
			print("CREATING NEW GRAPH:")
			number_of_nodes = number_of_nodes + 20
			connections_each = connections_each + 1
			create_new_nodeset_graph_and_paint(screen, number_of_nodes, connections_each)

		
		if e.type == pygame.QUIT:
			endLoop = True
		
		if e.type == pygame.VIDEORESIZE:
			window_size_X = e.w
			window_size_Y = e.h
		
	# draw scene
	if route:
		screen.fill((0,0,0))
		draw_node_list(screen, nodes)
		for edge in checked_edges:
			plot_route_from_node_list(screen, edge, 1, EDGE_LIST_COLS)
		# TODO the first distance is 0 means WRONG PATH length info used
		# the path length should match (and exactly over write the yellow path)
		# but they mistmatch
		plot_route_from_node_list(screen, route, 12, ROUTE_COLS)
		route = None
		g.reset_all_nodes_distance_from_source_to_inf()
				
	# limit to 10 FPS
	animation_timer.tick(10) # ~ a_timer.wait(100ms)

	# update display	
	pygame.display.update()

	  





sys.exit(0)   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - EXIT < <

