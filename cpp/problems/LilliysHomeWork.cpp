#include "stl.h"

using namespace std;

void swap(int* a, int* b) {
    int t = *b;
    *b = *a;
    *a = t;
}

int lilysHomework(vector<int> arr) {
    vector<int> sorted_asc(arr);
    sort(sorted_asc.begin(), sorted_asc.end());

    vector<int> sorted_desc(sorted_asc);
    reverse(sorted_desc.begin(), sorted_desc.end());

    map<int,int> vec_pos;
    for (int i = 0; i < arr.size(); i++)
        vec_pos[arr[i]] = i;
    
    int ascSwaps = 0,descSwaps = 0;
    for (int i = 0; i < arr.size(); i++)
    {
        while(sorted_asc[i] != arr[i]) {
            int originalIndex = vec_pos[sorted_asc[i]];
            swap(&sorted_asc[i], &sorted_asc[originalIndex]);
            ascSwaps++;
        }
        while(sorted_desc[i] != arr[i]) {
            int originalIndex = vec_pos[sorted_desc[i]];
            swap(&sorted_desc[i], &sorted_desc[originalIndex]);
            descSwaps++;
        }
    }

    return min(ascSwaps, descSwaps);

}

int main()
{
    cout<< lilysHomework({3,4,2,5,1}) << endl;
    return 0;
}
