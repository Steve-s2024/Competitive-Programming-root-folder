# scary, almost though will hit TLE
[n, m] = [int(e) for e in input().split(' ')]
allDish = []
for i in range(m):
    ingrediant = [int(e) for e in input().split(' ')]
    allDish.append(ingrediant)
overcome = [int(e) for e in input().split(' ')]
hashMap = {}
for i in range(n):
    hashMap[overcome[i]] = i
# print(hashMap)
ans = []
for ingrediant in allDish:
    max_ = 0
    length = ingrediant[0]
    for i in range(1, length + 1):
        max_ = max(max_, hashMap[ingrediant[i]])
    ans.append(max_)
    # print(ingrediant)
    # print(ans)
ans.sort()
i = 0
j = 0
while i < n:
    while j < m and ans[j] <= i:
        j += 1
    print(j)
    i += 1

