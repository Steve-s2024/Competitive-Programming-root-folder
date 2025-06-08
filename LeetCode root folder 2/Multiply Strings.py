# solution no.1: 5%
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        pairs = []
        n, m = len(num1), len(num2)
        for i in range(n):
            for j in range(m):
                # times num1[i] with num2[j]
                a, b = int(num1[i]), int(num2[j])
                prod = a * b
                zeros = (n - 1 - i) + (m - 1 - j)
                pairs.append((prod, zeros))

        # print(pairs)
        hashMap = defaultdict(list)
        for prod, zeros in pairs:
            hashMap[zeros].append(prod)

        res = deque([])
        i = 0
        while i <= n * m:
            zeroCnt = i
            if zeroCnt in hashMap:
                sm = sum(hashMap[zeroCnt])
                remain = sm % 10
                res.appendleft(str(remain))
                sm -= remain
                sm //= 10
                hashMap[zeroCnt + 1].append(sm)
            i += 1

        # print(res)
        while len(res) > 1 and res[0] == '0':
            res.popleft()
        return ''.join(res)

