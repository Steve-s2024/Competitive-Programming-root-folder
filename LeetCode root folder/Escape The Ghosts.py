# greedy solution: 0 ms beats 100%
# nice little brain-teaser
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        myDist = abs(target[0]) + abs(target[1])
        for x, y in ghosts:
            ghostDist = abs(target[0] - x) + abs(target[1] - y)
            if ghostDist <= myDist:
                return False
        return True