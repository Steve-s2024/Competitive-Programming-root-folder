from collections import defaultdict, deque, Counter
from typing import List
from sortedcontainers import SortedList, SortedSet
import heapq, sys
from math import gcd, lcm, inf, sqrt
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
    def longestPalindromeSubseq(self, s: str) -> int:
        mp = defaultdict(list)
        for i, c in enumerate(s):
            mp[c].append(i)

        n = len(s)
        @cache
        def recursive(i, j):
            if i > j: return 0
            res = recursive(i+1, j)
            nxtJ = mp[s[i]].pop()
            if i < nxtJ: res = max(res, recursive(i+1, nxtJ) + 2)
            elif i == nxtJ: res = max(res, recursive(i+1, nxtJ) + 1)
            mp[s[i]].append(nxtJ)
            return res
        return recursive(0, n-1)