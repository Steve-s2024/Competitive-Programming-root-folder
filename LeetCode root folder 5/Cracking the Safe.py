# so far the hardest question solved on leetcode, of course I have learned De Bruijn's Graph and
# Eulerian circuit algo (actually a simple DFS post-order traversal): 50%

class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        if n == 1: return ''.join([str(i) for i in range(k)])
        nodes = set()
        stk = []
        def backtrack(i):
            nonlocal stk
            if i >= n-1:
                nodes.add(''.join(stk))
                return
            for j in range(k):
                stk.append(str(j))
                backtrack(i+1)
                stk.pop()
        backtrack(0)

        vis = set()
        def dfs(node):
            nonlocal begin
            for i in range(k):
                if (node, i) not in vis:
                    vis.add((node, i))
                    dfs(node[1:]+str(i))
            strarr.append(node[-1])

        begin = '0'*(n-1)
        strarr = []
        dfs(begin)
        strarr[-1] = begin
        strarr = strarr[::-1]
        return ''.join(strarr)


# a second version of it: 50%
# I changed the post-order DFS a bit
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        if n == 1: return ''.join([str(i) for i in range(k)])
        nodes = set()
        stk = []
        def backtrack(i):
            nonlocal stk
            if i >= n-1:
                nodes.add(''.join(stk))
                return
            for j in range(k):
                stk.append(str(j))
                backtrack(i+1)
                stk.pop()
        backtrack(0)

        vis = set()
        def dfs(node):
            nonlocal begin
            for i in range(k):
                if (node, i) not in vis:
                    vis.add((node, i))
                    dfs(node[1:]+str(i))
                    strarr.append(str(i))

        begin = '0'*(n-1)
        strarr = []
        dfs(begin)
        strarr.append(begin)
        strarr = strarr[::-1]
        return ''.join(strarr)