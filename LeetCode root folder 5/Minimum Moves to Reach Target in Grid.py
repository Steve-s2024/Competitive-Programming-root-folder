# reverse engineering: incorrect
class Solution:
    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
        cnt = 0
        while tx and ty and tx >= sx and ty >= sy:
            if (tx, ty) == (sx, sy): return cnt
            cnt += 1
            if ty > tx:
                ty -= tx
            elif ty < tx:
                tx -= ty
            else:
                if (0, ty) == (sx, sy) or (tx, 0) == (sx, sy):
                    return cnt
                else:
                    return -1

        if tx == sx and ty == sy: return cnt
        return -1



# brute force knap-sack: MLE
class Solution:
    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
        if max(sx, sy) == 0: return 0 if max(tx, ty) == 0 else -1

        @cache
        def recursive(x, y):
            if x > tx or y > ty: return inf
            if x == tx and y == ty: return 0

            res = min(
                recursive(x+max(x, y), y),
                recursive(x, y+max(x, y))
            )+1
            return res
        res = recursive(sx, sy)
        if res == inf: return -1
        return res