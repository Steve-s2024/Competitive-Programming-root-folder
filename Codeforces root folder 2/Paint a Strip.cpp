#include<iostream>
using namespace std;
 
int main() {
    int t;
    cin >> t;
    for (int pos = 0; pos < t; pos++) {
        int n;
        cin >> n;
        int res = 1;
        int cnt = 1;
        while (cnt < n) {
            cnt += 1;
            cnt *= 2;
            res++;
        }
        cout << res << endl;
    }
}