# the tough part of these math question, sepcially this one
# is the inability to analyse the time complexity
# of the solutions, because it involves prime distribution 
# and also it is super hard to meet all the stringent edge cases
# there is not a cure-all solution here. the solution is simply
# iteration of all palindrome after n, and to iterate through the palindromes
# are actually the hard part and involve complicated if statment relationship


from collections import defaultdict, deque
import heapq, math
from typing import List

class Solution:
    def primePalindrome(self, n: int) -> int:
        if n == 1:
            return 2
        def checkPrime(num):
            i = 2
            while i*i <= num:
                if num % i == 0:
                    return False
                i+=1
            return True

        s = str(n)
        size = len(s)
        if size % 2:
            mid = s[size//2]
        else:
            mid = ''

        tar = ''
        if mid == '':
            for i in range(size//2):
                tar += max(s[i], s[size-1-i])
            tarSize = len(tar)
        else:
            tar = s[:size//2]
            tarSize = len(tar)
            # print(int(tar+mid+tar[::-1]))
            if int(tar+mid+tar[::-1]) < n:
                prev = len(tar+mid)
                combine = str(int(tar+mid)+1)
                if len(combine) != prev:
                    tarSize+=1
                    tar = combine[:tarSize]
                    mid = ''
                else:
                    tar, mid = combine[:-1], combine[-1]

        # print(tar, mid)
        while True:
            num = tar + mid + tar[::-1]
            # print(num)
            if checkPrime(int(num)):
                return int(num)

            prev = len(tar+mid)
            combine = str(int(tar+mid)+1)
            if mid != '':
                if len(combine) != prev:
                    tarSize+=1
                    tar = combine[:tarSize]
                    mid = ''
                    # print(combine, tarSize, tar, mid)
                else:
                    tar, mid = combine[:-1], combine[-1]
            else:
                if len(combine) != prev:
                    tar, mid = combine[:-1], combine[-1]                  
                else:
                    tar = combine
                    mid = ''

            

        
