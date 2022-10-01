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

#include <iostream>
#include <vector>
using namespace std;

int firstUniqChar(string s) {
    vector<int> arr(26,0);
    for (int i = 0; i < s.length(); i++)
    {
        arr[s[i]-'a']++;
    }
    for (int i = 0; i < s.length(); i++)
    {
        if(arr[s[i]-'a'] == 1)
            return i;
    }
    return -1;
}

int main() {
    cout<< firstUniqChar("codingtutsco");
    return 0;
}