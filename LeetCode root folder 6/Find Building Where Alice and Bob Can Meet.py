# the rating is too high, but let's go!! no hint read, and I come up with the seg tree solution, I have this strong intuition
# after watching NeetCode solution for a bit. though he probably is going to use priority queue at the end:  15%
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        arr = heights
        n = len(arr)
        ans = []
        tree = build(0, n-1, arr)
        for a, b in queries:
            if a == b:
                ans.append(a)
            elif a > b and heights[a] > heights[b]:
                ans.append(a)
            elif b > a and heights[b] > heights[a]:
                ans.append(b)
            else:
                mx = max(arr[a], arr[b])
                idx = query(tree, mx, max(a, b)+1, n)
                # print(a, b)
                # print(idx)
                ans.append(idx if idx != inf else -1)
        return ans

# 1. build
def build(l, r, inputArr):
    if l >= r:
        return TreeNode(inputArr[l])
    m = (l + r) // 2
    a = build(l, m, inputArr)
    b = build(m+1, r, inputArr)
    return TreeNode(
        max(a.val, b.val),
        a,
        b
    )

# 2. query
def query(root, mx, L, n):
    def dfs(node, l, r):
        nonlocal mx, L
        if l == r: return l if node.val > mx else inf

        m = (l+r)//2
        if r < L: return inf
        elif l < L and r >= L:
            res = inf
            if m >= L and node.left and node.left.val > mx:
                res = dfs(node.left, l, m)
            if node.right and node.right.val > mx:
                res = min(res, dfs(node.right, m+1, r))
            return res
        elif L <= l:
            if node.left and node.left.val > mx:
                return dfs(node.left, l, m)
            elif node.right and node.right.val > mx:
                return dfs(node.right, m+1, r)
        return inf
    return dfs(root, 0, n-1)



# NeetCode solution, using minheap: 64%
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:

        q = len(queries)
        arr = heights
        n = len(arr)
        mp = defaultdict(list)
        ans = [-1] * q
        for i, val in enumerate(queries):
            l, r = sorted(val)
            lv, rv = arr[l], arr[r]
            if l == r:
                ans[i] = l
            elif lv < rv:
                ans[i] = r
            else:
                mp[r].append((lv, i))

        minheap = []
        for i in range(n):
            for mx, idx in mp[i]: heapq.heappush(minheap, (mx, idx))

            val = arr[i]
            while minheap and minheap[0][0] < val:
                _, idx = heapq.heappop(minheap)
                ans[idx] = i

        return ans



# the rating is too high, I will only do the brute force version, then I will watch the neetcode solution: TLE
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)
        q = len(queries)
        ans = []
        for i in range(q):
            a, b = queries[i]
            if a == b:
                ans.append(a)
                continue

            st = set()
            st.add(a)
            for j in range(a, n):
                if heights[j] > heights[a]: st.add(j)
            if b in st:
                ans.append(b)
                continue
            for j in range(b, n):
                if heights[j] > heights[b] and j in st:
                    ans.append(j)
                    break
            else: ans.append(-1)
        return ans