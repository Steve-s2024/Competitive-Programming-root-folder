// haha, comparable interface implemented! (problem rating 2033). I used java because i don't know how to implement the
// customized comparator in python: 80%

import static java.lang.Math.max;

class Solution{
    public int earliestFullBloom(int[] plantTime, int[] growTime) {
        int n = plantTime.length;
        Pair[] arr = new Pair[n];
        for (int i = 0; i < n; i++) {
            arr[i] = new Pair(plantTime[i], growTime[i]);
        }
        Arrays.sort(arr);
        int res = 0;
        int t = 0;
        for (Pair p : arr) {
            // System.out.printf("%d %d\n", p.plantT, p.growT);
            int a = p.plantT, b = p.growT;
            t += a;
            res = max(res, t+b);
        }

        return res;
    }
    class Pair implements Comparable<Pair> {
        public int plantT;
        public int growT;
        public Pair(int plantT, int growT) {
            this.plantT = plantT;
            this.growT = growT;
        }

        @Override
        public int compareTo(Pair p)  {
            int a = this.plantT;
            int b = this.growT;
            int c = p.plantT;
            int d = p.growT;
            int res1 = max(a+b, a+c+d);
            int res2 = max(c+d, c+a+b);
            return res1-res2;
        }
    }
}

