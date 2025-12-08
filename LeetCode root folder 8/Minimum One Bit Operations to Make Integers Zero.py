# quite hard to derive the true version of this question, turns out you can treat it as a game theory problem
class Solution:
    def minimumOneBitOperations(self, num: int) -> int:
        mp = [0]*32
        for i in range(32): mp[i] = 2*mp[i-1] + 1
        s = str(bin(num))[2:][::-1]
        n = len(s)
        # print(mp, s)
        def recursive(i, t):
            nonlocal n
            if i < 0: return 0
            if t == 1: # form of 1000....
                if s[i] == '1': return recursive(i-1, 0)
                else: return 1 + recursive(i-1, 1) + (mp[i-1] if i else 0)
            else:  # form of 0000....
                if s[i] == '0': return recursive(i-1, 0)
                else: return 1 + recursive(i-1, 1) + (mp[i-1] if i else 0)
        return recursive(n-1, 0)
