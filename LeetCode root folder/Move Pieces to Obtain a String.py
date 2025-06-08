# simple two pointer's approach, by LeetCode tip: 79%
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        start += '_'
        target += '_'
        i1, i2 = 0, 0
        while True:
            while i1 < n and start[i1] == '_':
                i1+=1
            while i2 < n and target[i2] == '_':
                i2+=1
            
            if i1 >= n or i2 >= n:
                break
            if (
                start[i1] != target[i2] or 
                (start[i1] == 'L' and i1 < i2) or
                (start[i1] == 'R' and i1 > i2)
            ):
                return False
            
            i1+=1
            i2+=1

        return i1 == i2
        
    
            


# pairing and varify: 32%
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start += '_'
        target += '_'
        i1, i2 = 0, 0
        n = len(start)
        pairs = []
        while True:
            while i1 < n and start[i1] == '_':
                i1+=1
            while i2 < n and target[i2] == '_':
                i2+=1
            if i1 >= n or i2 >= n:
                break
            if start[i1] != target[i2]:
                return False
            pairs.append((i1, i2, start[i1]))
            i1+=1
            i2+=1
        
        if i1 != i2:
            return False
        # print(pairs)

        for i in range(len(pairs)):
            if (
                (pairs[i][2] == 'R' and pairs[i][1] < pairs[i][0]) or
                (pairs[i][2] == 'L' and pairs[i][1] > pairs[i][0])
            ):
                return False
            if (
                i > 0 and
                pairs[i-1][2] == 'R' and pairs[i][2] == 'L' and 
                pairs[i-1][1] >= pairs[i][1]
            ):
                return False
        return True

            
            
