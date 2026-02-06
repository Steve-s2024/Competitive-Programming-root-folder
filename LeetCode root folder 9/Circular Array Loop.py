# actually an interesting problem (a practice on the fundamentals of circuit manipulation)
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        g = [0]*n
        for u, v in enumerate(nums): g[u] = (u+v)%n

        # print(g)
        vs = [0]*n
        for u in range(n):
            if vs[u]: continue
            cr = u
            us = deque()
            while vs[cr] == 0:
                us.append(cr)
                vs[cr] = 1
                cr = g[cr]
            while us and us[0] != cr: us.popleft()
            if len(us) < 2: continue
            for u in us:
                if nums[u]*nums[us[0]] < 0: break
            else: return True
        return False