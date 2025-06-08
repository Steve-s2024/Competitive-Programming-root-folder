# intuitive two pointer approach, pre-processed one side
# and grow the other side while maintaining the minimum
# first side length required (use hash map to maintain):18%
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        cnts = Counter(s)
        if min(cnts.values()) < k or len(cnts) < 3:
            return -1

        hashMap = defaultdict(int)
        n = len(s)
        l = 0
        while l < n:
            hashMap[s[l]]+=1
            a, b, c = hashMap['a'], hashMap['b'], hashMap['c']
            if min(a, b, c) >= k:
                break
            l += 1
        res = l+1
        
        r = n-1
        # print(l, r)
        while r >= 0:
            hashMap[s[r]]+=1
            while l >= 0:
                hashMap[s[l]]-=1
                a, b, c = hashMap['a'], hashMap['b'], hashMap['c']
                if min(a, b, c) < k:
                    hashMap[s[l]]+=1
                    break
                l-=1
            # print(l, r)
            res = min(res, (l+1) + (n-r))
            r -= 1

        return res