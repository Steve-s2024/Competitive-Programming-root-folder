# absolutely a disgusting math question: 5%
class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded)
        ecxor = 0
        for num in encoded: ecxor ^= num
        a, b = encoded[0], ecxor
        arr = []
        arr.append(b)
        for i in range(1, n):
            b = a ^ b
            a = encoded[i]
            arr.append(b)
        # print(arr)
        xor = 0
        for num in arr: xor ^= num
        ofs = 0
        for i in range(1, n + 2): ofs ^= i

        lst = xor ^ ofs
        fst = ecxor ^ lst
        # print(ecxor, lst)
        # print(fst)
        ans = [fst]
        for i in range(n):
            fst ^= encoded[i]
            ans.append(fst)
        return ans
