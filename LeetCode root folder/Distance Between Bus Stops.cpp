#include<iostream>
#include<unordered_map>
#include<unordered_set>
#include<algorithm>
#include<vector>
#include<cmath>
#include<deque>
#include<limits>
#include<numeric>
using namespace std;

class Solution {
    public:
        int distanceBetweenBusStops(vector<int>& distance, int start, int destination) {
            int prefix = 0;
            int a = 0, b = 0;
            int n = distance.size();
            for (int i = 0; i < n; i++) {
                if (start == i) a = prefix;
                if (destination == i) b = prefix;
                prefix+=distance[i];
            }
            cout << a << ' ' << b << ' ';
            int dst = abs(a-b);
            return min(dst, prefix-dst);
        }
    };