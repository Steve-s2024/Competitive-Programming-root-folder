# 一开始理解错题意， 写出来了第一部分（三个字母都出现的情况下）。 之后将错就错直接分类讨论了两个字母和一个字母的情况。
class Solution:
    def longestBalanced(self, s: str) -> int:
        arr = [0, 0, 0]
        mp = {}
        mp[(0, 0)] = -1
        res = 0
        for i in range(len(s)):
            cur = ord(s[i]) - ord('a')
            arr[cur] += 1
            a, b = arr[1] - arr[0], arr[2] - arr[1]
            if (a, b) in mp:
                res = max(res, i - mp[(a, b)])
            else:
                mp[(a, b)] = i

        # we have the longest substring for a, b, c all exist

        # now find the longest substring for two of them exist and one of them exist
        def helper(c1, c2, s):
            arr = [0, 0]
            mp = {}
            mp[0] = -1
            res = 0
            for i in range(len(s)):
                if s[i] == c1: arr[0] += 1
                if s[i] == c2: arr[1] += 1
                if s[i] not in [c1, c2]:
                    mp.clear()
                    mp[0] = i
                    arr = [0, 0]
                    continue
                a = arr[1] - arr[0]
                if a in mp:
                    res = max(res, i - mp[a])
                else:
                    mp[a] = i

            return res

        res = max(res,
                  helper('a', 'b', s),
                  helper('a', 'c', s),
                  helper('b', 'c', s)
                  )

        # now for only one element exist
        cnt = 1
        res = max(res, 1)
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                cnt = 1
            else:
                cnt += 1
            res = max(cnt, res)

        return res