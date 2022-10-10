#include "stl.h"
using namespace std;


string twoArrays(int k, vector<int> A, vector<int> B) {
    long a = 0, b = 0;
    for(auto i: A)
        a += max(0,k - i);
    for(auto i: B)
        b += max(0,k - i);
    return a+b <= k*A.size() ? "YES" : "NO";
}

int main() {

    cout<<twoArrays(5, {1,2,2,1}, {3,3,3,4})<<endl;
    cout<<twoArrays(10, {2,1,3}, {7,8,9})<<endl;
    cout<<twoArrays(10, {10000, 1, 1, 1}, {1,1,1,1})<<endl;

}