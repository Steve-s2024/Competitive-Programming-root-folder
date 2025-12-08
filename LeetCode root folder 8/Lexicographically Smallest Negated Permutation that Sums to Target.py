class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> List[int]:
        perm = [i for i in range(1, n+1)]
        sm = sum(perm)
        if (sm-target)%2 == 1: return []
        x = (sm-target)//2
        # print(x)
        i = n-1
        while i >= 0:
            if perm[i] <= x:
                x -= perm[i]
                perm[i] = -perm[i]
            i -= 1
        # print(perm)
        if x != 0: return []
        perm.sort()
        return perm