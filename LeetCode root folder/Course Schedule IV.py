# 让人摸不着头脑， 什么情况?? it is thousands of time faster
# just by change the string into sets...: 44%
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        rec = [[] for i in range(numCourses)]
        for prereq, course in prerequisites:
            rec[prereq].append(course)
        
        ref = {}
        
        def dfs(prereq):
            if prereq in ref:
                s = ref[prereq]
                s.add(prereq)
                return s

            s = set()
            for nextPrereq in rec[prereq]:
                s = s.union(dfs(nextPrereq))
            ref[prereq] = s
            s.add(prereq)
            return s

        for i in range(numCourses):
            dfs(i)
        
        # print(ref)
        ans = []
        for p, c in queries:
            ans.append(c in ref[p])
        return ans
        
        


# brute-force: TLE
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # this record hashMap stores the prereqs hashMap, where prereqs hashMap map course id to all its subcourses 
        rec = [[] for i in range(numCourses)]
        for prereq, course in prerequisites:
            rec[prereq].append(course)
        
        def dfs(prereq, course):
            if prereq == course:
                return True
            for nextPrereq in rec[prereq]:
                if dfs(nextPrereq, course):
                    return True
            return False

        ans = []
        for p, c in queries:
            ans.append(dfs(p, c))
        
        return ans
  
# brute-force no.2: TLE
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        rec = [[] for i in range(numCourses)]
        for prereq, course in prerequisites:
            rec[prereq].append(course)
        
        ref = {}
        
        def dfs(prereq):
            if prereq in ref:
                return ref[prereq] + str(prereq)

            s = ''
            for nextPrereq in rec[prereq]:
                s += dfs(nextPrereq)
            ref[prereq] = s
            return s + str(prereq)

        for i in range(numCourses):
            dfs(i)
        
        # print(ref)
        ans = []
        for p, c in queries:
            ans.append(str(c) in ref[p])
        return ans
        
        