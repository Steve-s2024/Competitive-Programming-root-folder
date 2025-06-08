// very close to pass, but ig there is an overflow issue
import java.util.*;


class Solution {
    public long repairCars(int[] ranks, int cars) {
        long left = 1;
        int minVal = Arrays.stream(ranks).min().getAsInt();
        long right = minVal*(long)Math.pow(cars, 2);
        long minTime = right;
        while (left <= right) {
            long m = (left + right) / 2;
            int cTotal = 0;
            for (int r : ranks) {
                long c = (long)Math.sqrt((double)m/r);
                cTotal += c;
            } 

            if (cTotal >= cars) {
                right = m-1;
                minTime = m;
            }
            else {
                left = m+1;
            }
        }
        return minTime;
    }
}
