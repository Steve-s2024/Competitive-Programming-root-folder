# greedy 97%, masterpeice 🤣
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        # for the example case of nums = [6, 3, 3, 2], k = 1
        # before any operation, the product of nums is 6*3*3*2, call it oldProd
        # 
        # if choose to increase the first element, the final result will be: oldProd with an increase of (oldProd/firstElement) 
        # why the increase (oldProd/firstElement)? it comes from (6+1)*3*3*2, which is the new product,  
        # subtract 6*3*3*2, which is the old product.
        #
        # the above observation can be expand to --> if choose to increase the ith element, the result
        # will be --> oldProd + (oldProd/nums[i])

        # observe that to maximize the result, oldProd is constant, so we minimize nums[i].
        # in another word, spend the operation on increasing the min(nums)

        # for cases that k > 1, I didn't spend time to prove it, but my greedy solution worked...

        MOD = 1000000007

        nums.sort()
        nums.append(-1)
        total = 0
        prev = 0
        res = 1
        for i in range(len(nums)):
            total += nums[i]
            void = (i+1)*nums[i] - total 
            if void > k or i == len(nums)-1:
                total -= nums[i]
                extra = k - (i*prev - total)
                multiple = extra // i
                remain = extra % i
                
                base = multiple + prev
                a = i-remain
                b = remain

                res = pow(base, a) * pow(base+1, b)
                res %= MOD
                for j in range(i, len(nums)-1):
                    res *= nums[j]
                    res %= MOD
                break

            prev = nums[i]
        
        return res % MOD





