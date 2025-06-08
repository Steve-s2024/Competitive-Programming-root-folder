// 20%
class Solution {
    public List<Boolean> prefixesDivBy5(int[] nums) {
        ArrayList<Boolean> ans = new ArrayList<>(nums.length);
        int n = 0;
        for (int i = 0; i < nums.length; i++) {
            n *= 2;
            n += nums[i];
            ans.add(n % 5 == 0);
            n %= 5;
        }
        return ans;
    }
}