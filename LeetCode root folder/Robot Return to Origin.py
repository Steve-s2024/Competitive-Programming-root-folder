class Solution:
    def judgeCircle(self, moves: str) -> bool:
        hor, ver = 0, 0
        for move in moves:
            if move == 'R':
                hor += 1
            elif move == 'L':
                hor -= 1
            elif move == 'U':
                ver += 1
            elif move == 'D':
                ver -= 1
        return hor == 0 and ver == 0