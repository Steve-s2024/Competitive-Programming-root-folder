class Solution:
    def minSwaps(self, s: str) -> int:
        counter = Counter(s)
        if abs(counter['0'] - counter['1']) > 1:
            return -1
        mismatch1, mismatch2 = 0, 0
        count = 0
        for c in s:
            if count % 2:
                if c == '1':
                    mismatch1 += 1
                else:
                    mismatch2 += 1
            else:
                if c == '0':
                    mismatch1 += 1
                else:
                    mismatch2 += 1
            count += 1

        if mismatch1 % 2 == 1:
            return mismatch2//2
        if mismatch2 % 2 == 1:
            return mismatch1//2

        return min(mismatch1//2, mismatch2//2)
