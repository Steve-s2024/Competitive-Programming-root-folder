// 25%
class Solution {
    public int numEquivDominoPairs(int[][] dominoes) {
        HashMap<String, Integer> map = new HashMap<>();
        for (int[] pair : dominoes) {
            int a = pair[0], b = pair[1];
            String s = Math.min(a, b) + "," + Math.max(a, b);
            if (map.get(s) == null) map.put(s, 0);
            map.put(s, map.get(s)+1);
        }
        int res = 0;
        // System.out.println(map);
        for (Map.Entry<String, Integer> pair : map.entrySet()) {
            int n = pair.getValue();
            res += n * (n-1) / 2;
        }

        return res;
    }
}