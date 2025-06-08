# this is actually a pretty amazing question, the solution is absolutely
# fantastic, and I am so stupid for stuck on the comparing part for so
# long when it is so simple.😂:6%
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        n = len(nums)
        for i in range(n):
            j = i
            while j > 0:
                # compare nums[j-1] and nums[j]
                a, b = nums[j-1], nums[j]
                str1, str2 = a+b, b+a
                m = len(str1)
                state = 0
                for k in range(m):
                    if str1[k] < str2[k]:
                        state = -1
                        break
                    if str1[k] > str2[k]:
                        state = 1
                        break
                if state == -1:
                    nums[j] = a
                    nums[j-1] = b
                j-=1

        # print(nums, max(nums))
        res = ''.join(nums)
        i = 0
        while res[i] == '0' and i < n-1:
            i += 1
        return res[i:]


# comparing solution, not finished
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        n = len(nums)
        for i in range(n):
            j = i
            while j > 0:
                # compare nums[j-1] and nums[j]
                a, b = nums[j - 1], nums[j]
                min_ = min(len(a), len(b))
                state = 0
                for k in range(min_):
                    if a[k] > b[k]:
                        state = -1
                        break
                    if a[k] < b[k]:
                        state = 1

                if state == 0:
                    if len(a) > min_:
                        i1, i2 = min_, 0
                    elif len(b) > min_:
                        i1, i2 = 0, min_
                    else:
                        i1, i2 = len(a), len(b)

                    while i1 < len(a) and i2 < len(b):
                        if a[i1] > b[i2]:
                            state = -1
                            break
                        if a[i1] < b[i2]:
                            state = 1
                            break

                if state == 1 or (state == 0 and len(a) > len(b)):
                    nums[j] = a
                    nums[j - 1] = b
                j -= 1

        print(nums, max(nums))
        return ''.join(nums)



# this is not easy at all, make it tag hard!
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        n = len(nums)
        for i in range(n):
            j = i
            while j > 0:
                # compare nums[j-1] and nums[j]
                a, b = nums[j - 1], nums[j]
                min_ = min(len(a), len(b))
                state = 0
                for k in range(min_):
                    if a[k] > b[k]:
                        state = -1
                        break
                    if a[k] < b[k]:
                        state = 1

                if state == 0:
                    if len(a) > min_:
                        if a[min_] > a[0]:
                    if len(b) > min_:
                        first = b[min_]

                if state == 1:
                    nums[j] = a
                    nums[j - 1] = b

                j -= 1

        print(nums, max(nums))
        return ''.join(nums)

# [34323,3432]
# [999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999,999999999]
# [0,0,0]
# [999999,999999998,999999997]
# [121,12]
# [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
# [121,12,120]
# [1,11,111,1112]