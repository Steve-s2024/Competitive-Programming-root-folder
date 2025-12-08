# absolutely shame on this bullshit question, I have this solution in my head right in the beginning, but have no
# motivation to implement it due to its inefficient O(n*sqrt(n)) time complexity. how can this question do this
# to me! but at least I tried it in the end and able to solve the question (approach with number factorization and
# odd factor comparison for perfect square product)

class Solution:
    def sumOfAncestors(self, n: int, edges: List[List[int]], nums: List[int]) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def f(num):
            res = []
            for i in range(2, int(sqrt(num)) + 1):
                while num % i == 0:
                    res.append(i)
                    num //= i
            if num > 1: res.append(num)
            return res

        vis = [0] * n
        mp = {}
        stk = {}

        def dfs(u):
            cnts = Counter(f(nums[u]))
            tmp = []
            for key, val in cnts.items():
                if val % 2 == 1: tmp.append(key)
            key = tuple(tmp)
            # print(key)
            mp[u] = (stk[key] if key in stk else 0)
            if key in stk:
                stk[key] += 1
            else:
                stk[key] = 1

            for v in g[u]:
                if vis[v]: continue
                vis[v] = 1
                dfs(v)

            stk[key] -= 1
            if stk[key] == 0: stk.pop(key)

        vis[0] = 1
        dfs(0)
        return sum(mp.values())





# I am trying to prove this is O(n) time complexity, but clearly leetcode hidden test case disagree
class Solution:
    def sumOfAncestors(self, n: int, edges: List[List[int]], nums: List[int]) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        vis = [0] * n
        mp = {}
        stk = []

        def dfs(u):
            for i in range(len(stk) - 1, -1, -1):
                prod = stk[i][1] * nums[u]
                # print(u, prod)
                if sqrt(prod) == int(sqrt(prod)):
                    mp[u] = (mp[stk[i][0]] if stk[i][0] in mp else 0) + 1
                    break
            stk.append((u, nums[u]))
            for v in g[u]:
                if vis[v]: continue
                vis[v] = 1
                dfs(v)
            stk.pop()

        vis[0] = 1
        dfs(0)
        return sum(mp.values())