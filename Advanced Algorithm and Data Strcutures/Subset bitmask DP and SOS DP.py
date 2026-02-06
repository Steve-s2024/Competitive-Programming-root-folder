# 01/06/2025 UPD: I think I have an idea of how to optimize the enumerating over submask of the current mask
# now it is 2^n iteration per each function call, where n is the bit count of current mask, since we enumerate over all submask
# however, we actually only need to enumerate over all the submask which is 1 bit count less, this means we only iterate
# n times per each function call, and since that is all the possible way to generate submask (if we treat by generate submask only 1 bit
# can be removed at a time), than this DP over submask can be much more efficient.
# clarification: I choose DP over submask with one less bit count and know this is enough. Why? because when doing DP over choices
# we only care about the transition to sub-problem, doesn't matter how much easier the sub-problem we are transferring to.
# by transferring to 1 bit less submask, we gain a lot efficiency even though the sub-problem themselves didn't become much easier
# (which really doesn't matter as long as it is indeed transitioning to an easier subproblem instead of the same problem or a harder super problem).

# side note: this idea is theoretically sound but does not apply universally, doublecheck the DP state transition before using this idea.






# a program for the trick of iterating through all the subset of a mask represented set
n = 4
for i in range(1<<n):
    m = str(bin(i))[2:].zfill(4)
    print(f'all subsets of the set represented by mask {m} are: ')
    j = i
    while j:
        ma = str(bin(j))[2:].zfill(4)
        j = (j-1)&i
        print(ma)


# ME: chat, here is the problem statement wrote by me. is it a SOS DP problem? given an integer array
# nums, and a query array queries, queries[i] will be a set of indices of nums. return an answer array
# ans where ans[i] is the answer for the ith query, the sum of all the S where S is the sum of any subset
# of the set {nums[queries[i][0]], nums[queries[i][1]], nums[queries[i][2]]...}.

# CHAT: This does not require SOS DP.
# It’s just combinatorial counting. Each element contributes to half the subsets, so the formula is direct.
#
# it can be viewed as an SOS DP problem, but the particularity of the problem makes it very simple and can be solved
# greedily using combinatorics knowledge. you can think of it as a “toy case” where SOS DP degenerates into a direct
# formula because of linearity.

# ME: give me a counter-example where solution will not be simplified to a formula

# CHAT: instead of calculating the sum of S in the problem, calculate the sum of M, where M is
# max({nums[queries[i][0]], nums[queries[i][1]], nums[queries[i][2]]...}).
# here you will require SOS DP for the problem.


# an immature attempt of simplified SOS DP solution, one step away from the algorithm
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        size = 1
        mx = max(nums)
        while 1 << size <= mx: size += 1
        arr = [0] * (1 << size)
        for num in nums: arr[num] = num
        for num in range(1 << size):
            for i in range(size):
                if num & (1 << i): continue
                arr[num | (1 << i)] = max(arr[num | (1 << i)], arr[num])

        # print(arr)
        res = 0
        for num in nums:
            a, b = num, arr[num ^ ((1 << size) - 1)]
            res = max(res, a * b)

        return res
