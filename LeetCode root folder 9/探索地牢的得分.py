# 挺吓人的一题， 给我绕进去了
class Solution:
    def totalScore(self, hp: int, dam: List[int], req: List[int]) -> int:
        n = len(dam)
        t = 0
        suf = [0] * n
        for i in range(n - 1, -1, -1):
            t += dam[i]
            suf[i] = t

        sl = SortedList(suf)
        sm = 0
        score = 0
        for i in range(n - 1, -1, -1):
            tar = hp + sm - req[i]
            x = sl.bisect_right(tar)
            score += x
            sm += dam[i]
            sl.remove(suf[i])

        return score