# don't know why the second testcase give 40, if my hashMap is correct
# then the result should be 41
from collections import defaultdict, deque
import heapq, math
from typing import List

def truncate(num, place):
    factor = 10 ** place
    return int(num * factor) / factor

[n, m] = [int(e) for e in input().split(' ')]
lines = []
for i in range(m):
    [a, b] = [int(e) for e in input().split(' ')]
    lines.append((a, b))

dotMap = {}
unit = 360 / n
angle = 0
x = math.cos(angle)
y = math.sin(angle)
# print(unit)

for i in range(1, n+1):
    dotMap[i] = (x, y)
    angle = math.radians(unit * i)
    x = math.cos(angle)
    y = math.sin(angle)
# print(dotMap)

hashMap = defaultdict(int)
for a, b in lines:

    [x1, y1] = dotMap[a]
    [x2, y2] = dotMap[b]
    if x1 == x2:
        slope = float('inf')
    else:
        slope = (y1-y2)/(x1-x2)
        slope = round(slope, 15)
        diff = slope - int(slope)
        s = str(diff)
        if len(s) > 6:
            slope = float(str(slope)[:-1])
    # print(a, b)
    # print(x1, y1, x2, y2)
    hashMap[float(str(slope)[:-1])] += 1
# print(hashMap)
res = 0
for val in hashMap.values():
    res += (m-val) * val
print(res/2)