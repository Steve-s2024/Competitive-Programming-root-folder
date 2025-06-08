class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        hashMap = defaultdict(int)
        for row in wall:
            total = 0
            for col in row[:-1]:
                total += col
                hashMap[total] += 1

        if len(hashMap) == 0:
            return len(wall)
        return len(wall) - max(hashMap.values())