#! /usr/bin/env python
# 3.7

from dfs import *
from maze import *
import sys



if __name__ == '__main__':

	m = Maze(20,10)
	print(m)
	#MazeNode.quiet_mode = False
	
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
	
	dfs_result = dfs(g)
	
	pprint(dfs_result)
	
	print(m)
	
	pprint(dfs_result.components)