from collections import defaultdict, deque, Counter
from typing import List
from sortedcontainers import SortedList
import heapq, cmath, sys
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
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
