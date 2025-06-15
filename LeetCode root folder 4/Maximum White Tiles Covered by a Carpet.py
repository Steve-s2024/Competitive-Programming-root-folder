# I think I am making it unnecessarily complicated, especially the last part
# to compute the cover tiles: 5%
# it could've been much simpler if I realize sliding window can replace
# the computation code and the binary search...


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort(key=lambda i: i[0])
        n = len(tiles)
        stack = []
        for i in range(n):
            l, r = tiles[i]
            while stack and stack[-1][1] == l - 1:
                L, R = stack.pop()
                l = L
            stack.append((l, r))
        # print(stack)

        pre = []
        tot = 0
        for l, r in stack:
            size = r - l + 1
            tot += size
            pre.append(tot)

        n = len(stack)
        res = 0
        # print(stack)
        for i in range(n):
            x = stack[i][0] + carpetLen - 1

            l, r = 0, n - 1
            right = -1
            while l <= r:
                m = (l + r) // 2
                if stack[m][1] <= x:
                    right = m
                    l = m + 1
                else:
                    r = m - 1

            l, r = 0, n - 1
            left = -1
            while l <= r:
                m = (l + r) // 2
                if stack[m][0] <= x:
                    left = m
                    l = m + 1
                else:
                    r = m - 1

            # print(x, left, right)
            if left != -1:
                a = (stack[i][1] - stack[i][0] + 1)
                b = (stack[left][1] - stack[left][0] + 1)
                c = (min(stack[left][1], stack[i][0] + carpetLen - 1) - stack[left][0] + 1)
                tmp = pre[left] - pre[i] + a - b + c
                res = max(tmp, res)
            if right != -1 and right >= i:
                a = (stack[i][1] - stack[i][0] + 1)
                tmp = pre[right] - pre[i] + a
                res = max(tmp, res)
        return res
