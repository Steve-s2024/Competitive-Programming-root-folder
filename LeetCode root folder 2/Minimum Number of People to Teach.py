

# depricated
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        hashMap = {}
        for i in range(len(languages)):
            hashMap[i] = set(languages[i])
        

        graph = defaultdict(set)
        for a, b in friendships:
            a -= 1
            b -= 1
            for lan in languages[a]:
                if lan in hashMap[b]:
                    break
            else:
                graph[a].add(b)
                graph[b].add(a)
        def checkValid():
            for val in graph.values():
                if val:
                    return False
            return True

        def dfs(i):
            if i >= n:
                if checkValid():
                    return 0        
                return float('inf')
            res = float('inf')
            for friend in graph[i]:
                for lan in hashMap[friend]:
                    graph[i].remove(friend)
                    graph[friend].remove(i)
                    hashMap[i].add(lan)  
                    res = min(res, dfs(i)+1)
                    hashMap[i].remove(lan)
                    graph[friend].add(i)
                    graph[i].add(friend)
            return res
        return dfs(0)

                
                
                
        