
#include <iostream>
#include <algorithm>
using namespace std;

void update(int arr[], int inx, int value) 
{
	arr[inx] = value;
}


int main() {
	
	int arr[] = {0, 1, 2, 3, 4, 5};
	update(arr, 1, 10);

	for (int i = 0; i < sizeof(arr)/sizeof(int) ; i++)
	{
		cout<<arr[i]<<" ";
	}
	cout<<endl;
	return 0;
}

