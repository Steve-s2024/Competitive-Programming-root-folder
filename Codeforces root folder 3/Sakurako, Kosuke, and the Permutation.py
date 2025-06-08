# very interesting cycle detection question, I would not think it as dfs and cycle
# counting if not because of the topic

def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]

    idxMp = {}
    for i in range(n):
        idxMp[nums[i]] = i

    res = 0
    st = set()
    for i in range(n):
        if nums[i] in st:
            continue
        cnt = 0
        cur = nums[i]
        while cur not in st:
            st.add(cur)
            cur = nums[cur-1]
            cnt += 1

        res += (cnt-1)//2
    print(res)


t = int(input())
for i in range(t):
    solve()
