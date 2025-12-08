# cannot believe it passed, I didn't put much in proving it, just an instinct in my head and I carried it out.

def solve():
    n = int(input())
    nums = [int(e)-1 for e in input().split()]
    arr = [i for i in range(n)]
    ans = []
    for n in nums[::-1]:
        for i in range(arr.index(n)-1, -1, -1):
            ans.append((arr[i+1]+1, arr[i]+1))
            arr[i], arr[i+1] = arr[i+1], arr[i]
    print(len(ans))
    for a, b in ans:
        print(f'{a} {b}')


solve()