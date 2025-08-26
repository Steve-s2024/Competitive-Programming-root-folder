


# fking edge cases driving me mad, it all comes down to the stupid rule that Alice lose when no stone left to collect

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:

        n = len(stones)
        mp = defaultdict(int)
        for i in range(n): mp[stones[i] % 3] += 1

        # alice start with 1
        zero, one, two = mp[0], mp[1], mp[2]
        if one:
            one -= 1
            if zero % 2 == 0 and one < two: return True
            if zero % 2 == 1 and not one < two: return True

        # alice start with 2
        zero, one, two = mp[0], mp[1], mp[2]
        if two:
            two -= 1
            if zero % 2 == 0 and two < one: return True
            if zero % 2 == 1 and not two < one: return True

        return False
