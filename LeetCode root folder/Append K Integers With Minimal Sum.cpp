//greedy solution:111
//ms
//Beats
//56.90%

class Solution {
	public:
			long long minimalKSum(vector<int>& nums, int k) {
                vector<int> tmp;
                unordered_set<int> hashSet;
                for (int num : nums) {
                        if (hashSet.find(num) == hashSet.end()) {
                                hashSet.insert(num);
                                tmp.push_back(num);
                        }
                }
                nums = tmp;
                sort(nums.begin(), nums.end());
                long long total = 0;
                for (int i = 0; i < nums.size(); i++) {
                        int emptySpot = nums[i] - (i+1);
                        if (emptySpot >= k) {
                                long long size = i + k;
                                long long totalSum = size * (size+1) / 2;
                                return totalSum - total;
                        }
                        total += nums[i];
                }
                long long size = nums.size() + k;
                long long totalSum = size * (size+1) / 2;
                return totalSum - total;
			}
	};