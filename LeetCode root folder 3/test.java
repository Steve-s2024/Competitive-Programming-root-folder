import java.util.*;
public class test {}
  


class Robot {
    int width;
    int height;
    int parameter;
    int curDst = 0;
    Map<Integer, int[]> dstMap = new HashMap<>();
    Map<Integer, Integer> dirMap = new HashMap<>();
    boolean flag = true;

    public Robot(int width, int height) {
        this.width = width;
        this.height = height;
        this.parameter = 2*width + 2*(height-2);
        this.createMaps();
    }
    
    public void step(int num) {
        flag = false;
        curDst += num;
        curDst %= parameter;
        
    }
    
    public int[] getPos() {
        int[] coor = dstMap.get(curDst);
        int a = coor[0], b = coor[1];
        return new int[] {b-1, a-1};
    }
    
    public String getDir() {
        if (flag) return "East";
        int i = dirMap.get(curDst);
        String[] mp = {"East", "North", "West", "South"};
        return mp[i];
    }

    private void createMaps() {
        int dst = 0;
        int[][] ref = {{0, 1},{1, 0},{0, -1},{-1, 0}};
        int i = 0, r = 1, c = 1;
        while (dst < parameter) {
            dstMap.put(dst, new int[] {r, c});
            dirMap.put(dst, i);

            if (
                (r+ref[i][0] > height || r+ref[i][0] < 1) ||
                (c+ref[i][1] > width || c+ref[i][1] < 1)
            ) i++;
            r += ref[i][0];
            c += ref[i][1];
        }
        dirMap.put(0, 3);
    }
}

