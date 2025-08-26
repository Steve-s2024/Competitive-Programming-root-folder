# pretty similar to the Q3 in recent contest, reverse engineering: 100%
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        n = len(operations)
        tot = pow(2, n)
        crr = k
        dva = 0
        for i in range(n - 1, -1, -1):
            tot //= 2
            if crr > tot:
                crr -= tot
                if operations[i] == 1:
                    dva += 1
                    dva %= 26

        # now tot will be 1, crr will be 1, and dva will tell me the answer
        return chr(dva + ord('a'))