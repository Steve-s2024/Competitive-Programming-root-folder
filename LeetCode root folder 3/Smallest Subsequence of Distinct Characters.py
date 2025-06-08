

# can't solve it...
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        mp = Counter(s)

        res = []
        stack = deque()
        i = 0
        length = len(mp)
        for _ in range(length):
            # print(mp)
            while True:
                if s[i] in mp:
                    while stack and stack[-1][1] > s[i]:
                        stack.pop()
                    stack.append((i, s[i]))
                    mp[s[i]]-=1
                    if mp[s[i]] == 0:
                        break
                i += 1

            while stack and stack[0][1] not in mp:
                stack.popleft()
            idx, val = stack.popleft()
            res.append(val)
            mp.pop(val)

            for j in range(idx+1, i+1):
                if s[j] in mp:
                    mp[s[j]] += 1
            i = idx+1

        return ''.join(res)