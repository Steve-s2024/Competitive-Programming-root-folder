# suffix trie and dfs implementation, hard but somewhat intuitive: 75%
class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = {}
        for idx, word in enumerate(wordsContainer):
            cur = trie
            for c in word[::-1]:
                if c not in cur: cur[c] = {}
                cur = cur[c]
            if 'end' not in cur:
                cur['end'] = idx
            else:
                cur['end'] = min(cur['end'], idx)

        def dfs(node):
            if isinstance(node, int): return 0, node
            minDep = inf
            i = inf
            for nxt in node:
                dep, idx = dfs(node[nxt])
                if dep < minDep:
                    minDep, i = dep, idx
                elif dep == minDep:
                    i = min(i, idx)
            node['*'] = i
            return minDep + 1, i

        dfs(trie)

        ans = []
        for word in wordsQuery:
            cur = trie
            for c in word[::-1]:
                if c in cur:
                    cur = cur[c]
                else:
                    break
            ans.append(cur['*'])

        return ans