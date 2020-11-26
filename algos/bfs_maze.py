#! /usr/bin/env python
# 3.7

from bfs import *
from maze import *
import sys



if __name__ == '__main__':

	m = Maze(20,10)
	print(m)
	MazeNode.quiet_mode = False
	
	nodes = m.get_node_list()
	
	g = Graph()
	for i in nodes:
		# add each maze nodes edges to graph
		if i.u: g.add_edge(i.u, i.u.d)
		if i.d: g.add_edge(i.d, i.d.u)
		if i.l: g.add_edge(i.l, i.l.r)
		if i.r: g.add_edge(i.r, i.r.l)
		
	pprint(g)

	source_node = m.get(0,0)
	
	bfs_result = bfs(g, source_node)
	
	pprint(bfs_result)
	
	print(m)
	
	print(m.get(0,0))
	print("set_1")	
	for i in nodes:
		print(f"n_lev: {i.level}")

	print(m)
	
	print(m)