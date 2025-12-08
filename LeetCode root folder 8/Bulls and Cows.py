# boring question: 91%
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = 0
        b = 0
        mp = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
            else:
                if secret[i] not in mp: mp[secret[i]] = [0, 0]
                mp[secret[i]][0] += 1
                if guess[i] not in mp: mp[guess[i]] = [0, 0]
                mp[guess[i]][1] += 1

        for x, y in mp.values(): b += min(x, y)
        return str(a) + 'A' + str(b) + 'B'
