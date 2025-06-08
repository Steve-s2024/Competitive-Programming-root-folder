# ████████╗██╗███╗░░██╗  ██╗░░░░░███████╗
# ╚══██╔══╝██║████╗░██║  ██║░░░░░██╔════╝
# ░░░██║░░░██║██╔██╗██║  ██║░░░░░█████╗░░
# ░░░██║░░░██║██║╚████║  ██║░░░░░██╔══╝░░
# ░░░██║░░░██║██║░╚███║  ███████╗███████╗
# ░░░╚═╝░░░╚═╝╚═╝░░╚══╝  ╚══════╝╚══════╝
#   __________________
#  | ________________ |
#  ||          ____  ||
#  ||   /\    |      ||
#  ||  /__\   |      ||
#  || /    \  |____  ||
#  ||________________||
#  |__________________|
#  \###################\
#   \###################\
#    \        ____       \
#     \_______\___\_______\
# An AC a day keeps the doctor away. (tin_le)

from collections import defaultdict, deque, Counter
import heapq, cmath


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        def recursive(i, width):
            nonlocal n, shelfWidth
            if i >= n:
                return 0, 0
            res = float('inf')
            maxH = float('inf')
            w, h = books[i]
            if width+w <= shelfWidth:
                tot, hei = recursive(i+1, width+w)
                maxH = max(hei, h)
                res = tot

                tot, hei = recursive(i+1, 0)
                if tot+hei+h < res+maxH:
                    maxH = h
                    res = tot+hei

            return res, maxH

        return recursive(0, 0)

