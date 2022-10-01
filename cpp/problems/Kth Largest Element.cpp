/*
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Constraints:

1 <= k <= nums.length <= 10^4

-10^4 <= nums[i] <= 10^4

Example:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
 
Output: 4
*/
#include "stl.h"
using namespace std;

int findKthLargest(vector<int> nums, int k) {
    priority_queue<int, vector<int>, greater<int>> pq;
    for (int num : nums) {
        pq.push(num);
        if (pq.size() > k) {
            pq.pop();
        }
    }
    return pq.top();
}

int findKthLargest_my(vector<int> nums, int k) {
 sort(nums.begin(), nums.end(), greater<int>());
 return nums[k-1];
}

int main() {
  cout<<findKthLargest_my({1,2,3,4}, 4);
  return 0;
}
