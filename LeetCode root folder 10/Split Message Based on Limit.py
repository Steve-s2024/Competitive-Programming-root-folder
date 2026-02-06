# what a boring question, wonder its purpose of existence

class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        n = len(message)
        ar = [0]
        t = 0
        for i in range(1, n):
            t += len(str(i))
            ar.append(t)
        # print(ar)

        for i in range(1, n + 1):
            x = f'<{i}/{i}>'
            if len(x) > limit: return []

            t = ar[i - 1] + (3 + len(str(i))) * (i - 1)
            re = n - (limit * (i - 1) - t)
            # print(i, t, re)
            if re in range(limit - len(x) + 1):
                idx = 0
                ans = []
                for j in range(1, i + 1):
                    x = f'<{j}/{i}>'
                    ar = []
                    for k in range(limit - len(x)):
                        if idx >= n: break
                        ar.append(message[idx])
                        idx += 1
                    ans.append(''.join(ar) + x)
                return ans

                # return [str(i)]
        return []

