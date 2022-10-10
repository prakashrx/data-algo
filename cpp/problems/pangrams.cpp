#include "stl.h"
using namespace std;

string pangrams(string s) {
    vector<int> A(26, 0);
    for(char c: s){
        if(c < 65) continue;
        if(c < 97) c = c + 32;
        c -= 97;
        A[c] = 1;
    }
    for(auto i: A) if(i != 1) return "not pangram";
    return "pangram";
}


int main()
{
    cout<<pangrams("We promptly judged antique iory buckles for the next prize")<<endl;
    return 0;
}