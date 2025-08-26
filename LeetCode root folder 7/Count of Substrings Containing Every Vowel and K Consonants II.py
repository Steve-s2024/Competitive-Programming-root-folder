# sometimes I am really amazed by myself. one pass solution, took 30 minutes. 2200 rated: 57%
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        arr = []
        cnt = 0
        for i in range(n):
            arr.append(cnt)
            if word[i] in 'aeiou':
                cnt += 1
            else:
                cnt = 0

        mp = defaultdict(int)
        cnt = 0
        j = 0
        res = 0
        for i in range(n):
            if word[i] in 'aeiou':
                mp[word[i]] += 1
            else:
                cnt += 1
            old = j
            while j < n and len(mp) == 5 and cnt >= k:
                if word[j] in 'aeiou':
                    mp[word[j]] -= 1
                    if mp[word[j]] == 0: mp.pop(word[j])
                else:
                    cnt -= 1
                j += 1
            if j != old:
                j -= 1
                if word[j] in 'aeiou':
                    mp[word[j]] += 1
                else:
                    cnt += 1
            if len(mp) == 5 and cnt == k: res += arr[j] + 1
        return res