# brute force, all substring mapped and compared:171
# ms
# Beats
# 73.62%
# wonder why this could be solved by trie, my brute force is already very fast.
class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        hashMap = defaultdict(int)
        for s in arr:
            hashSet = set()
            for i in range(len(s)):
                for j in range(i, len(s)):
                    cur = s[i:j+1]
                    hashSet.add(cur)
            for key in hashSet:
                hashMap[key] += 1
        # print(hashMap)
        ans = []
        for s in arr:
            hashSet = set()
            res = []
            for i in range(len(s)):
                for j in range(i, len(s)):
                    cur = s[i:j+1]
                    if hashMap[cur] == 1:
                        if res and len(cur) < len(res[0]):
                            res.clear()
                            res.append(cur)
                        elif not res or len(res[0]) == len(cur):
                            res.append(cur)
            if res:
                ans.append(sorted(res)[0])
            else:
                ans.append('')
        return ans