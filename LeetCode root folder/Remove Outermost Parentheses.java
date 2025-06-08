// 5%
class Solution {
    public String removeOuterParentheses(String s) {
        Stack<Character> stack = new Stack<>();
        String res = "";
        for (int i = 0; i < s.length(); i++) {
          char cur = s.charAt(i);
            if (cur == '(') {
                if (!stack.isEmpty()) res += cur;
                stack.add('(');
            }
            else {
                stack.pop();
                if (!stack.isEmpty()) res += cur;
            }
        }
        return res;
    }
}