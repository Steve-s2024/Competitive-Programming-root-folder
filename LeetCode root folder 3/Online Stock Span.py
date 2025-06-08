# mono-stack: 76%
class StockSpanner:

    def __init__(self):
        self.stack = [(0, float('inf'))]
        self.cnt = 0

    def next(self, price: int) -> int:
        stack = self.stack
        self.cnt += 1
        while stack and stack[-1][1] <= price:
            stack.pop()
        res = self.cnt-stack[-1][0]
        stack.append((self.cnt, price))
        return res

