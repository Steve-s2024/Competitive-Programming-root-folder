# funny and casual question. (Q3 of 2025/09/27 contest)
class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        pre = []
        ho, ve = 0, 0
        for c in s:
            if c == 'U':
                ve += 1
            elif c == 'D':
                ve -= 1
            elif c == 'L':
                ho -= 1
            else:
                ho += 1
            pre.append((ho, ve))

        pre.append((0, 0))
        st = set()
        for i in range(len(s) - k + 1):
            l, r = i, i + k - 1
            # pre[r] - pre[l-1]

            hdif, vdif = pre[r][0] - pre[l - 1][0], pre[r][1] - pre[l - 1][1]
            st.add((hdif, vdif))
        # print(st)
        return len(st)