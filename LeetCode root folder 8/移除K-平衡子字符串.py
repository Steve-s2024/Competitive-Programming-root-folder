# a very hard question in first encounter, a compression of parenthesis stack use.
class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        stk = []
        arr = []
        cnt1, cnt2 = 0, 0
        for i, c in enumerate(s):
            if c == '(':
                cnt1 += 1
                if cnt2:
                    if stk and stk[-1] < 0:
                        stk[-1] += cnt2
                    else:
                        stk.append(cnt2)
                    cnt2 = 0
            else:
                if cnt1:
                    if stk and stk[-1] > 0:
                        stk[-1] += cnt1
                    else:
                        stk.append(cnt1)
                    cnt1 = 0
                cnt2 -= 1
                if -cnt2 == k:
                    if stk and stk[-1] >= k:
                        arr.append(i)
                        stk[-1] -= k
                        cnt2 = 0

                        if stk[-1] == 0:
                            stk.pop()
                            while stk and stk[-1] < 0: cnt2 += stk.pop()

            # print(stk)
        print(arr)

        st = set()
        stk = []
        cch = []
        j = 0
        for i in range(len(s)):
            if s[i] == '(':
                stk.append(i)
            else:
                if stk: cch.append((stk.pop(), i))
            if j < len(arr) and i == arr[j]:
                for _ in range(k):
                    l, r = cch.pop()
                    st.add(l)
                    st.add(r)
                j += 1

        strarr = []
        for i in range(len(s)):
            if i not in st: strarr.append(s[i])
        return ''.join(strarr)