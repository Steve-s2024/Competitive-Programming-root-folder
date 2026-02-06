# the pure greedy solution, linear
class Solution:
    def intersectionSizeTwo(self, itv: List[List[int]]) -> int:
        itv.sort(key = lambda i:i[1])
        n = len(itv)
        st = set()
        ar = []
        for i in range(n):
            l, r = itv[i]
            t = 0
            for j in range(len(ar)-1, max(len(ar)-4, -1), -1):
                if ar[j] >= l: t += 1

            for x in [r, r-1]:
                if t >= 2: break
                if x in st: continue
                st.add(x)
                t += 1
                ar.append(x)
        # print(st)
        return len(st)


# think about how to approach for a containing set of 1 element per interval, translate that idea into 2 elements per interval
# with the help of a frequency array
class Solution:
    def intersectionSizeTwo(self, itv: List[List[int]]) -> int:
        itv.sort()
        itv.append([inf, inf]) # terminator
        n = len(itv)
        ar = [2]*n
        hp = []
        st = set()
        for i in range(n):
            l, r = itv[i]
            while hp and hp[0][0] < l:
                if ar[hp[0][1]] <= 0:
                    heappop(hp)
                    continue
                R, j = hp[0]
                if R not in st:
                    st.add(R)
                    for _, i_ in hp: ar[i_] -= 1
                if R-1 not in st and ar[j] > 0:
                    st.add(R-1)
                    ar[j] -= 1
                    for _, i_ in hp:
                        l_, r_ = itv[i_]
                        if R-1 in range(l_, r_+1): ar[i_] -= 1
            # print((l, r), hp)
            heappush(hp, (r, i))
        # print(ar[:-1])
        # print(st)
        return len(st)