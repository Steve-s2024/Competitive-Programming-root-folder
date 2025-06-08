# holy, the bug in the previous code is so subtle that i would never realize
# without the help of Chat, here the bug is fixed, but spend too much memory
# : MLE
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        dp = {}
        def recursive(i, j):
            nonlocal n, m
            if (i, j) in dp:
                return dp[(i, j)]
            if i >= n or j >= m:
                q = deque(str1[i:]) + deque(str2[j:])
                return q
            if str1[i] == str2[j]:
                a = recursive(i + 1, j + 1)
                q = a.copy()
                q.appendleft(str1[i])
            else:
                a = recursive(i + 1, j)
                b = recursive(i, j + 1)
                if len(a) < len(b):
                    q = a.copy()
                    q.appendleft(str1[i])
                else:
                    q = b.copy()
                    q.appendleft(str2[j])
            dp[(i, j)] = q
            return q

        q = recursive(0, 0)
        # print(q)
        return ''.join(q)


# doesn't feel like a normal question, something is odd about it, im gonna skip it
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        dp = {}
        def recursive(i, j):
            nonlocal n, m
            if (i, j) in dp:
                return dp[(i, j)]
            if i >= n or j >= m:
                q = deque(str1[i:]) + deque(str2[j:])
                return q
            if str1[i] == str2[j]:
                q = recursive(i + 1, j + 1)
                q.appendleft(str1[i])
            else:
                a = recursive(i + 1, j)
                b = recursive(i, j + 1)
                if len(a) < len(b):
                    q = a
                    q.appendleft(str1[i])
                else:
                    q = b
                    q.appendleft(str2[j])
            dp[(i, j)] = q.copy()
            return q

        q = recursive(0, 0)
        # print(q)
        return ''.join(q)

# misunderstood the question and returned the length of the shortest
# supersequence
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        def recursive(i, j):
            nonlocal n, m
            if i >= n or j >= m:
                return max(m-j, n-i)
            if str1[i] == str2[j]:
                res = recursive(i+1, j+1) + 1
            else:
                res = min(
                    recursive(i+1, j),
                    recursive(i, j+1)
                ) + 1
            return res
        return recursive(0, 0)