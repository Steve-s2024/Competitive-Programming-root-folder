import java.util.*;

class Solution {
    public int generateKey(int num1, int num2, int num3) {
        string s1 = nums1 + ''
        string s2 = nums2 + ''
        string s3 = nums3 + ''
        s1 = '0'*(4-s1.length())+s1 // add padding heading zeros until the length is 4
        char arr[] = new char[4];
        for (int i = 0; i < 4; i++ ){
            arr[i] = min(s1.charat(i), s2.charat(i), s3.charat(i));
        }
        return ''.join(arr);
    }
}