# really tricky, need to spot the atomic operation implied by the given operation
# first time realize that the atomic operation of sorting arbitrary subarray is just:
# "move nums[i] one position to right if nums[i+1] is smaller than it"

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        mp = Counter(s)
        for k, v in Counter(t).items():
            if k not in mp or mp[k] != v: return False

        n = len(s)
        mp = defaultdict(list)
        for i in range(n): mp[s[i]].append(i)

        s = list(s)
        idx = n - 1
        for i in range(n - 1, -1, -1):
            while idx >= 0 and s[idx] == '': idx -= 1
            if idx < 0: return False
            x = t[i]
            if s[idx] == x:
                mp[x].pop()
                idx -= 1
            else:
                for j in range(int(x) + 1, 10):
                    if mp[str(j)] and mp[str(j)][-1] > mp[x][-1]: return False
                s[mp[x].pop()] = ''

        return True
