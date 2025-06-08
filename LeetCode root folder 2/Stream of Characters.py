# backwords trie solution, pretty easy to implement
# and pretty easy to think of it, this should probably
# not be a hard question: 38%
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        n = len(words)
        for i in range(n):
            m = len(words[i])
            cur = self.trie
            for j in range(m - 1, -1, -1):
                char = words[i][j]
                if char not in cur:
                    cur[char] = {}
                cur = cur[char]
            cur['end'] = True
        self.s = ''

    def query(self, letter: str) -> bool:
        self.s += letter
        n = len(self.s)
        cur = self.trie
        for i in range(n - 1, -1, -1):
            char = self.s[i]
            if char in cur:
                cur = cur[char]
                if 'end' in cur:
                    return True
            else:
                break
        return False


# brute force: TLE
class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = set(words)
        self.s = ''

    def query(self, letter: str) -> bool:
        self.s += letter
        n = len(self.s)
        for i in range(n):
            if self.s[i:] in self.words:
                return True
        return False
