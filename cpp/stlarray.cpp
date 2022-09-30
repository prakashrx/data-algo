
#include <iostream>
#include <array>
#include <algorithm>
using namespace std;

void update(array<int,6>& arr, int inx, int value) 
{
	arr[inx] = value;
}


int main() {
	
	array<int, 6> arr = {100, 2, 4, 77, 43, 24};
	update(arr, 1, 10);
    sort(arr.begin(), arr.end());
	for (int i = 0; i < arr.size() ; i++)
	{
		cout<<arr[i]<<" ";
	}
	cout<<endl;
	return 0;
}