# made a tiny trivial unimportant mistake in the code below,
# now fixed!: 67%
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # bfs, merging intervals
        q = deque([0])
        n = len(s)
        right = 0
        while q:
            # print(q)
            size = len(q)
            intervals = []
            while size:
                cur = q.popleft()
                if cur == n - 1:
                    return True
                l, r = cur + minJump, cur + maxJump
                if r <= right:
                    size -= 1
                    continue
                if l <= right:
                    l = right
                if intervals and intervals[-1][1] >= l:
                    intervals[-1][1] = r
                else:
                    intervals.append([l, r])
                size -= 1
            for l, r in intervals:
                for i in range(l, min(n, r + 1)):
                    if s[i] == '0':
                        q.append(i)
            if intervals:
                right = intervals[-1][1]
        return False



# bfs and interval solution: TLE
# don't know why, the complexity is clearly O(n)
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # bfs, merging intervals
        q = deque([0])
        n = len(s)
        visited = set()
        visited.add(0)
        right = 0
        while q:
            size = len(q)
            intervals = []
            while size:
                cur = q.popleft()
                if cur == n - 1:
                    return True
                l, r = cur + minJump, cur + maxJump
                if r <= right:
                    size -= 1
                    continue
                if l <= right:
                    l = right
                if intervals and intervals[-1][1] <= l:
                    intervals[-1][1] = r
                else:
                    intervals.append((l, r))
                size -= 1
            for l, r in intervals:
                for i in range(l, min(n, r + 1)):
                    if s[i] == '0' and i not in visited:
                        visited.add(i)
                        q.append(i)
            right = intervals[-1][1]
        return False




# dp solution, this dp will give O(n^2) in worst case: TLE
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = set()
        def recursive(i):
            nonlocal n, minJump, maxJump
            if i in dp:
                return
            dp.add(i)
            if i == n-1:
                return True
            for j in range(i+minJump, min(n, i+maxJump+1)):
                if s[j] != '1':
                    if recursive(j):
                        return True
            return False
        return recursive(0)