# sorted set implementation, either you know it and its easy or you don't know it and its very hard: 18%
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        ss = SortedSet([i for i in range(k)])
        minheap = []
        mp = defaultdict(int)
        n = len(arrival)
        for i in range(n):
            a, l = arrival[i], load[i]
            while minheap and minheap[0][0] <= a:
                _, server = heapq.heappop(minheap)
                ss.add(server)

            if not ss: continue

            pos = ss.bisect_left(i % k)
            if pos >= len(ss): pos = 0
            use = ss[pos]
            ss.remove(use)
            mp[use] += 1
            heapq.heappush(minheap, (a + l, use))

        # print(mp)
        ans = []
        mx = max(mp.values())
        for key, val in mp.items():
            if val == mx: ans.append(key)
        return ans
