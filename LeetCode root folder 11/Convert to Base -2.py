# more than a year have passed since I first came across this problem. I have grown, and this is no longer a challenge
# still quite hard. the reason why it is 1700 possibly due to prerequisite
# I don't have the prior knowledge, so it is as hard as a 2200 to me

class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0: return '0'
        ct = [0]*60
        for i in range(30):
            re = n%2
            if re:
                ct[i] += 1
                if i%2: ct[i+1] += 1
            while ct[i] > 1 and ct[i+1]: ct[i], ct[i+1] = ct[i]-2, ct[i+1]-1
            while ct[i] > 1:
                ct[i] -= 2
                ct[i+1] += 1
                ct[i+2] += 1
            n >>= 1
        # print(ct)
        ct = ct[::-1]
        ct = ct[ct.index(1):]
        return ''.join(str(e) for e in ct)