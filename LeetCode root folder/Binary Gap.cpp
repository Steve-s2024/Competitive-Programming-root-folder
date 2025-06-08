class Solution {
	public:
		int binaryGap(int n) {
			int begin = -1;
			int end = 0;
			int maxLen = 0;
			while (n) {
				int mod = n % 2;
				if (mod == 1) {
					if (begin != -1) maxLen = max(maxLen, end-begin);
					begin = end;
				}
				n -= mod;
				n /= 2;
				end++;
			}
			return maxLen;
		}
	};