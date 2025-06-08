class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        res = [[0] * len(img[0]) for i in range(len(img))]
        for r in range(len(img)):
            for c in range(len(img[0])):
                total = img[r][c]
                count = 1
                steps = [
                    [1, 0], [-1, 0], [1, 1], [-1, 1],
                    [1, -1], [-1, -1], [0, -1], [0, 1]
                ]
                for rStep, cStep in steps:
                    curR = r + rStep
                    curC = c + cStep
                    if (curR not in range(len(img)) or
                        curC not in range(len(img[0]))
                    ):
                        continue
                    total += img[curR][curC]
                    count += 1
                res[r][c] = floor(total / count)
        return res