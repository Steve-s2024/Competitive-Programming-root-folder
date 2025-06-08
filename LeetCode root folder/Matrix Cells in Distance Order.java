// 6.2%
class Solution {
    public int[][] allCellsDistOrder(int rows, int cols, int rCenter, int cCenter) {
        ArrayList<ArrayList<Integer>> res = new ArrayList<>(rows*cols);
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                int dst = Math.abs(rCenter-r) + Math.abs(cCenter-c);
                ArrayList<Integer> tmp = new ArrayList<>(Arrays.asList(dst, r, c));
                res.add(tmp);
            }
        }
        Collections.sort(res, (a, b) -> Integer.compare(a.get(0), b.get(0)));
        System.out.println(res);
        int[][] ans = new int[rows*cols][2];
        int i = 0;
        for (ArrayList<Integer> arr : res) {
            ans[i][0] = arr.get(1);
            ans[i][1] = arr.get(2);
            i++;
        }
        return ans;
    }
}




// discarded, failed atempt of using lambda function
class Solution {
    public int[][] allCellsDistOrder(int rows, int cols, int rCenter, int cCenter) {
        int[][] grid = new int[rows*cols][2];
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                grid[r*cols+c][0] = r;
                grid[r*cols+c][1] = c;
            }
        }
        Arrays.sort(grid, (e1, e2) -> Integer.compare(
            (int)Math.sqrt(Math.pow(rCenter-e1[0], 2) + Math.pow(cCenter-e1[1], 2)), 
            (int)Math.sqrt(Math.pow(rCenter-e2[0], 2) + Math.pow(cCenter-e2[1], 2))
          ));
        return grid;
    }
}