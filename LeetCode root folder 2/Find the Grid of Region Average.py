


# brute force: TLE
class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        row, col = len(image), len(image[0])
        ans = []
        for rw in image:
            ans.append(rw[:])
        hashMap = {}
        def markCell(R, C):
            total = 0
            for r in range(R, R+3):
                for c in range(C, C+3):
                    if (
                        r < R+2 and abs(image[r+1][c] - image[r][c]) > threshold or
                        c < C+2 and abs(image[r][c+1] - image[r][c]) > threshold
                    ):
                        return
                    total += image[r][c]
            avrg = total // 9
            for r in range(R, R+3):
                for c in range(C, C+3):
                    if (r, c) in hashMap:
                        hashMap[(r, c)] += 1
                        ans[r][c] += avrg
                    else:
                        hashMap[(r, c)] = 1
                        ans[r][c] = avrg

        for r in range(row-2):
            for c in range(col-2):
                markCell(r, c)
        for r in range(row):
            for c in range(col):
                if (r, c) in hashMap:
                    ans[r][c] //= hashMap[(r, c)]

        return ans
