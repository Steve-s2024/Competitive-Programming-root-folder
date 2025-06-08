# trie solution, limit the checking to the size of dictionary
#: 24%
class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.hashMap = dict(zip(keys, values))
        self.dictionary = set(dictionary)
        self.mp2 = defaultdict(list)
        n = len(keys)
        for i in range(n):
            self.mp2[values[i]].append(keys[i])

        self.trie = {}
        for word in dictionary:
            cur = self.trie
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur['end'] = True
        

    def encrypt(self, word1: str) -> str:
        res = ''
        for c in word1:
            if c not in self.hashMap:
                return ''
            res += self.hashMap[c]
        return res

    def decrypt(self, word2: str) -> int:
        if len(word2) % 2 == 1:
            return 0
            
        n = len(word2)
        def recursive(i, trie):
            nonlocal n
            if i >= n:
                return 1 if 'end' in trie else 0

            cur = word2[i]+word2[i+1]
            if cur not in self.mp2:
                return 0

            res = 0
            for key in self.mp2[cur]:
                if key not in trie:
                    continue
                res += recursive(i+2, trie[key])    
            return res
        return recursive(0, self.trie)


# brute force checking: TLE
class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.hashMap = dict(zip(keys, values))
        self.dictionary = set(dictionary)
        self.mp2 = defaultdict(list)
        n = len(keys)
        for i in range(n):
            self.mp2[values[i]].append(keys[i])

    def encrypt(self, word1: str) -> str:
        res = ''
        for c in word1:
            if c not in self.hashMap:
                return ''
            res += self.hashMap[c]
        return res

    def decrypt(self, word2: str) -> int:
        if len(word2) % 2 == 1:
            return 0
            
        n = len(word2)
        def recursive(i, s):
            nonlocal n
            if i >= n:
                return 1 if s in self.dictionary else 0

            cur = word2[i]+word2[i+1]
            if cur not in self.mp2:
                return 0

            res = 0
            for key in self.mp2[cur]:
                res += recursive(i+2, s+key)    
            return res
        return recursive(0, '')