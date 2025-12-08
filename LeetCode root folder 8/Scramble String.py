# another nightmare conquered. doesn't feel so hard now, but definitely not easy. not to mention i get lucky to
# come up with this solution (which initially make no intuitive sense to me at first)

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def recursive(la, ra, lb, rb):
            if la == ra: return s1[la] == s2[lb]
            res = False
            for i in range(la, ra):
                a = recursive(la, i, lb, lb+(i-la)) and recursive(i+1, ra, lb+(i-la)+1, rb)
                b = recursive(la, i, rb-(i-la), rb) and recursive(i+1, ra, lb, rb-(i-la)-1)
                res = res or (a or b)
            # print(la, ra, lb, rb, res)
            return res
        return recursive(0, len(s1)-1, 0, len(s2)-1)