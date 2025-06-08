# easy simulation, easier than Robot Bounded In Circle, and
# this is even rated 1846: 60%
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        st = set()
        for r, c in obstacles:
            st.add((r, c))
        res = 0
        mp = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r, c = 0, 0
        d = 0
        n = len(commands)
        for i in range(n):
            com = commands[i]
            if com == -1:
                d = (d + 1) % 4
            elif com == -2:
                d = ((d + 4) - 1) % 4
            else:
                rr, cc = mp[d]
                for i in range(com):
                    if (r+rr, c+cc) in st:
                        break
                    r += rr
                    c += cc
            res = max(res, pow(r, 2)+pow(c, 2))
        return res

