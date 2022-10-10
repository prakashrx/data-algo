/*
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or

|a - x| == |b - x| and a < b

Constraints:

1 <= k <= arr.length

1 <= arr.length <= 10^4

arr is sorted in ascending order.

-10^4 <= arr[i], x <= 10^4



Example :

Input: arr = [1,2,3,4,5], k = 4, x = 3
 
Output: [1,2,3,4]
*/
#include "stl.h"
using namespace std;


vector<int> findClosestElements(vector<int> arr, int k, int x) {
    vector<int> v;
    priority_queue<pair<int,int>> pq;
    
    for (int i = 0; i < arr.size(); i++)
    {
        pq.push(make_pair(abs(x-arr[i]), arr[i]));
        if(pq.size() > k)
            pq.pop();
    }

    while (!pq.empty())
    {
        auto e = pq.top();
        pq.pop();
        v.push_back(e.second);
    }
    sort(v.begin(), v.end());
    return v;
}

int main()
{
    auto v = findClosestElements({1,2,3,4,5}, 4, 3);
    for (auto i : v)
    {
        cout<<i<<" ";
    }
    cout<<endl;
    return 0;
}