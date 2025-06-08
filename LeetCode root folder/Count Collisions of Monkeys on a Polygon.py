# it turns out this is a terrible question and other people share the same confusion as i do and no one disagree
# with the answer being 2^n - 4 when n is even, so idk what the hell is going on!!
class Solution:
    def monkeyMove(self, n: int) -> int:
        # the total number of way to collide when n is even: 2 ^ n - 4 (because there are 4 ways which they will not collide) --but the reality is clearly not like this?? why???
        # the reality is somehow showing the answer to be 2 ^ n - 2 in all cases!!

        # when n is odd, collide count: (2 ^ n - 2)
        # (not 100% sure if this will work)

        if n % 2 == 1:
            res = pow(2, n) - 2
        else:
            res = pow(2, n) - 4

        return res % (pow(10, 9) + 7)
