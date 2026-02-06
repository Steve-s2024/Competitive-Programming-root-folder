# the level of my DP instinct is just insane

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        n, m = len(seats), len(seats[0])
        @cache
        def recursive(r, c, msk, msk2):
            nonlocal n, m
            if r >= n: return 0
            if c == m: return recursive(r+1, 0, msk2, 0)

            res = recursive(r, c+1, msk, msk2)
            if (
                (c == 0 or (1<<(c-1)&msk == 0 and 1<<(c-1)&msk2 == 0)) and
                (1<<(c+1)&msk == 0) and
                (seats[r][c] == '.')
            ):
                a = recursive(r, c+1, msk, msk2|1<<c)+1
                res = max(res, a)
            return res
        return recursive(0, 0, 0, 0)