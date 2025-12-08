# this is the most disgusting solution I've ever wrote. my headache is killing me
def check(arr, tar):
    strarr = []
    for i in range(26 - 1, -1, -1):
        for j in range(arr[i]): strarr.append(chr(ord('a') + i))
    return ''.join(strarr) > tar


class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        arr = [0] * 26
        for c in s: arr[ord(c) - ord('a')] += 1
        ct = 0
        for val in arr: ct += val % 2
        if ct > 1 or ct == 1 and n % 2 == 0 or ct == 0 and n % 2 == 1: return ''

        c = ''
        if n % 2 == 1:
            for i in range(26):
                if arr[i] % 2:
                    c = chr(ord('a') + i)
                    break
        for i in range(26): arr[i] = arr[i] // 2
        # print(arr)

        strarr = []
        for i in range(26):
            for j in range(arr[i]): strarr.append(chr(ord('a') + i))
        t = ''.join(strarr) + c + ''.join(strarr)[::-1]
        if t > target: return t

        cp = arr[:]
        strarr = []
        for i in range(n // 2):
            o = ord(target[i]) - ord('a')
            if not cp[o]: break
            cp[o] -= 1
            strarr.append(chr(ord('a') + o))
        t = ''.join(strarr) + c + ''.join(strarr)[::-1]
        if len(t) == n and t > target: return t

        ans = []
        target = target[:n // 2]
        for i in range(n // 2):
            o = ord(target[i]) - ord('a')
            idx = -1
            for j in range(26):
                if arr[j] and j >= o:
                    idx = j
                    break
            if idx == -1: return ''

            if idx > o:
                ans.append(chr(ord('a') + idx))
                arr[idx] -= 1
                strarr = []
                for i in range(26):
                    for j in range(arr[i]): strarr.append(chr(ord('a') + i))
                return ''.join(ans + strarr) + c + ''.join(ans + strarr)[::-1]
            else:
                arr[idx] -= 1
                if check(arr, target[i + 1:]):
                    ans.append(chr(ord('a') + idx))
                else:
                    arr[idx] += 1
                    idx = -1
                    for j in range(26):
                        if arr[j] and j > o:
                            idx = j
                            break
                    if idx == -1: return ''
                    ans.append(chr(ord('a') + idx))
                    arr[idx] -= 1
                    strarr = []
                    for i in range(26):
                        for j in range(arr[i]): strarr.append(chr(ord('a') + i))
                    return ''.join(ans + strarr) + c + ''.join(ans + strarr)[::-1]

        return ''