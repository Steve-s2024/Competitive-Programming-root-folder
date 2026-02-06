# I tried DP for an hour, but hit dead end every time
# than think about greedy and realize it is indeed greedy, sadly I could not make enough observation to prove the approach
# it is a gamble after all (it worked though)

class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        n = len(nums)
        xor = 0
        for v in nums: xor ^= v
        mp = Counter(nums)
        for i in range(n):
            if xor == 0: return i%2 == 0
            for k, v in list(mp.items()):
                if xor == k or v == 0: continue
                mp[k] -= 1
                xor ^= k
                break
        return n%2 == 0

# I thought about it and realize something... lol it is such a hard brainteaser (this is actually so simple)
class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        xor = 0
        for v in nums: xor ^= v
        return xor == 0 or len(nums)%2 == 0




