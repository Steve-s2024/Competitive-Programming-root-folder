# very un-intuitive solution, mostly because it is hard to analyze the time complexity doing prime factorization
# and finding the way to efficiently compare if two part is coprime in constant time: 5%
class Solution:
    @staticmethod
    def getPrime(x):
        arr = []
        for i in range(2, int(math.sqrt(x))+1):
            while x % i == 0:
                arr.append(i)
                x //= i
        if x > 1: arr.append(x)
        return arr

    def findValidSplit(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        for i in range(len(nums)):
            for num in Solution.getPrime(nums[i]):
                mp[num] += 1

        cnt = 0
        st = set()
        for i in range(len(nums)-1):
            for num in Solution.getPrime(nums[i]):
                if num not in st:
                    cnt += 1
                    st.add(num)
                mp[num] -= 1
                if mp[num] == 0: cnt -= 1
            if cnt == 0: return i
        return -1
