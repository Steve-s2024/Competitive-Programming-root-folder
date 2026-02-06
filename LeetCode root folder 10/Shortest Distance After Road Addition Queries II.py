# the two bizarre constraints changed everything
# 0 <= queries[i][0] < queries[i][1] < n
# There are no two queries such that i != j and queries[i][0] < queries[j][0] < queries[i][1] < queries[j][1].

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        res = []
        sl = SortedList([inf, -inf])
        mp = {inf:inf, -inf:-inf}
        x = n-1
        for u, v in queries:
            j = sl.bisect_left(u)
            f = 0
            while j < len(sl) and mp[sl[j]] <= v:
                f = 1
                l = sl[j]
                r = mp[l]
                sl.remove(l)
                del mp[l]
                x += r-l-1
            if f or (mp[sl[j-1]] <= u and v <= sl[j]):
                mp[u] = v
                sl.add(u)
                # print(u, v)
                x -= v-u-1
            res.append(x)

        return res
