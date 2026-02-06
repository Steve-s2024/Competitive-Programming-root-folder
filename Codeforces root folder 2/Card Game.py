# turns out i'm overcomplicating the situation
def solve():
    n = int(input())
    s = input()
    alice, bob = [], []
    for i in range(n):
        if s[i] == 'A':
            alice.append(i)
        else:
            bob.append(i)

    # if alice want to win, she must win the first round!!
    if (
        s[0] == 'A' and s[-1] == 'A' or
        s[0] == 'A' and len(bob) == 1 and bob[0] == n-1 or
        s[0] == 'B' and s[-1] == 'A' and s[-2] == 'A'
    ):
        print('Alice')
    else:
        print('Bob')




# deprecated
def solve():
    n = int(input())
    s = input()
    aMask = 0
    bMask = 0
    for i in range(1, n + 1):
        if s[i] == 'A':
            bMask += pow(2, i)
        else:
            aMask += pow(2, i)

    def recursive(turn, prevCard):
        nonlocal aMask, bMask
        if aMask == pow(2, n) - 1:
            return 1
        if bMask == pow(2, n) - 1:
            return 2

        if turn:
            for i in range(n):
                if aMask & pow(2, i) == 0:
                    aMask ^= pow(2, i)
                    if recursive(not turn, i) == 1:
                        aMask ^= pow(2, i)

        else:
            for i in range(n):
                if bMask & pow(2, i) == 0:
                    card = i
                    if card > prevCard or card == 0 and prevCard == n - 1:
                        bMask ^= pow(2, card)
                        bMask ^= pow(2, prevCard)
                        recursive(not turn, card)
                        bMask ^= pow(2, card)
                        bMask ^= pow(2, prevCard)
                    else:
                        aMask ^= pow(2, card)
                        aMask ^= pow(2, prevCard)
                        recursive(not turn, card)
                        aMask ^= pow(2, card)
                        aMask ^= pow(2, prevCard)


t = int(input())
for tt in range(t):
    solve()
