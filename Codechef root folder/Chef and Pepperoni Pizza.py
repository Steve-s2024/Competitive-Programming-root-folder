# boring, does not belong to the rating category
# cook your dish here
t = int(input())
for tt in range(t):
    n = int(input())
    left, right = [], []
    for i in range(n):
        row = input()
        cnt1, cnt2 = 0, 0
        for i in range(n // 2):
            cnt1 += int(row[i])
        for i in range(n // 2, n):
            cnt2 += int(row[i])
        left.append(cnt1)
        right.append(cnt2)
    # print(left, right)
    sm1, sm2 = sum(left), sum(right)
    res = abs(sm1 - sm2)
    for i in range(len(left)):
        cur1, cur2 = sm1 - left[i] + right[i], sm2 - right[i] + left[i]
        res = min(res, abs(cur1 - cur2))
    print(res)

