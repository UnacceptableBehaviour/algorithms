#! /usr/bin/env python
# 3.7

from pprint import pprint
from collections import Counter
import timeit

# R20 MIT 6.006 - Dynamic Programing - Blackjack
# https://courses.csail.mit.edu/6.006/fall11/rec/rec20.pdf



# Rules / Info - - - - <
# Ace can be 1 or 11.
# Dealer sticks on 17 or higher
# $1 per win - outcomes = {1,0,-1} win, draw, lose < represented by EDGES
# deck is represents [c0,c1,c2, . . cn-1]        cn-1 because starts at 0

# Strategy
# We want to know number of hits or if we should stick (0 hits) for some
# suffix of cards starting at i. Suffix of card is a subset of cards (IE sub-problem)

# i         the number of cards already played!
# BJ(i)     the best play with the remnaining cards [c0,c1,c2, . . cn-1]
# BJ(i)s    will be the sub problems
# O(n)      of these sub problems since i spans from 0-n
# gues how many time player hits the deck - O(n) guesses

# Q won't a certain propotion of these be invalid plays since player bust?
 
# from handout
# 
# BJ(i):
#     if n-1 < 4: return 0        # since there are not enough cards
#     
#     for p in range(2, n-i-2):   # number of cards taken
#         # player's cards by deal order (player, then dealer, then player)
#         player = sum(c_i, c_{i+2}, c_{i+4:i+p+2})
#         
#         if player > 21:         # bust
#             options.append(-1 + BJ(i+p+2))
#             break
# 
#         for d in range(2, n-i-p):
#             dealer = sum(c_{i+1}, c_{i+3}, c_{i+p+2:i+p+d})
#             if dealer >= 17: break
# 
#         if dealer > 21: dealer = 0 # bust
# 
#         options.append(cmp(player, dealer) + BJ(i+p+d))   # < recurrence
# 
#     return max(options)


# for each  


if __name__ == '__main__':
    
    print("S")
    
    
    
