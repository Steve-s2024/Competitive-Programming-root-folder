# Union find solution:3
# ms
# Beats
# 63.10%
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        hashMap = defaultdict(list)
        # hashMap[i] = [val, [groupMembers...]]
        # when encounter "n1==n2", build up an undirected connection between n1 and n2.
        # after the connections constructed, i have a undirected graph of clusters, element from one cluster must be the same number as each other, element from different clusters can have the same value or different value.
        # go over the equations and this time when encounter "n1!==n2", check if n1 and n2 belongs to the same cluster, and made the return False statement if needed.
        # after this examination, if the function is still not returned, return True as the default

        for eq in equations:
            if eq[1] == '=':
                # equal
                hashMap[eq[0]].append(eq[3])
                hashMap[eq[3]].append(eq[0])

        visited = set()

        def dfs(val):
            nonlocal groupNum
            if val in visited:
                return
            groupMap[val] = groupNum
            visited.add(val)
            for nextVal in hashMap[val]:
                dfs(nextVal)

        groupMap = {}
        groupNum = 0
        for key in hashMap:
            dfs(key)
            groupNum += 1

        # print(groupMap)
        for eq in equations:
            if (
                    eq[1] == '!' and
                    (
                            (eq[0] in groupMap and eq[3] in groupMap) and
                            groupMap[eq[0]] == groupMap[eq[3]] or
                            eq[0] == eq[3]
                    )
            ):
                return False
        return True
