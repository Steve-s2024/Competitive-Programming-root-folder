# bfs solution:3
# ms
# Beats
# 68.95%
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        visited = set()
        q = deque([])
        ans = [0] * len(s)
        for i in range(len(s)):
            if s[i] == c:
                q.append(i)
                visited.add(i)

        time = 0
        while q:
            l = len(q)
            while l:
                cur = q.popleft()
                ans[cur] = time
                if cur - 1 not in visited and cur > 0:
                    visited.add(cur - 1)
                    q.append(cur - 1)
                if cur + 1 not in visited and cur < len(s) - 1:
                    visited.add(cur + 1)
                    q.append(cur + 1)
                l -= 1
            time += 1
        return ans