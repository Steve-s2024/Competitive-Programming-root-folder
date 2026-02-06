# holy shit didn't expect this to pass all testcases. 10 seconds run time
# O(10kn), 9million in worst case
# to be accurate it is actually O(10/2kn), so 4.5 mill at most
class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        if n == 1:
            x = k
            while x+k < 10: x += k
            return str(x)

        ar = [[0] * 10 for _ in range(n)]
        x = 1
        for i in range(n - 1, -1, -1):
            for j in range(1, 10):
                ar[i][j] = (j * x) % k
            x *= 10
            x %= k

        # print(ar)
        @cache
        def recursive(i, re):
            if i >= n // 2:
                if n % 2 == 0: return -1 if re != 0 else 0
                else:
                    x = -1
                    for v, y in enumerate(ar[i]):
                        if (y+re)%k == 0: x = v
                    return x

            res = -1
            for j in range(10):
                a = recursive(i + 1, (re + ar[i][j] + ar[n - i - 1][j]) % k)
                if a != -1: res = j
            return res

        cri, crre = 0, 0
        ans = []
        for v in range(1, 10):
            a = recursive(1, (ar[0][v] + ar[-1][v])%k)
            if a != -1:
                # print(v, a, ar[1], (ar[0][v] + ar[-1][v])%k)
                cri, crre = 1, (ar[0][v] + ar[-1][v])%k
                ans = [v]
        # print(cri, crre, ans)
        while cri < (n + 1) // 2:
            j = recursive(cri, crre)
            ans.append(j)
            cri, crre = cri + 1, (crre + ar[cri][j] + ar[n - cri - 1][j]) %k

        # print(ans)
        s = ''.join(str(e) for e in ans)
        return s + s[::-1][n%2:]



# seriously.... added a few lines of additional checking at the beginning, and freaking speed up the solution for 4 seconds
class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:

        if n == 1:
            x = k
            while x+k < 10: x += k
            return str(x)

        if k == 1: return '9'*n
        if k == 2: return '8' + '9'*(n-2) + '8'
        if k == 3: return '9'*n
        if k == 5: return '5' + '9'*(n-2) + '5'
        if k == 9: return '9'*n

        ar = [[0] * 10 for _ in range(n)]
        x = 1
        for i in range(n - 1, -1, -1):
            for j in range(1, 10):
                ar[i][j] = (j * x) % k
            x *= 10
            x %= k

        # print(ar)
        @cache
        def recursive(i, re):
            if i >= n // 2:
                if n % 2 == 0: return -1 if re != 0 else 0
                else:
                    x = -1
                    for v, y in enumerate(ar[i]):
                        if (y+re)%k == 0: x = v
                    return x

            res = -1
            for j in range(10):
                a = recursive(i + 1, (re + ar[i][j] + ar[n - i - 1][j]) % k)
                if a != -1: res = j
            return res

        cri, crre = 0, 0
        ans = []
        for v in range(1, 10):
            a = recursive(1, (ar[0][v] + ar[-1][v])%k)
            if a != -1:
                # print(v, a, ar[1], (ar[0][v] + ar[-1][v])%k)
                cri, crre = 1, (ar[0][v] + ar[-1][v])%k
                ans = [v]
        # print(cri, crre, ans)
        while cri < (n + 1) // 2:
            j = recursive(cri, crre)
            ans.append(j)
            cri, crre = cri + 1, (crre + ar[cri][j] + ar[n - cri - 1][j]) %k

        # print(ans)
        s = ''.join(str(e) for e in ans)
        return s + s[::-1][n%2:]
