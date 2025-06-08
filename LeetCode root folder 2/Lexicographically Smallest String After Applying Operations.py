# knapsack solution, I consider this as a brute force solution
# and the worst time complexity can be up to 2^100. However, the
# reality is this passed with average speed. why? maybe because when
# you only allowed to do the operation with specified rules and fixed
# a and b, the possible output will be reduced dramatically from 2^100
# to a small number, but it's really hard to analyze the actual complexity...
# so its more like gambling with odd: 17%
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        q = deque(list(s))
        n = len(q)
        res = '9'*n
        visited = set()
        def recursive(q):
            nonlocal n, res, a, b
            string = ''.join(q)
            if string in visited:
                return
            visited.add(string)
            res = min(res, string)
            q1, q2 = q.copy(), q.copy()
            for i in range(1, n, 2):
                q1[i] = str( (int(q1[i]) + a) % 10 )
            recursive(q1)
            for i in range(b):
                q2.appendleft(q2.pop())
            recursive(q2)
        recursive(q)
        return res