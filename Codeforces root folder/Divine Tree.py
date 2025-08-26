# good construction greedy question, somewhat intuitive, but the implementation need some thinking
from collections import defaultdict, deque, Counter
import heapq, math


def solve():
    n, m = [int(e) for e in input().split()]
    if m not in range(n, n*(n+1)//2 + 1): print(-1)
    else:
        res = []
        val = n
        st = set([i for i in range(1, n+1)])
        for i in range(n-1, -1, -1):
            if m-val < i:
                node = m-i
                st.remove(m-i)
                res.append(node)
                if node != 1:
                    node = 1
                    res.append(node)
                    st.remove(node)
                for node in st:
                    res.append(node)
                break
            node = val
            st.remove(node)
            res.append(node)
            m -= val
            val -= 1

        print(res[0])
        for i in range(1, len(res)):
            print(str(res[i-1]) + ' ' + str(res[i]))

t = int(input())
for i in range(t):
    solve()


