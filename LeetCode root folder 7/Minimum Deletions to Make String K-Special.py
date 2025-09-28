# boring low rating question: 28%
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        mp = Counter(word)
        arr = list(mp.values())
        arr.sort()
        n = len(arr)
        res = inf
        for i in range(n):
            tot = sum(arr[:i]) if i else 0
            for j in range(n):
                if arr[j] > arr[i]+k: tot += arr[j] - arr[i]-k
            res = min(tot, res)
        return res