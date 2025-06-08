# boring question:63
# ms
# Beats
# 95.96%
class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        pos, neg = set(positive_feedback), set(negative_feedback)
        hashMap = defaultdict(list)
        for idx, comment in enumerate(report):
            score = 0
            for word in comment.split():
                if word in pos:
                    score += 3
                if word in neg:
                    score -= 1
            hashMap[score].append(student_id[idx])
        res = [(key, sorted(val)) for key, val in hashMap.items()]
        res.sort(key = lambda i : i[0])
        # print(res, k)
        ans = []
        while k:
            cur = res.pop()
            l = min(len(cur[1]), k)
            ans += cur[1][:k]
            k -= l
        return ans
