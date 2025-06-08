# this is the most uncertain code process of my career, I didn't try to
# prove any intuition, but keeps pushing the train of thoughts beyond the
# limit, and giving up understanding every corner of the solution
# it really gave me a boost in solving problem and lower brain burden
# this is probably the best way to practice under stressful situation
# most importantly, I start taking the help of the universe to help me
# When not certain of one of two choices, simply try to run both and pick the one that worked.
# this new strategy can also explain the long and duplicated code below: 71%
# I would hardly be able to explain to someone what is happening here (the code), but
# the strategy did help me to solve a seemingly brain-racking work
# in under short time and low mind stress.
# you can hardly understand the code below, cause I have taken too much shortcuts and tricks
# developing the solution, but the good thing is I did gain confident and a new way of working

# also, in the entire process I always try to favor easy steps over compact code.
# so, even the code is tedious and it could be potentially around 20 lines, but the way
# I did it elevated the level of comfortability by a lot for the coding and thought process
# for each step.
class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        a, b = 0, 0
        c, d = 0, 0
        pre = [None] * n
        for i in range(n):
            if i % 2 == 0:
                if s[i] == '0':
                    a += 1
                else:
                    b += 1
            else:
                if s[i] == '0':
                    c += 1
                else:
                    d += 1
            pre[i] = (a + d, b + c)

        a, b = 0, 0
        c, d = 0, 0
        suf = [None] * n
        for i in range(n - 1, -1, -1):
            if i % 2 == 0:
                if s[i] == '0':
                    a += 1
                else:
                    b += 1
            else:
                if s[i] == '0':
                    c += 1
                else:
                    d += 1
            suf[i] = (a + d, b + c)

        if n % 2 == 0:
            return min(a + d, b + c)

        # print(pre, suf)
        res = float('inf')
        for i in range(n - 1):
            tot = 0
            if s[i] == s[i + 1]:
                if s[i] == '0':
                    if i > 0:
                        if i % 2 == 0:
                            tot += pre[i - 1][1]
                        else:
                            tot += pre[i - 1][0]
                    if i + 1 < n - 1:
                        if i % 2 == 0:
                            tot += suf[i + 2][0]
                        else:
                            tot += suf[i + 2][1]
                else:
                    if i > 0:
                        if i % 2 == 0:
                            tot += pre[i - 1][0]
                        else:
                            tot += pre[i - 1][1]
                    if i + 1 < n - 1:
                        if i % 2 == 0:
                            tot += suf[i + 2][1]
                        else:
                            tot += suf[i + 2][0]
                # print(i, tot)
                res = min(tot, res)
        return min(res, min(a + d, c + b))

