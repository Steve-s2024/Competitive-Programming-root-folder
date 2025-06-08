# greedy solution:287
# ms
# Beats
# 6.58%
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans = [[-1, -1] for i in range(len(people))]
        people.sort(key=lambda i: i[0])
        # print(people)
        for h, c in people:
            total = 0
            for i in range(len(ans)):
                if total >= c and ans[i][0] == -1:
                    ans[i] = [h, c]
                    break
                if ans[i][0] >= h or ans[i][0] == -1:
                    total += 1

        # print(ans)
        return ans

