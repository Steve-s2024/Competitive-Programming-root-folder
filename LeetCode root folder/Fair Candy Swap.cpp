class Solution {
public:
    vector<int> fairCandySwap(vector<int>& aliceSizes, vector<int>& bobSizes) {
        int aliceTotal = accumulate(aliceSizes.begin(), aliceSizes.end(), 0);
        int bobTotal = accumulate(bobSizes.begin(), bobSizes.end(), 0);
        int aliceOwe = aliceTotal - bobTotal;

        unordered_set<int> hashSet;
        for (int num : aliceSizes) {
            hashSet.insert(num);
        }
        for (int num : bobSizes) {
            // pretned bob send the current box to alice
            // now alice owe bob this amount -> aliceOwe + 2 * num
            // but alice only need to return half of the amount to equalize their candies
            int equalizeAmount = (aliceOwe + 2 * num) / 2;
            if (hashSet.find(equalizeAmount) != hashSet.end()) return {equalizeAmount, num};
        }
        return {0, 0};
    }
};