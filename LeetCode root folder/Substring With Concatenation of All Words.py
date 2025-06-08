# only work if the words input only have distinct word.
'''
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        arr = []
        wordSet = set(words)
        for i in range(len(s)):
            arr.append([])
            word = ''
            for j in range(i, len(s)):
                word += s[j]
                if word in wordSet:
                    arr[i].append(word)
        # print(arr)

        targets = set(words)

        def recursive(i):
            if len(targets) == 0:
                return True
            if i >= len(s):
                return False
            for word in arr[i]:
                res = False
                if word in targets:
                    targets.remove(word)
                    res = res or recursive(i + len(word))
                    targets.add(word)
                    if res:
                        return True
            return False

        ans = []
        for i in range(len(s)):
            if recursive(i):
                ans.append(i)
        return ans
'''

# brute-force: tle
'''
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        arr = []
        wordSet = set(words)
        for i in range(len(s)):
            arr.append([])
            word = ''
            for j in range(i, len(s)):
                word += s[j]
                if word in wordSet:
                    arr[i].append(word)
        # print(arr)
        
        targets = Counter(words)
        def recursive(i):
            if len(targets) == 0:
                return True
            if i >= len(s):
                return False
            for word in arr[i]:
                res = False
                if word in targets:
                    targets[word] -= 1
                    if targets[word] == 0:
                        del targets[word]
                    res = res or recursive(i+len(word))
                    if word not in targets:
                        targets[word] = 0
                    targets[word] += 1
                    if res:
                        return True
            return False

        ans = []
        for i in range(len(s)):
            if recursive(i):
                ans.append(i)
        return ans
'''

# dp solution, can't do better: tle
'''class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        arr = []
        wordSet = set(words)
        for i in range(len(s)):
            arr.append([])
            word = ''
            for j in range(i, len(s)):
                word += s[j]
                if word in wordSet:
                    arr[i].append(word)
        # print(arr)

        targets = Counter(words)
        dp = set()

        def recursive(i):
            if i in dp:
                return False
            if len(targets) == 0:
                return True
            if i >= len(s):
                return False
            for word in arr[i]:
                res = False
                if word in targets:
                    targets[word] -= 1
                    if targets[word] == 0:
                        del targets[word]
                    res = res or recursive(i + len(word))
                    if word not in targets:
                        targets[word] = 0
                    targets[word] += 1
                    if res:
                        return True
            return False

        ans = []
        for i in range(len(s) - 1, -1, -1):
            if recursive(i):
                ans.append(i)
            else:
                dp.add(i)
        return ans'''


# i can't believe this is actually a sliding window question..., i guess it is because of the constraint len(words[i])
# less than 30 and all words[i] shares the same length:357
# ms
# Beats
# 43.84%
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        wordLen = len(words[0])
        totalLen = len(words) * wordLen
        for begin in range(wordLen):
            curWords = deque([])
            hashMap = Counter(words)
            l, r = begin, begin
            while r <= len(s) - wordLen:
                word = ''
                for i in range(r, r + wordLen):
                    word += s[i]
                if word in hashMap:
                    curWords.append(word)
                    if hashMap[word] == 0:
                        while hashMap[word] == 0:
                            hashMap[curWords.popleft()] += 1
                            l += wordLen
                    hashMap[word] -= 1
                else:
                    curWords.clear()
                    hashMap = Counter(words)
                r += wordLen
                if len(curWords) == len(words):
                    # print('found', curWords)
                    res.append(r - totalLen)
        return res

