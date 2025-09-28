#返回贪心第二题： 27%

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda i: i[1])
        n = len(courses)
        res = n
        maxheap = []
        t = 0
        for i in range(n):
            heappush(maxheap, -courses[i][0])
            t += courses[i][0]
            if t > courses[i][1]:
                t += heappop(maxheap)
                res -= 1

        return res