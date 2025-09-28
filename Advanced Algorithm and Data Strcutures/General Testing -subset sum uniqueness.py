# testing the amount of distinct number can be created by adding some element of an array up

from random import randint

def testSubsetSummationUniqueness(nums):
    st = set()
    n = len(nums)
    def recursive(i, tot):
        nonlocal n
        if i >= n:
            st.add(tot)
            return
        recursive(i + 1, tot)
        recursive(i + 1, tot + nums[i])


    recursive(0, 0)
    return len(st)


def getRandArr(n, lim):
    arr = [0]*n
    for i in range(n):
        arr[i] = randint(0, lim) # size is small
    return arr


for i in range(5):
    size = 10
    lim = 10
    res = testSubsetSummationUniqueness(getRandArr(size, lim))
    print(f'when size is {size} and lim is {lim}, number of unique count is small: {res}')
print()
for i in range(5):
    size = 10
    lim = 20
    res = testSubsetSummationUniqueness(getRandArr(size, lim))
    print(f'when size is {size} and lim is {lim}, number of unique count is still small: {res}')
print()
for i in range(5):
    size = 10
    lim = 400
    res = testSubsetSummationUniqueness(getRandArr(size, lim))
    print(f'when size is {size} and lim is {lim}, number of unique count is big now: {res}')
print()
for i in range(5):
    size = 10
    lim = 4000
    res = testSubsetSummationUniqueness(getRandArr(size, lim))
    print(f'when size is {size} and lim is {lim}, number of unique count is big now, but capped by 2^{size}: {res}')


# conclusion, the amount of distinct integer produced is closely related to lim*size, while it is capped by 2^n as while
# so in extreme case the number can go up to 2^n, after that threshold the value of lim will no longer affect the count

# so, the more different the numbers are in the testing array, the more possible distinct subset sum it can produce
