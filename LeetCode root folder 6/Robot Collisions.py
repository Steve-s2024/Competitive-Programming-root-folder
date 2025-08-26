# stack solution: 13%
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        arr = [[positions[i], i, healths[i], directions[i]] for i in range(n)]
        arr.sort(key = lambda i:i[0])
        ans = []
        stack = []
        for i in range(n):
            if arr[i][3] == 'R':  stack.append([arr[i][2], arr[i][1]])
            else:
                while stack:
                    health, _ = stack[-1]
                    if health == arr[i][2]:
                        stack.pop()
                        arr[i][2] = 0
                        break
                    elif health < arr[i][2]:
                        stack.pop()
                        arr[i][2] -= 1
                    else:
                        stack[-1][0] -= 1
                        arr[i][2] = 0
                        break
                if arr[i][2]:
                    ans.append([arr[i][2], arr[i][1]])

        ans += stack
        print(ans)
        ans.sort(key = lambda i:i[1])
        return [e[0] for e in ans]
