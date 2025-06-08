# pretty slow, both the constructing graph and detecting cycle deserve
# to be hard-medium by them self, the dfs part to build the string is actually
# easy: passed on neetcode, premium on leetcode
class Solution:
    @staticmethod
    def detectCycle(graph):

        def dfs(node):
            visited.add(node)
            for nextNode in graph[node]:
                if nextNode in st:
                    return -1
                st.add(nextNode)
                if dfs(nextNode) == -1:
                    return -1
                st.remove(nextNode)

        visited = set()
        st = set()
        keys = list(graph.keys())
        for key in keys:
            if key not in visited:
                st.add(key)
                if dfs(key) == -1:
                    return True
                st.remove(key)
        return False

    def foreignDictionary(self, words: List[str]) -> str:
        hashSet = set()
        for word in words:
            hashSet = hashSet.union(set(word))
        graph = defaultdict(set)

        n = len(words)

        def recursive(pos, left, right):
            # print(pos, left, right)
            if right - left <= 1:
                return
            while left < right and len(words[left]) <= pos:  # make sure the shortest one is always at the beginning
                left += 1
            prev = ''  # give pseudo value
            l, r = left, left
            for i in range(left, right):
                word = words[i]
                if len(word) <= pos:  # the dictinoary is invalid if this happened
                    # print('invalid')
                    return -1

                if prev == '':
                    prev = word[pos]
                if word[pos] == prev:
                    r += 1
                else:
                    if recursive(pos + 1, l, r) == -1:
                        return -1
                    l = r
                    r += 1
                    graph[word[pos]].add(prev)
                    prev = word[pos]

            if recursive(pos + 1, l, r) == -1:  # the trailing segment
                return -1

        if recursive(0, 0, n) == -1:
            return ''

        if Solution.detectCycle(graph):
            return ''

        res = []
        visited = set()

        def dfs(node):
            for nextNode in graph[node]:
                if nextNode not in visited:
                    visited.add(nextNode)
                    dfs(nextNode)
            res.append(node)

        for key in hashSet:
            if key not in visited:
                visited.add(key)
                dfs(key)
        return ''.join(res)




# included the cycle detection, but not complete.
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        hashSet = set()
        for word in words:
            hashSet = hashSet.union(set(word))
        graph = defaultdict(set)

        n = len(words)

        def recursive(pos, left, right):
            # print(pos, left, right)
            if right - left <= 1:
                return
            while left < right and len(words[left]) <= pos:  # make sure the shortest one is always at the beginning
                left += 1
            prev = ''  # give pseudo value
            l, r = left, left
            for i in range(left, right):
                word = words[i]
                if len(word) <= pos:  # the dictinoary is invalid if this happened
                    # print('invalid')
                    return -1

                if prev == '':
                    prev = word[pos]
                if word[pos] == prev:
                    r += 1
                else:
                    if recursive(pos + 1, l, r) == -1:
                        return -1
                    l = r
                    r += 1
                    graph[word[pos]].add(prev)
                    prev = word[pos]

            if recursive(pos + 1, l, r) == -1:  # the trailing segment
                return -1

        if recursive(0, 0, n) == -1:
            return ''
        print(graph)

        res = []
        visited = set()

        def dfs(node):
            if node in set2:
                return -1
            set2.add(node)
            for nextNode in graph[node]:
                if nextNode not in visited:
                    visited.add(nextNode)
                    if dfs(nextNode) == -1:
                        return -1
            res.append(node)

        for key in hashSet:
            if key not in visited:
                set2 = set()
                visited.add(key)
                if dfs(key) == -1:
                    return ''
        return ''.join(res)


# boring, tried to construct a prerequisite array, and do
# dfs, but didn't implement the cycle detection yet
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        hashSet = set()
        for word in words:
            hashSet = hashSet.union(set(word))
        graph = defaultdict(list)

        n = len(words)

        def recursive(pos, left, right):
            # print(pos, left, right)
            if right - left <= 1:
                return
            while left < right and len(words[left]) <= pos:  # make sure the shortest one is always at the beginning
                left += 1
            prev = ''  # give pseudo value
            l, r = left, left
            for i in range(left, right):
                word = words[i]
                if len(word) <= pos:  # the dictinoary is invalid if this happened
                    # print('invalid')
                    return -1

                if prev == '':
                    prev = word[pos]
                if word[pos] == prev:
                    r += 1
                else:
                    if recursive(pos + 1, l, r) == -1:
                        return -1
                    l = r
                    r += 1
                    graph[word[pos]].append(prev)
                    prev = word[pos]

            if recursive(pos + 1, l, r) == -1:  # the trailing segment
                return -1

        if recursive(0, 0, n) == -1:
            return ''
        print(graph)

        res = []
        visited = set()

        def dfs(node):
            for nextNode in graph[node]:
                if nextNode not in visited:
                    visited.add(nextNode)
                    dfs(nextNode)
            res.append(node)

        for key in hashSet:
            if key not in visited:
                visited.add(key)
                dfs(key)
        return ''.join(res)


