#

def solve():
    n, x, y = [int(e) for e in input().split()]
    X, Y = x, y
    s = input()
    nums = [int(e) for e in input().split()]
    sm = sum(nums)

    for i in range(n):
        f, v = int(s[i]), nums[i]
        if f: # B party
            y -= v//2 + 1
        else:
            x -= v//2 + 1
        sm -= v//2 + 1

    if x < 0 or y < 0 or x+y < sm:
        print('No')
        return

    if x >= y and '0' in s:
        print('Yes')
    elif y >= x and '1' in s:
        print('Yes')
    else:
        if '0' in s:
            print('Yes' if X-n >= Y else 'No')
        if '1' in s:
            print('Yes' if Y-n >= X else 'No')


for _ in range(int(input())): solve()


# look back 10 month of time this is a good testament of the progress i made.


def solve():
    n, x, y = [int(e) for e in input().split()]
    s = input()
    nums = [int(e) for e in input().split()]
    sm = sum(nums)

    for i in range(n):
        f, v = int(s[i]), nums[i]
        if f: # B party
            y -= v//2 + 1
        else:
            x -= v//2 + 1
        sm -= v//2 + 1

    if x < 0 or y < 0 or x+y < sm:
        print('No')
        return

    if x >= y and '0' in s:
        print('Yes')
    elif y >= x and '1' in s:
        print('Yes')
    else:
        hsm = sum(e//2 for e in nums)
        if x > y:
            x -= y+hsm
            print('No' if x > 0 else 'Yes')
        elif y > x:
            y -= x+hsm
            print('No' if y > 0 else 'Yes')


for _ in range(int(input())): solve()