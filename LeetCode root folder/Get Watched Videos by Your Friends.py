# bfs solution:19
# ms
# Beats
# 75.23%
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> \
    List[str]:
        visited = set()
        q = deque([id])
        visited.add(id)
        depth = 0
        while q:
            if depth == level:
                break
            l = len(q)
            while l:
                cur = q.popleft()
                for next_ in friends[cur]:
                    if next_ not in visited:
                        visited.add(next_)
                        q.append(next_)
                l -= 1
            depth += 1

        # print(q)
        hashMap = defaultdict(int)
        for person in q:
            for video in watchedVideos[person]:
                hashMap[video] += 1
        # print(hashMap)

        ans = []
        for key, val in hashMap.items():
            ans.append((key, val))

        ans.sort(key=lambda i: (i[1], i[0]))
        # print(ans)
        for i in range(len(ans)):
            ans[i] = ans[i][0]
        return ans
