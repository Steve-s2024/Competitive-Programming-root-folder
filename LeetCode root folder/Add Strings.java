// 18%
class Solution {
    Map<String, Integer> map;
    public Solution() {
        map = new HashMap<>();
        for (int n1 = 0; n1 < 10; n1++) {
            for (int n2 = 0; n2 < 10; n2++) {
                String s = n1 + "," + n2;
                map.put(s, n1+n2);
            }
        }
    }

    public String addStrings(String num1, String num2) {
        int size = Math.max(num1.length(), num2.length());
        char[] zeros = new char[size - num1.length()];
        Arrays.fill(zeros, '0');
        num1 = new String(zeros) + num1;
        zeros = new char[size - num2.length()];
        Arrays.fill(zeros, '0');
        num2 = new String(zeros) + num2;

        int carry = 0, remain;
        LinkedList<String> ans = new LinkedList<>();
        for (int i = size-1; i >= 0; i--) {
            String s = num1.charAt(i) + "," + num2.charAt(i);
            int total = carry + map.get(s);
            remain = total % 10;
            carry = total / 10;
            ans.addFirst(remain + "");
        }
        if (carry == 1) ans.addFirst("1");
        return String.join("", ans);
    }
}