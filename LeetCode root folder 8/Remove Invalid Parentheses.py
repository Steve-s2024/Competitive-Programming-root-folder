# bit brute force backtracking solution
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        mp = defaultdict(list)
        stk = []
        def recursive(i, ct):
            if ct < 0: return
            if i >= len(s):
                if ct == 0: mp[len(stk)].append(''.join(stk))
                return
            if s[i] in '()':
                recursive(i+1, ct)
                stk.append(s[i])
                recursive(i+1, ct+(1 if s[i] == '(' else -1))
                stk.pop()
            else:
                stk.append(s[i])
                recursive(i+1, ct)
                stk.pop()
        recursive(0, 0)
        # print(mp)
        return list(set(mp[max(mp.keys())]))