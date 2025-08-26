# pretty tough, force me to fill in the gaps of parenthesis validation process: 93%

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        q = deque()
        stk = []
        for i in range(n):
            if locked[i] == '1':
                if s[i] == '(': stk.append(i)
                else:
                    if stk: stk.pop()
                    elif q: q.popleft()
                    else: return False
            else: q.append(i)
        while stk:
            if q and q[-1] > stk[-1]:
                stk.pop()
                q.pop()
            else: return False

        return len(q) % 2 == 0