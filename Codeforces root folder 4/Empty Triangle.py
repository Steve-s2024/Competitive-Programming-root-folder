# adaptive frontman? you can adapt first one but can't adapt this bitch (random.randint()) haha!
from sys import stdout
from random import randint

# accepted code, first ever question passed with randomization
def query(i, j, k):
    print(f'? {i} {j} {k}')
    stdout.flush()
    return int(input())


def solve():
    n = int(input())
    i, j, k = 1, 2, 3
    while 1:
        res = query(i, j, k)
        if res == -1:
            exit()
        elif res == 0:
            print(f'! {i} {j} {k}')
            return

        rd = randint(1, 3)
        if rd == 1: i = res
        elif rd == 2: j = res
        else: k = res





# the judge adapted my strategy and give me stupid query answer that eventually cause
# me to run out of query on case 22
def query(i, j, k):
    print(f'? {i} {j} {k}')
    stdout.flush()
    return int(input())

def solve():
    n = int(input())
    i, j, k = 1, 2, 3
    while 1:
        res = query(i, j, k)
        if res == -1:
            exit()
        elif res == 0:
            print(f'! {i} {j} {k}')
            return

        i = res

