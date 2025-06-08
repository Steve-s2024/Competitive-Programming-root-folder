//100%
class Solution {
    public boolean isBoomerang(int[][] points) {
        int[] a = points[0], b = points[1], c = points[2];
        if (a[0] == b[0] && a[1] == b[1] || c[0] == b[0] && c[1] == b[1] || a[0] == c[0] && a[1] == c[1]) return false;
        if (a[0] == b[0] && a[0] == c[0]) return false;
        return (
            (a[1] - b[1]) / (double)(a[0] - b[0]) !=
            (b[1] - c[1]) / (double)(b[0] - c[0])
        );
    }
}