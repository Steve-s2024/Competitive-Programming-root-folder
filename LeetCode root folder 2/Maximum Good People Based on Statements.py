# for fuck sake, it is actually the purest brute-force!: 10%
class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        graph = {}
        n = len(statements)
        for i in range(n):
            graph[i] = [[], []]
            for j in range(n):
                claim = statements[i][j]
                if claim != 2:
                    graph[i][claim].append(j)

        # print(graph)
        def checkValid(arr):
            for person, sign in enumerate(arr):
                if sign == 'g':
                    for g in graph[person][1]:
                        if arr[g] != 'g':
                            return False
                    for b in graph[person][0]:
                        if arr[b] != 'b':
                            return False
            return True

        visited = [''] * n
        def recursive(i):
            nonlocal n
            if i >= n:
                res = Counter(visited)['g']
                if checkValid(visited):
                    return res
                return 0
            visited[i] = 'g'
            a = recursive(i + 1)
            visited[i] = 'b'
            b = recursive(i + 1)
            visited[i] = ''
            return max(a, b)

        return recursive(0)


# I gotta give up to save the brain
class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        graph = {}
        n = len(statements)
        for i in range(n):
            graph[i] = [[], []]
            for j in range(n):
                claim = statements[i][j]
                if claim != 2:
                    graph[i][claim].append(j)
        # print(graph)
        maxGoodie = 0
        visited = [''] * n

        def recursive(i):
            nonlocal n, maxGoodie
            if i >= n:
                res = Counter(visited)['good']
                maxGoodie = max(maxGoodie, res)
                return

            tmp = visited[i]
            goodPerson = True
            for g in graph[i][1]:
                if visited[g] == 'bad':
                    goodPerson = False
            for b in graph[i][0]:
                if visited[b] == 'good':
                    goodPerson = False
            if goodPerson and tmp == 'bad':
                return

            if goodPerson:
                visited[i] = 'good'
                gs, bs = [], []
                for g in graph[i][1]:
                    if visited[g] == '':
                        gs.append(g)
                        visited[g] = 'good'
                for b in graph[i][0]:
                    if visited[b] == '':
                        bs.append(b)
                        visited[b] = 'bad'

                recursive(i + 1)

                for g in gs:
                    visited[g] = ''
                for b in bs:
                    visited[b] = ''
                visited[i] = tmp

            if visited[i] != 'good':
                visited[i] = 'bad'
                recursive(i + 1)
                visited[i] = tmp

        recursive(0)
        return maxGoodie


# this problem is toasting my brain, sigh...
class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        graph = {}
        n = len(statements)
        for i in range(n):
            graph[i] = [[], []]
            for j in range(n):
                claim = statements[i][j]
                if claim != 2:
                    graph[i][claim].append(j)
        # print(graph)
        maxGoodie = 0
        visited = {}

        def recursive(i):
            nonlocal n, maxGoodie
            if i >= n:
                res = Counter(visited.values())['good']
                maxGoodie = max(maxGoodie, res)
                return
            person = i
            # person (i) should either be bad or good
            ifBad = False
            for baddie in graph[person][0]:
                if baddie in visited and visited[baddie] == 'good':
                    ifBad = True
                    break
            for goodie in graph[person][1]:
                if goodie in visited and visited[goodie] == 'bad':
                    ifBad = True
                    break
            if person in visited and ifBad and visited[person] != 'bad':
                return
            if not ifBad:
                visited[person] = 'good'
                goodies, baddies = [], []
                for goodie in graph[person][1]:
                    if goodie not in visited:
                        goodies.append(goodie)
                        visited[goodie] = 'good'
                for baddie in graph[person][0]:
                    if baddie not in visited:
                        baddies.append(baddie)
                        visited[baddie] = 'bad'
                recursive(i + 1)

                for goodie in goodies:
                    del visited[goodie]
                for baddie in baddies:
                    del visited[baddie]


            visited[person] = 'bad'
            recursive(i + 1)
            del visited[person]

        recursive(0)
        return maxGoodie
