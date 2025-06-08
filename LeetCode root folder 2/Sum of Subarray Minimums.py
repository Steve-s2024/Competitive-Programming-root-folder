# handle duplicate, and efficient, but holy this is long...: 5%
class Solution:
    def getBounds(self, arr, n):
        bounds = [[0, 0] for i in range(n)]
        stack = []
        for i in range(n):
            val = arr[i]
            while stack and val <= stack[-1][0]:
                [prevVal, prevI] = stack.pop()
                bounds[prevI][1] = i - 1
            stack.append((val, i))
        while stack:
            [prevVal, prevI] = stack.pop()
            bounds[prevI][1] = n - 1

        for i in range(n - 1, -1, -1):
            val = arr[i]
            while stack and val <= stack[-1][0]:
                [prevVal, prevI] = stack.pop()
                bounds[prevI][0] = i + 1
            stack.append((val, i))
        while stack:
            [prevVal, prevI] = stack.pop()
            bounds[prevI][0] = 0

        hashMap = defaultdict(list)
        for i in range(n):
            val = arr[i]
            [l, r] = bounds[i]
            hashMap[val].append((l, r, i))
        return hashMap

    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        MOD = 1000000007
        hashMap = self.getBounds(arr, n)
        res = 0
        for key, val in hashMap.items():
            val.append((float('inf'), -1, -1))  # add the terminator
            m = len(val)
            [L, R, IDX] = val[0]
            [l_idx, r_idx] = IDX, IDX
            offset = 0
            for i in range(1, m):
                [l, r, idx] = val[i]
                if l <= R + 1:
                    # connect the two
                    size = idx - r_idx - 1
                    offset += size * (size + 1) // 2
                    r_idx = idx
                    R = r
                else:
                    # calc the cluster L to R contribution of val
                    size = R - L + 1
                    comb = size * (size + 1) // 2
                    left, right = l_idx - L, R - r_idx
                    comb -= offset + (left * (left + 1) // 2 + right * (right + 1) // 2)
                    # print(key, comb)
                    res += comb * key
                    res %= MOD
                    offset = 0
                    L, R = l, r
                    l_idx, r_idx = idx, idx
        return res


# handle duplicate, but not efficient enough: TLE
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        MOD = 1000000007
        hashMap = defaultdict(list)
        for i in range(n):
            val = arr[i]
            l, r = i-1, i+1
            while l >= 0 and arr[l] > val:
                l-=1
            while r < n and arr[r] > val:
                r+=1
            hashMap[val].append((l+1, r-1, i))

        # print(hashMap)
        res = 0
        for key, val in hashMap.items():
            val.append((float('inf'), -1, -1)) # add the terminator
            m = len(val)
            [L, R, IDX] = val[0]
            [l_idx, r_idx] = IDX, IDX
            offset = 0
            for i in range(1, m):
                [l, r, idx] = val[i]
                if l <= R+1:
                    # connect the two
                    size = idx - r_idx - 1
                    offset += size*(size+1) // 2
                    r_idx = idx
                    R = r
                else:
                    # calc the cluster L to R contribution of val
                    size = R - L + 1
                    comb = size*(size+1) // 2
                    left, right = l_idx - L, R - r_idx
                    comb -= offset + (left*(left+1)//2 + right*(right+1)//2)
                    # print(key, comb)
                    res += comb * key
                    res %= MOD
                    offset = 0
                    L, R = l, r
                    l_idx, r_idx = idx, idx
        return res



# the brute force solution, what can't handle input array with duplicate
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        MOD = 1000000007
        for i in range(n):
            val = arr[i]
            l, r = i-1, i+1
            while l >= 0 and arr[l] > val:
                l-=1
            while r < n and arr[r] > val:
                r+=1
            left, right = i-l, r-i
            res += (left * right) * val
            res %= MOD
        return res % MOD