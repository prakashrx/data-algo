/*
One Integer
You are given a list of integers nums. You can reduce the length of nums by taking any two integers, removing them, and appending their sum to the end. The cost of doing this is the sum of the two integers you removed.

Return the minimum total cost of reducing nums to one integer.



Note : Cost can be negative also.

Constraints

n ≤ 100,000 where n is length of nums.



Example :

Input

nums = [1, 2, 3, 4, 5]
Output

33
Explanation

We take 1 and 2 out to get [3, 4, 5, 3]

We take 3 and 3 out to get [4, 5, 6]

We take 4 and 5 out to get [6, 9]

We take 6 and 9 out to get [15]

The sum is 33 = 1 + 2 + 3 + 3 + 4 + 5 + 6 + 9
*/
#include "stl.h"
using namespace std;

int solve(vector<int> nums) {
    priority_queue<int, vector<int>, greater<int>> pq(nums.begin(), nums.end());

    int sum = 0;
    while (pq.size() > 1)
    {
        int first = pq.top();
        pq.pop();
        int second = pq.top();
        pq.pop();
        pq.push(first + second);
        sum += first + second;
    }
    return sum;
}

int main() {
  cout<<solve({1, 2, 3, 4, 5});
  return 0;
}
