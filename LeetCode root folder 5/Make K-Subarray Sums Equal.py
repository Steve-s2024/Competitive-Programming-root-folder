# completely gambled this GCD solution: 83%
class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        n = len(arr)
        res = 0
        k = math.gcd(n, k)
        for i in range(k):
            tmp = []
            for j in range(i, n, k): tmp.append(arr[j])
            tmp.sort()
            size = len(tmp)
            mid = tmp[size // 2]
            for num in tmp: res += abs(mid - num)

        return res


# failed attempt
class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        n = len(arr)
        res = 0

        # scenario1 -> n%k == 0
        # find the best way to make every 0, k, 2*k... equal, every 1, k+1, 2*k+1... equal, every 2, k+2, 2*k+2... equal
        if n % k == 0:
            for i in range(k):
                tmp = []
                for j in range(i, n, k): tmp.append(arr[j])
                tmp.sort()
                size = len(tmp)
                mid = tmp[size // 2]
                for num in tmp: res += abs(mid - num)

        # scenario2 -> n%k != 0
        # find the best way to make every element equal
        else:
            arr.sort()
            size = n
            mid = arr[size // 2]
            for num in arr: res += abs(mid - num)

        return res