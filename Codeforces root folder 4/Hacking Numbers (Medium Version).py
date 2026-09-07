# the memorable question, good for a challenge among friends who don't know much about coding



def query(t, v):
    print(f'{t} {v}')
    stdout.flush()
    res = int(input())
    if res == -1: exit(4399)
    return res

def solve():
    n = int(input())
    query('mul', 9)
    query('digit', '')
    query('digit', '')
    query('add', n-9)
    print('!')
    input()


for _ in range(int(input())): solve()

