# first time learn about this property of not being palindrome (a greedy approach to always make the string
# constructed not being a palindrome), interesting.
# basically you guarantee to append the new character that is different from previous two characters, then the
# string constructed will never be a palindrome in any moment except when it's length is 1

# in another word, make sure that any consecutive three characters of the string be distinct to each other

def solve():
    n, k = [int(e) for e in input().split()]
    nums = [int(e)-1 for e in input().split()]
    vis = [1]*n
    for num in nums: vis[num] = 0

    arr = []
    for i in range(n):
        if vis[i]: arr.append(i)

    res = []
    # print(arr)
    cur = 0
    a, b = nums[-2], nums[-1]
    if len(arr):
        k -= 1
        a, b = b, arr[0]
        res.append(arr[0])

    for i in range(k):
        while cur in [a, b]: cur = (cur+1)%n
        res.append(cur)
        a, b = b, cur

    print(' '.join(str(e+1) for e in res))



t = int(input())
for i in range(t): solve()