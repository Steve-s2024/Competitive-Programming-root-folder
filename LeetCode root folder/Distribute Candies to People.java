// not easy for sure! or maybe I just didn't see the obvious solution here since my solution is indeed the most optimized one!: 96%
class Solution {
    public int[] distributeCandies(int candies, int num_people) {
        int n = 0;
        long total = 0;
        while (total < candies) {
            n++;
            total = n*(n+1) / 2;
        }
        n--;
        
        int remain = candies - (n*(n+1)/2); // the number of candies remain for the last person handout.
        int cycle = n / num_people; // the number of complete cycles for handing out candies among the people.
        int extra = n % num_people; // the number of people in the last incomplete candy handout.
        // System.out.println(n);
        int[] ans = new int[num_people];
        for (int i = 0; i < ans.length; i++) {
            ans[i] = num_people * ((cycle-1)*cycle/2) + cycle * (i+1); //"num_people * ((cycle-1)*cycle/2) + cycle * (i+1)" is the increase of candy for person(i) in all complete cycles. 
            // System.out.println(i+1 + ' ' + cycle + ' ' + ans[i]);
        }
        for (int i = 0; i < extra; i++) { // assign candies for the last cycle, which is incomplete.
            ans[i] += num_people*cycle + i+1; // num_people*cycle + i+1 is the increase of candies each people have
        }
        ans[extra] += remain; // the very last person to have handout.
        return ans;
    }
}
