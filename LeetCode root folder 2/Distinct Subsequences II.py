# dp solution with hashMap as the return type: TLE
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        idxMp = defaultdict(int)
        cntArr = [[-1]*26 for i in range(n)]
        for i in range(n-1, -1, -1):
            for key, val in idxMp.items():
                j = ord(key) - ord('a')
                cntArr[i][j] = val
            val = s[i]
            idxMp[val] = i
        # print(cntArr)
        dp = {}
        dp[n] = defaultdict(int)
        MOD = 1000000007
        def dfs(i):
            nonlocal MOD
            if i in dp:
                return dp[i]
            res = defaultdict(int)
            res[1] += 1
            for j in cntArr[i]:
                if j != -1:
                    mp = dfs(j)
                    for key, val in mp.items():
                        res[key+1] += val % MOD
            dp[i] = res
            return res
        res = 0
        for i in range(len(cntArr[0])):
            if i == ord(s[0])-ord('a'):
                tmp = dfs(0)
                # print(i, tmp)
                res += sum(tmp.values())
            elif cntArr[0][i] != -1:
                tmp = dfs(cntArr[0][i])
                # print(i, tmp)
                res += sum(tmp.values())
        return res % MOD
            
            

# brute force solution with preprocess: TLE
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        idxMp = defaultdict(int)
        cntArr = [[-1]*26 for i in range(n)]
        for i in range(n-1, -1, -1):
            for key, val in idxMp.items():
                j = ord(key) - ord('a')
                cntArr[i][j] = val
            val = s[i]
            idxMp[val] = i
        # print(cntArr)

        sizeMp = defaultdict(int)
        def dfs(i, size):
            if i >= n:
                return
            sizeMp[size] += 1
            for j in cntArr[i]:
                if j != -1:
                    dfs(j, size+1)
            return 1
        for i in range(len(cntArr[0])):
            if i == 0:
                dfs(0, 1)
            elif cntArr[0][i] != -1:
                dfs(cntArr[0][i], 1)
        return sum(sizeMp.values())