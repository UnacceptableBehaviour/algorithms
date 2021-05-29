#! /usr/bin/env python
# 3.7

from collections import deque
import random
from pprint import pprint
import os


# colour layout - yellow front & centre
#    W
#  R Y O B    blue wraps to back
#    G

# representation base 3 digit for each corner in a byte
# describes orientation

# 0   3   6   9         12   15   18   21                        
# 1   4   7   10        13   16   19   22                  
# 2   5   8   11        14   17   20   23                  

#    W                      W
#  R Y O B                O B R
#    G                      G
#
#  FRONT                 BACK

# F1 W W F2            B2 W W B1
#  R Y Y O              O B B R
#  R Y Y O              O B B R
# F4 G G F3            B3 G G B4
#
#   FRONT    BACK - - - - BACK
#   |           |
#   |           |
#   F1  F2  B2  B1      ----- 
#   R    L  L    R
#  
#   F4  F3  B3  B4      -----
#   ------
#       ------
#           ------
#   --          --
#   Legal moves
#   Rotate      F1  F2  B2  B1      Row L/R
#   Rotate      F4  F3  B3  B4      Row L/R
#   Rotate      F1  F2  F3  F4      Front CW/CCW
#   Rotate      B4  B3  B2  B1      Back  CW/CCW
#   Rotate      F2  B2  B3  F3      Left  TB/TF     rotate towards back TB = CW if facing side
#   Rotate      F1  B1  B4  F4      Right TB/TF     rotate towards back TB = CCW if facing side
#
#   Rotate L1 = Rotate R3
#   Rotate L2 = Rotate R2
#   Rotate 4  = No move     So only need to rotate in one direction since 3 forward = 1 backward!
#
#   Same for oposite sides of axis - relative to each other only need move one! right?
#



class RubiksCorner:
    colour_map = {
        'F1' : ['','Y',''],
        'F2' : ['','Y',''],
        'F3' : ['','Y',''],
        'F4' : ['','Y',''],
        'B1' : ['','B',''],
        'B2' : ['','B',''],
        'B3' : ['','B',''],
        'B4' : ['','B',''],
    }
    def __init__(self, position):
        self.orientation = 0

class RubiksCube:
    def __init__(self):
      self.F = [RubiksCorner('F1'),RubiksCorner('F2'),RubiksCorner('B2'),RubiksCorner('B1')]
      self.B = [RubiksCorner('F4'),RubiksCorner('F3'),RubiksCorner('B3'),RubiksCorner('B4')]
        
        

if __name__ == '__main__':

    print("start_marker")
    m = Maze(20,10, False)    # show maze being built w/ debug data

    #m = Maze(20,10)        # quite mode
    #print(m)