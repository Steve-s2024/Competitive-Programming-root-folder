# struggling to even solve for 2000 rated question...: 17%
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = [i for i in range(n)]
        heapq.heapify(rooms)

        taken = []
        meetings.sort(key=lambda i: i[0])
        mx = max(e[1] for e in meetings)
        i = 0
        mp = defaultdict(int)
        day = 0
        while i < len(meetings):
            s, e = meetings[i]
            day = max(day, s)
            while taken and taken[0][0] <= day:
                _, room = heapq.heappop(taken)
                heapq.heappush(rooms, room)

            if rooms:
                room = heapq.heappop(rooms)
                dur = e - s
                heapq.heappush(taken, (day + dur, room))
                mp[room] += 1
                i += 1
            else:
                d, room = heapq.heappop(taken)
                day = d
                heapq.heappush(rooms, room)

        # print(mp)
        res = 0
        mxUse = 0
        for key, val in mp.items():
            if val > mxUse:
                mxUse = val
                res = key
            elif val == mxUse:
                res = min(res, key)

        return res



# deprecated
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = [i for i in range(n)]
        heapq.heapify(rooms)

        taken = []
        meetings.sort(key=lambda i: i[0])
        mx = max(e[1] for e in meetings)
        i = 0
        mp = defaultdict(int)

        for day in range(1, mx + 1_000):
            while taken and taken[0][0] <= day:
                _, room = heapq.heappop(taken)
                heapq.heappush(rooms, room)

            while i < len(meetings) and meetings[i][0] <= day and len(rooms):
                room = heapq.heappop(rooms)
                s, e = meetings[i]
                dur = e - s + 1
                heapq.heappush(taken, (day + dur, room))
                mp[room] += 1
                i += 1

        # print(mp)
        res = 0
        mxUse = 0
        for key, val in mp.items():
            if val > mxUse:
                mxUse = val
                res = key
            elif val == mxUse:
                res = min(res, key)

        return res