#! /usr/bin/env python
# 3.7

from collections import deque
import random
from pprint import pprint
import os


class MazeNode:
	quiet_mode = True
	
	def __init__(self, name, x, y, u=None,d=None,l=None,r=None):
		self.name = name
		self.u = u
		self.d = d
		self.l = l
		self.r = r
		self.sides = 4 - len([i for i in [u,d,l,r] if i]) # None = wall
		self.x = x
		self.y = y
		self.level = -1
		self.parent = None
		
	def __repr__(self):
		verbose = not MazeNode.quiet_mode
		
		if verbose:
			u = 'None'
			l = 'None'
			r = 'None'
			d = 'None'
			try:
				u = str(self.u.name)
			except:
				pass		
			try:
				l = str(self.l.name)
			except:
				pass		
			try:
				r = str(self.r.name)
			except:
				pass		
			try:	
				d = str(self.d.name)
			except:
				pass

			#	    8 6    				xy-u
			#	7 7  1  9 7	     xy-l   sides   xy-r
			#	   None                 xy-d
			#ascii_image = "\n    "+u+"    "+"\n"+l+f" {str(self.sides).center(3)}"+r+"\n"+"    "+d+"    "
			ascii_image = "\n    "+u+"    "+"\n"+l+f"{str(self.level).center(3)} "+r+"\n"+"    "+d+"    "
			return ascii_image
		
		return str(self.name)


	def add_random_wall(self): # remove
		REMOVE_CELL = 99
		
		available_routes_to_close = []
		if not MazeNode.quiet_mode: print(f"close ({self.x},{self.y})\n{self}")
		# define how to close a link in each direction
		def close_top():
			self.u.d = None
			self.u.sides += 1
			self.u   = None
			self.sides += 1 

		def close_bottom():
			self.d.u = None
			self.d.sides += 1
			self.d   = None
			self.sides += 1
		
		def close_left():
			self.l.r = None
			self.l.sides += 1
			self.l   = None
			self.sides += 1
		
		def close_right():
			self.r.l = None
			self.r.sides += 1
			self.r   = None
			self.sides += 1
			
		# build list of open routes
		if self.u:
			if self.u.sides < 2:	# don't create cells w/ 3 sides
				available_routes_to_close.append(close_top)

		if self.d:
			if self.d.sides < 2:
				available_routes_to_close.append(close_bottom)

		if self.l:
			if self.l.sides < 2:
				available_routes_to_close.append(close_left)

		if self.r:
			if self.r.sides < 2:
				available_routes_to_close.append(close_right)


		if len(available_routes_to_close) > 0:
			# close a random route
			close_wall = random.choice(available_routes_to_close)		
			close_wall()
			if not MazeNode.quiet_mode: print(self)		
			return self.sides
		else:
			# surrounded by cells w/ 2 sides - remove it
			if not MazeNode.quiet_mode: print(self)
			return REMOVE_CELL
		

class Maze:
	MAZE_CELL_SIZE_SML = 3
	MAZE_CELL_SIZE_LRG = 5
	
	def __init__(self, x=10, y=10, quiet_mode=True):
		'''
		TLHC = 0,0 origin
		         xy
		mz = [  [00, 10, 20 . .  ],
			    [01, 11, 21 . .  ],
			    [02, 12, 22 . .  ] ]
		'''
		self.cell_size = Maze.MAZE_CELL_SIZE_LRG
		self.mz = []
		self.mz_art = []
		self.x = x
		self.y = y
		self.quiet_mode = quiet_mode
		MazeNode.quiet_mode = quiet_mode
		for yy in range(self.y):
			self.mz.append([])
			for xx in range(self.x):				
				self.mz[yy].append(MazeNode(f"{str(xx).rjust(2)}{str(yy).rjust(2)}",xx,yy))
				#print(xx,yy,"--",f"{str(xx).rjust(2)}{str(yy).rjust(2)}")
			#pprint(self.mz)
		
		#connect nodes
		for yy in range(self.y):			
			for xx in range(self.x):
				node = self.get(xx,yy)
				node.u = self.get(xx,self.dec_y(yy))
				node.d = self.get(xx,self.inc_y(yy))
				node.l = self.get(self.dec_x(xx),yy)
				node.r = self.get(self.inc_x(xx),yy)
				node.sides = 0
				
		self.create_maze()
		
		self.create_art()

	def cls():
		os.system('cls' if os.name=='nt' else 'clear')

	def create_maze(self):
		'''
		randomly pick a square and add a side
		if adding one more side creates a closed box remove it from target list
		repeat until no targets left
		'''
		flat_maze = [maze_node for row in self.mz for maze_node in row]
		if not self.quiet_mode: print(f"flat_maze len: {len(flat_maze)}")

		# self.get(0,0).add_random_wall()
		# self.get(self.x-1,0).add_random_wall()
		# self.get(self.x-1,self.y-1).add_random_wall()
		# self.get(5,self.y-1).add_random_wall()
		# self.get(5,self.y-1).add_random_wall()
		# self.get(0,self.y-1).add_random_wall()
		
		while len(flat_maze) > 0:
			target_node = random.randint(0, len(flat_maze)-1)
			
			if flat_maze[target_node].sides >= 2:	# cells get set from the 'other side'
				del flat_maze[target_node]
				continue
			
			sides = flat_maze[target_node].add_random_wall()
			if sides >= 2:				
				del flat_maze[target_node]
				if not self.quiet_mode: print(f" - - - - - - nodes_left: {len(flat_maze)}\n")
			
			if not self.quiet_mode:
				Maze.cls()
				self.create_art()
				print(self)
		
	
	def inc_x(self, x):
		x += 1
		return x % self.x

	def dec_x(self, x):
		x -= 1
		if x < 0: x = self.x - 1
		return x

	def inc_y(self, y):
		y += 1
		return y % self.y

	def dec_y(self, y):
		y -= 1
		if y < 0: y = self.y - 1
		return y		
		
	def create_art(self):
		self.mz_art = []
		# build blank art array
		#print(f"create_art: x:{self.x} y:{self.y}")
		for yy in range((self.y * (self.cell_size-1))+1):	# cells overlap by 1
			self.mz_art.append([])
			for xx in range((self.x * (self.cell_size-1))+1):				
				self.mz_art[yy].append(' ')

		for yy in range(self.y):
			for xx in range(self.x):			
				art = self.get_ascii(xx,yy)
				#art = self.get_ascii(xx,yy,True) # debug - place number of side in centre
				self.place_art(xx,yy, art)
		# x = 0
		# y = 0
		# art = self.get_ascii(x,y)
		# self.place_art(x,y, art)
		# x = 19
		# y = 0
		# art = self.get_ascii(x,y)
		# self.place_art(x,y, art)
		# #print
		# x = 0
		# y = 9
		# art = self.get_ascii(x,y)
		# self.place_art(x,y, art)
		# x = 19
		# y = 9
		# art = self.get_ascii(x,y)
		# self.place_art(x,y, art)
		
		
	def place_art(self, x, y, art):
		'''
		over write ascii art with lists in art
		x,y co-ord of maze position
		'''
		xpos = x * (self.cell_size - 1)
		ypos = y * (self.cell_size - 1)
		# print(f"place_art {x}:{xpos},{y}:{ypos}")
		# TODO - generalise to art size y / cell_size
		if self.cell_size == Maze.MAZE_CELL_SIZE_SML:
			self.mz_art[ypos][xpos:xpos+len(art[0])] = art[0]
			self.mz_art[ypos+1][xpos:xpos+len(art[1])] = art[1]
			self.mz_art[ypos+2][xpos:xpos+len(art[2])] = art[2]
		if self.cell_size == Maze.MAZE_CELL_SIZE_LRG:
			self.mz_art[ypos][xpos:xpos+len(art[0])] = art[0]
			self.mz_art[ypos+1][xpos:xpos+len(art[1])] = art[1]
			self.mz_art[ypos+2][xpos:xpos+len(art[2])] = art[2]
			self.mz_art[ypos+3][xpos:xpos+len(art[3])] = art[3]
			self.mz_art[ypos+4][xpos:xpos+len(art[4])] = art[4]
			
	def get(self,x,y):
		return self.mz[y][x]		

	def get_node_list(self):
		return [maze_node for row in self.mz for maze_node in row]
	
	def get_ascii(self,x,y, dbg=False):
		node = self.get(x,y)
		stud = '@'		
		blank = ' '
		#print(f"get_ascii lev: {node.level} - {node.__class__.__name__} \n {node}")
		
		if self.cell_size == 3:		
			if dbg:
				cpoint = str(node.sides)
			else:
				#cpoint = blank
				cpoint = str(node.level)[0]
				
			cell_art = [[stud, stud, stud],
						[stud, cpoint, stud],
						[stud, stud, stud] ]		
			if node.u: cell_art[0][1] = blank
			if node.d: cell_art[2][1] = blank
			if node.l: cell_art[1][0] = blank
			if node.r: cell_art[1][2] = blank
		else: # 5
			if dbg:
				cpoint = str(node.sides)
			else:
				#cpoint = blank
				cpoint = str(node.level)				
				
			cell_art = [[stud, stud, stud, stud, stud],
						[stud, blank, blank, blank, stud],
						[stud, blank, cpoint, blank, stud],
						[stud, blank, blank, blank, stud],
						[stud, stud, stud, stud, stud] ]		
			if node.u: cell_art[0][1:4] = [blank,blank,blank]
			if node.d: cell_art[4][1:4] = [blank,blank,blank]
			if node.l:
				cell_art[1][0] = blank
				cell_art[2][0] = blank
				cell_art[3][0] = blank
			if node.r:
				cell_art[1][4] = blank
				cell_art[2][4] = blank
				cell_art[3][4] = blank
			if len(cpoint) >1:
				cell_art[2][2] = cpoint[0]
				cell_art[2][3] = cpoint[1]
		
		
		return cell_art
	

	def __repr__(self):
		'''
		cell four corners & 4 ports
		* *     ***     * *
		        *       * *
		* *     * *     * *
		'''
		self.create_art()		
		maze_str = f'{self.__class__.__name__}\n'
		maze_str += '   .123456789.123456789.123456789.123456789.123456789\n'
		# for yy in range(self.y):
		# 	for xx in range(self.x):				
		# 		#maze_str += f"{self.get(xx,yy)} "
		# 		maze_str += ''.join(self.mz_art[yy])
		# 	maze_str += '\n'
		cnt = 0
		for yy in range(len(self.mz_art)):
			maze_str += str(cnt).rjust(2)+' '+''.join(self.mz_art[yy])
			maze_str += '\n'
			cnt+=1
		if self.quiet_mode: Maze.cls()
		return maze_str



if __name__ == '__main__':

	print("start_marker")
	m = Maze(20,10, False)	# show maze being built w/ debug data

	#m = Maze(20,10)		# quite mode
	#print(m)