# non-necessary solution, because it's too good...

'''class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        dp = [[] for i in range(len(s))]
        dp.append([''])
        for i in range(len(s) - 1, -1, -1):
            idx = i
            string = ''
            while True:
                if idx >= len(s):
                    break
                string += s[idx]
                if int(string) > 255:
                    break
                for seq in dp[idx + 1]:
                    if seq != '':
                        newSeq = string + '.' + seq
                    else:
                        newSeq = string
                    if newSeq.count('.') <= 3:
                        dp[i].append(newSeq)
                idx += 1
        # print(dp)
        res = []
        for seq in dp[0]:
            if seq.count('.') == 3:
                res.append(seq)
        return res'''

# back-tracking solution
# easy to implement, but not so good. however it will only generate the ip addresses LeetCode want
# 26
# ms
# Beats
# 7.95%
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def dfs(seq, count, s):
            if count == 4 and len(s) == 0:
                res.append(seq[1:])
                return
            if len(s) == 0:
                return
            string = ''
            idx = 0
            while idx < len(s):
                string += s[idx]
                if int(string) > 255:
                    break
                if (
                    not (int(string) != 0 and string[0] == '0') and
                    not (int(string) == 0 and len(string) != 1)
                ):
                    dfs(seq + '.' + string, count + 1, s[idx + 1:])
                idx += 1
        dfs('', 0, s)
        # print(res)
        return res
