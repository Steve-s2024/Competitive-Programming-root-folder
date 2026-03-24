# a kind of cheating solution, not suppose to pass the time constraint, but they lack good counter testcases
# mo's algorithm (implementing mo's is already a challenge) then combined with an inc and dec helper functions (which is also implementation hell)
# to maintain the maximum frequency element in the curr window.
# it is the dec function which cheats with a complexity of O(n) worst case. in contrast, inc with O(1) is acceptable
# I guess it is really rare for dec to be O(n) such that my overall runtime is very fast
# 1699ms
# Beats
# 82.50%

# otherwise, the intended solution involves a modification to the basic mo's algo, which I am really exhausted to learn
class Solution:
    def subarrayMajority(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n, q = len(nums), len(queries)

        BCT = ceil(sqrt(q))
        BW = ceil(n / BCT)
        ar = [[] for _ in range(BCT)]

        for i in range(q):
            l, r, t = queries[i]
            ar[l // BW].append((l, r, t, i))

        for v in ar: v.sort(key=lambda i: i[1])
        ans = [0] * q

        def inc(mp, MP, j, mx):
            mp[nums[j]] += 1
            x, frq = nums[j], mp[nums[j]]
            MP[frq].append(x)
            return max(mx, (frq, -x))

        def dec(mp, MP, j, mx):
            mp[nums[j]] -= 1
            t = mx[0]
            while t > 0:
                while MP[t] and mp[MP[t][-1]] != t: MP[t].pop()
                if MP[t]:
                    mx = (-1, -1)
                    for v in MP[t]:
                        if mp[v] == t: mx = max(mx, (t, -v))
                    break
                t -= 1
            if t == 0: return (-1, -1)
            return mx

        # print(ar)
        for i in range(BCT):
            A = ar[i]
            if not A: continue
            L, R, T, J = A[0]
            mp = defaultdict(int)
            mx = (-1, -1)
            MP = defaultdict(list)
            for j in range(L, R + 1): mx = inc(mp, MP, j, mx)
            ans[J] = -mx[1] if mx[0] >= T else -1
            # print(L, R, mx)
            A.pop(0)
            for l, r, t, idx in A:
                for j in range(R + 1, r + 1): mx = inc(mp, MP, j, mx)

                if l < L:
                    for j in range(L - 1, l - 1, -1): mx = inc(mp, MP, j, mx)
                else:
                    # print(MP)
                    for j in range(L, l): mx = dec(mp, MP, j, mx)
                ans[idx] = -mx[1] if mx[0] >= t else -1
                L, R = l, r
                # print(l, r, mx)
                # print(mp)
        return ans
