# can't believe that this end up being a Dijkstra problem.
# so wierd that I cannot even see a bit of it until I read through some of the comments
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        mih = [(nums1[0] + nums2[0], 0, 0)]
        ans = []
        vis = set()
        for _ in range(k):
            x, i, j = heappop(mih)
            ans.append((nums1[i], nums2[j]))
            if i < len(nums1) - 1 and (i + 1, j) not in vis:
                vis.add((i + 1, j))
                heappush(mih, (nums1[i + 1] + nums2[j], i + 1, j))
            if j < len(nums2) - 1 and (i, j + 1) not in vis:
                vis.add((i, j + 1))
                heappush(mih, (nums1[i] + nums2[j + 1], i, j + 1))

        return ans