// 9%


class Solution {
    public String gcdOfStrings(String str1, String str2) {
        int l1 = str1.length(), l2 = str2.length();
        String res = "";
        for (int i = 1; i <= Math.max(l1, l2); i++) {
            if (l1 % i == 0 && l2 % i == 0 && str1.substring(0, i).equals(str2.substring(0, i))) {
                boolean flag1 = true, flag2 = true;
                for (int j = i; j <= l1-i; j+=i) {
                    if (!str1.substring(j-i, j).equals(str1.substring(j, j+i))) {
                        flag1 = false;
                        break;
                    }
                }
                for (int j = i; j <= l2-i; j+=i) {
                    if (!str2.substring(j-i, j).equals(str2.substring(j, j+i))) {
                        flag2 = false;
                        break;
                    }
                }
                if (flag1 && flag2) {
                    res = str1.substring(0, i);
                }
            }
        }
        return res;
    }
}
