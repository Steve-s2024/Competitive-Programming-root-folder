# damn its easy

class Solution:
    def minimumCost(self, nums: List[int], k: int, d: int) -> int:
        n = len(nums)
        d += 1
        sl = SortedList(nums[-d:])
        x = sl[k-2]
        t = sum(sl[:k-1])
        mp = [0]*n
        mp[n-d] = t
        for i in range(n-d-1, -1, -1):
            a = nums[i]
            sl.add(a)
            if a < x:
                t -= x
                t += a
                x = sl[k-2]

            b = nums[i+d]
            if b < x:
                t -= b
                sl.remove(b)
                x = sl[k - 2]
                t += x
            elif b == x and sl.bisect_right(x) == k-1:
                t -= b
                sl.remove(b)
                x = sl[k - 2]
                t += x
            else:
                sl.remove(b)
                x = sl[k - 2]
            mp[i] = t

        # print(mp)

        return nums[0] + min(mp[1:-d+1])






# new data structure acquired: Dual Heap
class DoubleHeap:
    def __init__(self, k):
        self.k, self.mihp, self.mxhp = k, [], []
        self.frq, self.frq2, self.sm, self.ct = defaultdict(int), defaultdict(int), 0, 0

    def push(self, e):
        k, mihp, mxhp, frq, sm, ct, frq2 = self.k, self.mihp, self.mxhp, self.frq, self.sm, self.ct, self.frq2
        frq[e] += 1
        ct += 1
        sm += e
        heappush(mxhp, -e)
        if ct > k:
            while frq[-mxhp[0]] == 0: heappop(mxhp)
            e = -heappop(mxhp)
            heappush(mihp, e)
            frq2[e] += 1
            frq[e] -= 1
            ct -= 1
            sm -= e
        self.sm, self.ct = sm, ct

    def pop(self, e):
        k, mihp, mxhp, frq, sm, ct, frq2 = self.k, self.mihp, self.mxhp, self.frq, self.sm, self.ct, self.frq2
        if frq2[e]: frq2[e] -= 1
        elif frq[e]:
            frq[e] -= 1
            sm -= e
            while frq2[mihp[0]] == 0: heappop(mihp)
            e = heappop(mihp)
            heappush(mxhp, -e)
            frq2[e] -= 1
            frq[e] += 1
            sm += e
        self.sm, self.ct = sm, ct




class Solution:
    def minimumCost(self, nums: List[int], k: int, d: int) -> int:
        n = len(nums)
        d += 1
        dh = DoubleHeap(k-1)
        for i in range(n-d, n):
            dh.push(nums[i])

        mp = [1<<40]*n
        mp[n-d] = dh.sm
        for i in range(n-d-1, -1, -1):
            dh.push(nums[i])
            dh.pop(nums[i+d])
            mp[i] = dh.sm

        return nums[0] + min(mp[1:])
