# i am so tired when solving this:
class ATM:

    def __init__(self):
        self.hashMap = defaultdict(int)
        self.ref = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            key = self.ref[i]
            self.hashMap[key] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        copyMap = copy.deepcopy(self.hashMap)
        ref = self.ref
        i = len(ref) - 1
        res = [0] * 5
        for i in range(len(ref) - 1, -1, -1):
            key = ref[i]
            n = min(amount // key, copyMap[key])
            res[i] = n
            copyMap[key] -= n
            amount -= key * n
            if amount == 0:
                self.hashMap = copyMap
                return res
        return [-1]
