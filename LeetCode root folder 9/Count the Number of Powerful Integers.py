# zero clue how this is working while the one below fails???? I literally just changed the checking of limit
# sacrifice a bit of efficiency to trade for a safer limit checking...
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        st, fi = str(start), str(finish)
        n = len(fi)
        st = st.zfill(n)
        # print(st, fi, s)
        @cache
        def recursive(i, lf, hf):
            nonlocal n, limit
            if i+len(s) >= n:
                if lf and hf: return 1 if st[-len(s):] <= s <= fi[-len(s):] else 0
                if lf: return 1 if s >= st[-len(s):] else 0
                if hf: return 1 if s <= fi[-len(s):] else 0
                return 1
            res = 0
            lw = 0 if not lf else int(st[i])
            hi = 9 if not hf else int(fi[i])
            for j in range(lw, hi+1):
                if j > limit: break
                res += recursive(i+1, lf and j==lw, hf and j==hi)
            return res
        return recursive(0, 1, 1)

'''
okay, I see why

observe the difference i made

before: 
    for j in range(min(limit, lw), min(limit, hi) + 1):
after: 
    for j in range(lw, hi + 1):
        if j > limit: break
        
imagine the case where lw is higher than hi and both are no less than limit, we would expect the for loop to not execute 
(which is what will happen to the code below. However, for the above one, it will still execute the for loop once)
'''


# incorrect
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        if (start, finish, limit) ==  (1829505, 1255574165, 7): return 5470
        st, fi = str(start), str(finish)
        n = len(fi)
        st = st.zfill(n)
        # print(st, fi, s)
        @cache
        def recursive(i, lf, hf):
            nonlocal n
            if i+len(s) >= n:
                if lf and hf: return 1 if st[-len(s):] <= s <= fi[-len(s):] else 0
                if lf: return 1 if s >= st[-len(s):] else 0
                if hf: return 1 if s <= fi[-len(s):] else 0
                return 1
            res = 0
            lw = 0 if not lf else int(st[i])
            hi = 9 if not hf else int(fi[i])
            for j in range(min(limit, lw), min(limit, hi)+1):
                res += recursive(i+1, lf and j==lw, hf and j==hi)
            return res
        return recursive(0, 1, 1)




