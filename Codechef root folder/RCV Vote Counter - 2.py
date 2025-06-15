# fking boring enough

from collections import deque, defaultdict


def calculate_rcv_winner(ballots):
    if len(ballots) == 0 or len(ballots[0]) == 0: return None
    # Write your code here
    cands = set()
    for row in ballots:
        for cand in row: cands.add(cand)
    n, m = len(ballots), len(ballots[0])
    sm = n
    mp = defaultdict(int)
    for i in range(n): mp[ballots[i][0]] += 1
    ballots = [deque(row) for row in ballots]

    while cands:
        mi = min(mp.values())
        rms = set()
        for cand in cands:
            if mp[cand] * 2 > sm: return cand
            if mp[cand] == mi: rms.add(cand)

        for rm in rms: cands.remove(rm)

        for i in range(n):
            row = ballots[i]
            l = len(row)
            while row and row[0] not in cands: row.popleft()
            if l != len(row):
                if row:
                    mp[row[0]] += 1
                else:
                    sm -= 1

        for rm in rms: mp.pop(rm)

    return None
