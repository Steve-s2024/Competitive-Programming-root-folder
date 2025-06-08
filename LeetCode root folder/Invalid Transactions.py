# idk what to call solution (hash map plus sorting?):7
# ms
# Beats
# 95.99%
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        hashMap = defaultdict(list)
        ans = set()
        for i, tran in enumerate(transactions):
            info = tran.split(',')
            if int(info[2]) > 1000:
                ans.add(i)
            info.append(i)
            hashMap[info[0]].append(info)
        # print(hashMap)

        for arr in hashMap.values():
            arr.sort(key=lambda i: int(i[1]))
            q = deque([])
            for i in range(len(arr)):
                curInfo = arr[i]
                while q and int(curInfo[1]) - int(q[0][1]) > 60:
                    q.popleft()
                # print(q, ans)
                if q:
                    for info in q:
                        if info[3] != curInfo[3]:
                            # print(info, curInfo)
                            # print(i, info[4])
                            ans.add(curInfo[4])
                            ans.add(info[4])
                q.append(arr[i])

        res = []
        for idx in ans:
            res.append(transactions[idx])
        return res