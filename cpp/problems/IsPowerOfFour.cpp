#include "stl.h"

using namespace std;

bool isPowerOfFour(int n) {
 if(n < 4)
    return false;
 double x = sqrt(n);
 if(int(x) != x)
    return false;
 return ( (int(x) & (int(x) -1)) == 0);
}

int main() {
    cout<<isPowerOfFour(16)<<endl;
    cout<<isPowerOfFour(8)<<endl;
    cout<<isPowerOfFour(5)<<endl;
    cout<<isPowerOfFour(32)<<endl;
    cout<<isPowerOfFour(64)<<endl;
}