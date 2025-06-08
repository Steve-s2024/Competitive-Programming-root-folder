# graph & linked list and cycle detection solution:211
# ms
# Beats
# 21.01%
# the tricky part of the solution is to come up with the theory of finding the number of swap to make an array
# sorted. but I have manage to come up with the correct theory that the minimum number of swap required is always the
# number of misplaced element in the array minus 1, and the misplaced elements always form clusters that are kind of
# like cycled linked-list.
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        nums = []
        while q:
            l = len(q)
            nums.append([])
            while l:
                cur = q.popleft()
                nums[-1].append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                l -= 1
        # print(nums)
        visited = set()

        def traverseLinklist(i, length, hashMap):
            if i in visited:
                return length
            visited.add(i)
            return traverseLinklist(hashMap[row[i]], length + 1, hashMap)

        res = 0
        for row in nums:
            hashMap = defaultdict(int)
            sortedRow = sorted(row)
            visited.clear()
            for i in range(len(sortedRow)):
                hashMap[sortedRow[i]] = i

            for i in range(len(row)):
                if hashMap[row[i]] != i:  # misplaced
                    if i not in visited:  # if the cluster is not visited, count the size of it
                        size = traverseLinklist(i, 0, hashMap)
                        # print(row, i, size)
                        res += size - 1

        return res

