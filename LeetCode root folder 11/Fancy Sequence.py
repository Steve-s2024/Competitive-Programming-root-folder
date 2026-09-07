# brought prefix array range query to a new difficulty with the help of modulo arithmetic
class Fancy:
    def __init__(self):
        self.mul, self.ar, self.vals, self.mp = [], [], [], []

    def append(self, x: int) -> None:
        mul, ar, vals, mp = self.mul, self.ar, self.vals, self.mp
        vals.append(x)
        ar.append(ar[-1] if ar else 0)
        mul.append(mul[-1] if mul else 1)
        mp.append(len(ar) - 1)

    def addAll(self, x: int) -> None:
        mul, ar, vals, mp = self.mul, self.ar, self.vals, self.mp
        ar.append((ar[-1] if ar else 0) + x)
        mul.append(mul[-1] if mul else 1)

    def multAll(self, m: int) -> None:
        mul, ar, vals, mp = self.mul, self.ar, self.vals, self.mp
        M = 10 ** 9 + 7
        mul.append(((mul[-1] if mul else 1) * m) % M)
        ar.append(((ar[-1] if ar else 0) * m) % M)

    def getIndex(self, idx: int) -> int:
        mul, ar, vals, mp = self.mul, self.ar, self.vals, self.mp
        # print(mul, ar)
        if idx >= len(mp): return -1
        i = mp[idx]
        M = 10 ** 9 + 7

        a, b = mul[i], mul[-1]
        f = (b * pow(a, M - 2, M)) % M

        tp = vals[idx] * f
        x = ar[i] * f
        # print(tp, x, f)
        res = (ar[-1] - x) % M
        return (tp + res) % M
