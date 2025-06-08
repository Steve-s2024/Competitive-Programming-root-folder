# binary search solution, pretty obvious binary search 
# & greedly simulation solution: 100%
# but to get the sum1 and sum2 with the proper formula is 
# quite challenging
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        res = 0
        l, r = 1, maxSum
        l1, l2 = index, n-1-index
        while l <= r:
            m = (l+r) // 2
            # pretend m is the values of nums[index]
            if l1 >= m-1:
                sum1 = l1-(m-1) + m*(m-1)//2
            else:
                sum1 = l1*(l1+1)//2 + (m-1 - l1)*l1
            if l2 >= m-1:
                sum2 = l2-(m-1) + m*(m-1)//2
            else:
                sum2 = l2*(l2+1)//2 + (m-1 - l2)*l2

            if sum1 + m + sum2 > maxSum:
                r = m-1
            else:
                res = m
                l = m+1
        return res 