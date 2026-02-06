# type of problem that makes you headache
# this is my weak spot. when the task gets complicate, not necessarily hard, I can't think clear.
# I am overcoming the issue; solving this without too much pain is the evidence
class LFUCache:

    def __init__(self, capacity: int):
        self.hp = []
        self.frq = defaultdict(int)
        self.mp = {}
        self.x = 0
        self.cap = capacity
        self.tm = 0

    def get(self, key: int) -> int:
        hp = self.hp
        frq = self.frq
        mp = self.mp

        if key in mp:
            frq[key] += 1
            self.tm += 1
            heappush(hp, (frq[key], self.tm, key))
            return mp[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        hp = self.hp
        frq = self.frq
        mp = self.mp
        if key not in mp:
            self.x += 1
            if self.x > self.cap:
                # print(frq)
                while hp and hp[0][0] != frq[hp[0][2]]: heappop(hp)
                t = hp[0][2]
                # print(t, mp)
                mp.pop(t)
                frq[t] = 0
                self.x -= 1

        mp[key] = value
        frq[key] += 1
        self.tm += 1
        heappush(hp, (frq[key], self.tm, key))

