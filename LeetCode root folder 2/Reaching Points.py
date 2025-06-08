# the optimized for loop version of the recursive attempt
# its interesting how viewing the problem from forward, backward
# can change the complexity so much: 100%

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:

        while tx >= sx and ty >= sy:
            # print(tx, ty)
            if tx == sx and ty == sy:
                return True
            if tx == ty:
                return False
            elif tx > ty:
                if ty == sy and (tx - sx) % ty == 0:
                    return True
                diff = tx - ty
                rdce = math.ceil(diff / ty) * ty
                tx -= rdce
            elif ty > tx:
                if tx == sx and (ty - sy) % tx == 0:
                    return True
                diff = ty - tx
                rdce = math.ceil(diff / tx) * tx
                ty -= rdce
            # print(tx, ty)
            # print()

        return False

# swapping comparison, or reversing the order, somehow magically changed
# the complexity from 2^n to linear... interesting
# but the code will get maximum recursion depth exceeded
# so we need to use a for loop instead
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        def recursive(x, y):
            if x < sx or y < sy:
                return False
            if x == sx and y == sy:
                return True
            if x > y:
                return recursive(x-y, y)
            else:
                return recursive(x, y-x)
        return recursive(tx, ty)

# recursive brute force: RE, maximum recursion depth exceeded
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        def recursive(x, y):
            if x > tx or y > ty:
                return False
            if x == tx and y == ty:
                return True
            return (
                recursive(x+y, y) or
                recursive(x, x+y)
            )
        return recursive(sx, sy)