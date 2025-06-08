# to come up with solutions to these contest problem is
# extra hard due to the fact that all the testcases are
# hidden and there is nowhere to get information as to
# why the code failed. I have to imagine my way out of them.
# cook your dish here
t = int(input())
for T in range(t):
    [n, k] = input().split(" ")
    k = int(k)
    n = int(n)
    s = input()
    zeros = 0
    ones = 0
    flag = False
    for i in range(len(s)-1, -1, -1):
        if s[i] == '1':
            ones += 1
            flag = True
        if flag and s[i] == '0':
            zeros += 1
    print(ones + min(zeros, k))