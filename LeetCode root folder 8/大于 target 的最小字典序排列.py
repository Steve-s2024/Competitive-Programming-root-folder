# 到最后还是模拟然后假设取某个值之后看剩下的字符能不能保证字典序还是大于target， 极低的限制允许这样去模拟
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        mp = Counter(s)
        n = len(target)
        ans = []
        for i in range(n):
            tmp = []
            for key, val in mp.items():
                if val and key >= target[i]: tmp.append(key)
            # print(tmp)
            res = 'zz'
            for e in tmp:
                mp[e] -= 1
                chars = []
                for key, val in mp.items():
                    for _ in range(val): chars.append(key)
                chars.sort(reverse=True)
                string = ''.join(chars)
                if e > target[i] or string > target[i + 1:]:
                    res = min(res, e)
                mp[e] += 1
            # print(res)
            if res == 'zz': return ''
            ans.append(res)
            mp[res] -= 1
            if res > target[i]:
                arr = []
                for key, val in mp.items():
                    for _ in range(val): arr.append(key)
                return ''.join(ans) + ''.join(sorted(arr+['']))
        string = ''.join(ans)
        if string == target: return ''
        return string