# simulation solution, push from left to right first, and record the time each dominoe is pushed, then push from
# right to left and do adjustments according to the recorded times:149
# ms
# Beats
# 74.11%
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        i = 0
        t = 0
        ans = ['.'] * len(dominoes)
        time = [float('inf')] * len(dominoes)
        while i < len(dominoes):
            if dominoes[i] == 'R':
                t = 0
                ans[i] = 'R'
                time[i] = t
                while i < len(dominoes) - 1 and dominoes[i + 1] == '.':
                    i += 1
                    t += 1
                    ans[i] = 'R'
                    time[i] = t
            i += 1

        # print(ans, time)
        i = len(dominoes) - 1
        while i >= 0:
            if dominoes[i] == 'L':
                t = 0
                ans[i] = 'L'
                time[i] = t
                while i > 0 and dominoes[i - 1] == '.':
                    i -= 1
                    t += 1
                    if time[i] > t:
                        ans[i] = 'L'
                    elif time[i] == t:
                        ans[i] = '.'
            i -= 1
        # print(ans)
        return ''.join(ans)

