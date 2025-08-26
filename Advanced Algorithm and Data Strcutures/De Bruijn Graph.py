# an implementation of the building of De Bruijn graph, for constructing the De Bruijn sequence

class DeBruijnGraph:
    def build(self, n, k):
        strarr = []
        vis = set()
        def dfs(node):
            for i in range(k):
                string = node + str(i)
                if string not in vis:
                    vis.add(string)
                    dfs(string[1:])
                    strarr.append(string[-1])
        begin = '0'*(n-1)
        dfs(begin)
        print(begin + ''.join(reversed(strarr)))

dbg = DeBruijnGraph()
dbg.build(2, 2)
dbg.build(3, 2)
dbg.build(3, 3)
