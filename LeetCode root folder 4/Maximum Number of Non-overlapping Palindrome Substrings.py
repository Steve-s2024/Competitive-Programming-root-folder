# greedy and brute force: 47%
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        arr1, arr2 = [0]*n, [0]*n
        q = deque()
        for i in range(k):
            q.append(s[i])
        for i in range(k, n):
            cur = ''.join(q)
            if cur == cur[::-1]:
                arr1[i-k] = 1
            q.append(s[i])
            q.popleft()

        cur = ''.join(q)
        if cur == cur[::-1]:
            arr1[n-k] = 1

        if k < n:
            q = deque()
            for i in range(k+1):
                q.append(s[i])
            for i in range(k+1, n):
                cur = ''.join(q)
                if cur == cur[::-1]:
                    arr2[i-k-1] = 1
                q.append(s[i])
                q.popleft()
            cur = ''.join(q)
            if cur == cur[::-1]:
                arr2[n-k-1] = 1


        res = 0
        i = 0
        while i < n:
            if arr1[i]:
                i+=k
                res += 1
            elif arr2[i]:
                i+=k+1
                res += 1
            else:
                i+=1
        return res