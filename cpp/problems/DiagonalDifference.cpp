/*
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9  
The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .

Function description

Complete the  function in the editor below.

diagonalDifference takes the following parameter:

int arr[n][m]: an array of integers
Return

int: the absolute diagonal difference
Input Format

The first line contains a single integer, , the number of rows and columns in the square matrix .
Each of the next  lines describes a row, , and consists of  space-separated integers .

Constraints

Output Format

Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

Sample Input

3
11 2 4
4 5 6
10 8 -12
Sample Output

15
*/

#include "stl.h"
using namespace std;

int diagonalDifference(vector<vector<int>> arr) {
    int a =0, b = 0, N =arr.size();
    int j = 0,k = N - 1;
    for (int i = 0; i < N; i++, j++, k--)
    {
        a += arr[i][j];
        b += arr[i][k];
    }

    return abs(a-b);
}

int main() {
    cout<<diagonalDifference({{1,2,3},{4,5,9},{9,8,9}})<<endl;
}