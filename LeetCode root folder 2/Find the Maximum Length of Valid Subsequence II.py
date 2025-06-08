# the time complexity is really hard to define, I expected this to TLE,
# but I guess the worst case scenario didn't happen: 85%
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        idxMp = defaultdict(list)
        for i in range(n):
            remain = nums[i] % k
            idxMp[remain].append(i)

        def getMaxInterleave(arr1, arr2):
            i1, i2 = 0, 0
            n1, n2 = len(arr1), len(arr2)
            res = 2
            while i1 < n1 and i2 < n2:
                i1 += 1
                while i1 < n1 and arr1[i1] < arr2[i2]:
                    i1 += 1
                if i1 < n1:
                    res += 1
                else:
                    break
                i2 += 1
                while i2 < n2 and arr2[i2] < arr1[i1]:
                    i2 += 1
                if i2 < n2:
                    res += 1
            return res

        ans = 0
        for i in range(k):
            for j in range(i+1, k):
                if idxMp[i] and idxMp[j]:
                    if idxMp[i][0] < idxMp[j][0]:
                        arr1 = idxMp[i]
                        arr2 = idxMp[j]
                    else:
                        arr2 = idxMp[i]
                        arr1 = idxMp[j]

                    ans = max(ans, getMaxInterleave(arr1, arr2))
            ans = max(len(idxMp[i]), ans)
        return ans

# failed attempt
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        hashSet = set()
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i):
                sum_ = nums[i] + nums[j]
                if sum_%k not in hashSet:
                    hashSet.add(sum_%k)
                    q = deque([nums[j], nums[i]])
                    length = 2
                    for ii in range(i+1, n):
                        if abs(q[0] - nums[ii]) % k == 0:
                            q.popleft()
                            q.append(nums[ii])
                            length += 1
                    # print(i, j, length)
                    res = max(res, length)
        return res
