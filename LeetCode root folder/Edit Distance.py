# brute-force backtracking solution, not complete
# this solution only deals with the insert and deplete operations, but not the replace operation.
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # this solution only deals with the insert and delete operations.

        def backtrack(i1, i2):
            if i2 >= len(word2):
                # return the number of operation left to delete rest of word1 if any exists
                return max(len(word1) - i1, 0)

            if i1 >= len(word1):
                res = backtrack(i1, i2+1) + 1 # insert element
            elif word1[i1] == word2[i2]:
                res = min(
                    backtrack(i1+1, i2+1),
                    backtrack(i1+1, i2) + 1, # i delete the word[i1], so number of operation increase by one
                    backtrack(i1, i2+1) + 1 # i insert the word[i1] at the index, num of operation increase by one
                )
            else:
                res = min(
                    backtrack(i1+1, i2) + 1, # i delete the word[i1], so number of operation increase by one
                    backtrack(i1, i2+1) + 1 # i insert the word[i1] at the index, num of operation increase by one
                )
            return res

        return backtrack(0, 0)
'''


# solution no.1, backtracking:
# NeetCode I Love U. I woudn't be able to solve this in my life if it weren't because of you!
# this is the brute-force solution, I also have the dp solution below
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def backtrack(i1, i2, insertOrDelete):
            if i2 >= len(word2):
                # return the number of operation left to delete rest of word1 if any exists
                return max(len(word1) - i1, 0)
            # the insertOrDelete has three values: 0, 1, 2
            #   0 -> there is insert to be cancel
            #   1 -> there is delete to be cancel
            #   2 -> there is nothing to be cancel

            if i1 >= len(word1):
                if insertOrDelete == 1:
                    res = backtrack(i1, i2+1, 2) 
                else:
                    res = backtrack(i1, i2+1, 0) + 1
            elif word1[i1] == word2[i2]:
                if insertOrDelete == 1:
                    a = backtrack(i1, i2+1, 2)
                else:
                    a = backtrack(i1, i2+1, 0) + 1
                if insertOrDelete == 0:
                    b = backtrack(i1+1, i2, 2)
                else:
                    b = backtrack(i1+1, i2, 1) + 1
                c = backtrack(i1+1, i2+1, 2)
                res = min(a, b, c)
            else:
                if insertOrDelete == 1:
                    a = backtrack(i1, i2+1, 2)
                else:
                    a = backtrack(i1, i2+1, 0) + 1
                if insertOrDelete == 0:
                    b = backtrack(i1+1, i2, 2)
                else:
                    b = backtrack(i1+1, i2, 1) + 1
                res = min(a, b)
            return res

        return backtrack(0, 0, 2)
'''



# solution no.2, dp solution:735
# ms
# Beats
# 5.03%
# 2025-02-08
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}

        def backtrack(i1, i2, insertOrDelete):
            if (i1, i2, insertOrDelete) in dp:
                return dp[(i1, i2, insertOrDelete)]

            if i2 >= len(word2):
                # return the number of operation left to delete rest of word1 if any exists
                return max(len(word1) - i1, 0)
            # the insertOrDelete has three values: 0, 1, 2
            #   0 -> there is insert to be cancelled
            #   1 -> there is delete to be cancelled
            #   2 -> there is nothing to be cancelled

            if i1 >= len(word1):
                if insertOrDelete == 1:
                    res = backtrack(i1, i2+1, 2) 
                else:
                    res = backtrack(i1, i2+1, 0) + 1
            elif word1[i1] == word2[i2]:
                if insertOrDelete == 1:
                    a = backtrack(i1, i2+1, 2)
                else:
                    a = backtrack(i1, i2+1, 0) + 1
                if insertOrDelete == 0:
                    b = backtrack(i1+1, i2, 2)
                else:
                    b = backtrack(i1+1, i2, 1) + 1
                c = backtrack(i1+1, i2+1, 2)
                res = min(a, b, c)
            else:
                if insertOrDelete == 1:
                    a = backtrack(i1, i2+1, 2)
                else:
                    a = backtrack(i1, i2+1, 0) + 1
                if insertOrDelete == 0:
                    b = backtrack(i1+1, i2, 2)
                else:
                    b = backtrack(i1+1, i2, 1) + 1
                res = min(a, b)
            dp[(i1, i2, insertOrDelete)] = res
            return res

        return backtrack(0, 0, 2)
