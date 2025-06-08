// 96%
class Solution {
  public:
      bool validMountainArray(vector<int>& arr) {
          int size = arr.size();
          if (size < 3) return false;
          int l = 1, r = size-2;
          while (l < size && arr[l-1] < arr[l]) l++;
          while (r >= 0 && arr[r+1] < arr[r]) r--;
          return l == r+2 && r != size-2 && l != 1;
      }
  };