from collections import defaultdict, deque, Counter
from typing import List
from sortedcontainers import SortedList, SortedSet
import heapq, math, sys
sys.setrecursionlimit(1 << 15)
'''
  __________________
 | ________________ |
 ||          ____  ||
 ||   /\    |      ||
 ||  /__\   |      ||
 || /    \  |____  ||
 ||________________||
 |__________________|
 \###################\
  \###################\
   \        ____       \
    \_______\___\_______\
An AC a day keeps the doctor away. (tin_le)
'''


class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
