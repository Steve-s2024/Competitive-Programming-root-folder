# the true bitmasking implementation: 42%
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        bitmask = 0
        dp = {}
        def recursive():
            nonlocal n, sessionTime, bitmask
            if bitmask in dp:
                return dp[bitmask]

            if bitmask == pow(2, n)-1:
                return (0, 1)
            minSessionCnt, minTotal = float('inf'), float('inf')
            for i in range(n):
                if bitmask & pow(2, i) == 0:
                    bitmask ^= pow(2, i)
                    (total, sessionCnt) = recursive()
                    bitmask ^= pow(2, i)
                    if total + tasks[i] > sessionTime:
                        sessionCnt += 1
                        total = tasks[i]
                    else:
                        total += tasks[i]
                    if sessionCnt < minSessionCnt:
                        minSessionCnt = sessionCnt
                        minTotal = total
                    elif sessionCnt == minSessionCnt:
                        minTotal = min(minTotal, total)
            dp[bitmask] = (minTotal, minSessionCnt)
            return (minTotal, minSessionCnt)
        (minTotal, minSessionCnt) = recursive()
        # print(dp)
        return minSessionCnt

# push up the speed a bit more by using array as used (bitmasking): 42%
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        used = ['0']*n
        dp = {}
        def recursive():
            nonlocal n, sessionTime
            state = ''.join(used)
            if state in dp:
                return dp[state]

            if '0' not in used:
                return (0, 1)
            minSessionCnt, minTotal = float('inf'), float('inf')
            for i in range(n):
                if used[i] == '0':
                    used[i] = '1'
                    (total, sessionCnt) = recursive()
                    used[i] = '0'
                    if total + tasks[i] > sessionTime:
                        sessionCnt += 1
                        total = tasks[i]
                    else:
                        total += tasks[i]
                    if sessionCnt < minSessionCnt:
                        minSessionCnt = sessionCnt
                        minTotal = total
                    elif sessionCnt == minSessionCnt:
                        minTotal = min(minTotal, total)
            dp[state] = (minTotal, minSessionCnt)
            return (minTotal, minSessionCnt)
        (minTotal, minSessionCnt) = recursive()
        # print(dp)
        return minSessionCnt


# haha, I made such a stupid mistake with the state of the previous dp
# solution 😂🤣, decent!!: 37%
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        used = set()
        dp = {}
        def recursive():
            nonlocal n, sessionTime
            state = []
            for i in range(n):
                if i not in used:
                    state.append(str(i))
            state = ' '.join(state)
            if state in dp:
                return dp[state]

            if len(used) == n:
                return (0, 1)
            minSessionCnt, minTotal = float('inf'), float('inf')
            for i in range(n):
                if i not in used:
                    used.add(i)
                    (total, sessionCnt) = recursive()
                    used.remove(i)
                    if total + tasks[i] > sessionTime:
                        sessionCnt += 1
                        total = tasks[i]
                    else:
                        total += tasks[i]
                    if sessionCnt < minSessionCnt:
                        minSessionCnt = sessionCnt
                        minTotal = total
                    elif sessionCnt == minSessionCnt:
                        minTotal = min(minTotal, total)
            dp[state] = (minTotal, minSessionCnt)
            return (minTotal, minSessionCnt)
        (minTotal, minSessionCnt) = recursive()
        # print(dp)
        return minSessionCnt



# dp solution with unusual state and return type comparison, but
# failed for whatever reason
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        used = set()
        dp = {}
        def recursive(i):
            nonlocal n, sessionTime
            state = ''.join([str(e) for e in sorted(list(used))])
            if (state, i) in dp:
                return dp[(state, i)]
            if len(used) == n:
                return (tasks[i], 1)
            minSessionCnt, minTotal = float('inf'), float('inf')
            for j in range(n):
                if j not in used:
                    used.add(j)
                    (total, sessionCnt) = recursive(j)
                    used.remove(j)
                    if sessionCnt < minSessionCnt:
                        minSessionCnt = sessionCnt
                        minTotal = total
                    elif sessionCnt == minSessionCnt:
                        if total < minTotal:
                            minTotal = total
            if minTotal + tasks[i] > sessionTime:
                minSessionCnt += 1
                minTotal = tasks[i]
            else:
                minTotal += tasks[i]
            dp[(state, i)] = (minTotal, minSessionCnt)
            return (minTotal, minSessionCnt)

        res = float('inf')
        for i in range(n):
            used.add(i)
            (minTotal, minSessionCnt) = recursive(i)
            used.remove(i)
            # print(i, minTotal, minSessionCnt)
            res = min(res, minSessionCnt)
        # print(dp)
        return res



# brute force: TLE
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        minCnt = float('inf')
        used = set()
        def recursive(i, total, cnt):
            nonlocal n, minCnt, sessionTime
            if len(used) == n:
                minCnt = min(minCnt, cnt)
                return
            for j in range(n):
                if j not in used:
                    used.add(j)
                    if total + tasks[j] > sessionTime:
                        recursive(j, tasks[j], cnt+1)
                    else:
                        recursive(j, total + tasks[j], cnt)
                    used.remove(j)
        for i in range(n):
            used.add(i)
            recursive(i, tasks[i], 1)
            used.remove(i)
        return minCnt

