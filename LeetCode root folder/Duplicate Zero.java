//98%
class Solution {
    public void duplicateZeros(int[] arr) {
        int[] ans = new int[arr.length];
        int i = 0, j = 0;
        while (j < arr.length) {
            if (arr[i] == 0) {
                ans[j] = 0;
                if (j == arr.length-1) break;
                ans[j+1] = 0;
                j++;
            }
            else ans[j] = arr[i];
            i++;
            j++;
        }
        for (int idx = 0; idx < arr.length; idx++) arr[idx] = ans[idx];
    }
}