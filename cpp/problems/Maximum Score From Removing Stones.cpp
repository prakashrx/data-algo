/*
One Integer
You are playing a solitaire game with three piles of stones of sizes a​​​​​​, b,​​​​​​ and c​​​​​​ respectively. Each turn you choose two different non-empty piles, take one stone from each, and add 1 point to your score. The game stops when there are fewer than two non-empty piles (meaning there are no more available moves).

Given three integers a​​​​​, b,​​​​​ and c​​​​​, return the maximum score you can get.

Constraints:

1 <= a, b, c <= 10^5

Example:

Input: a = 2, b = 4, c = 6
 
Output: 6
 
Explanation: The starting state is (2, 4, 6). One optimal set of moves is:
- Take from 1st and 3rd piles, state is now (1, 4, 5)
- Take from 1st and 3rd piles, state is now (0, 4, 4)
- Take from 2nd and 3rd piles, state is now (0, 3, 3)
- Take from 2nd and 3rd piles, state is now (0, 2, 2)
- Take from 2nd and 3rd piles, state is now (0, 1, 1)
- Take from 2nd and 3rd piles, state is now (0, 0, 0)
There are fewer than two non-empty piles, so the game ends. Total: 6 points.

*/
#include "stl.h"
using namespace std;

int maximumScore(int a, int b, int c) {
    priority_queue<int> pq;
    pq.push(a); pq.push(b); pq.push(c); 
    int moves = 0;
    while(pq.size() > 1) {
      c = pq.top(); pq.pop();
      b = pq.top(); pq.pop();
      c--; b--;
      if(c) pq.push(c);
      if(b) pq.push(b);
      moves++;
    }
    return moves;
}

int maximumScore2(int a, int b, int c) {
    int s = a + b + c;
    int nimsum = a ^ b ^ c;
    return (s - nimsum)/2;
}

int main() {
  cout<<maximumScore(2, 4, 6)<<" "<<maximumScore2(2, 4, 6)<<endl;
  cout<<maximumScore(2, 2, 2)<<" "<<maximumScore2(2, 2, 2)<<endl;
  cout<<maximumScore(1, 2, 6)<<" "<<maximumScore2(1, 2, 6)<<endl;
  cout<<maximumScore(2, 3, 3)<<" "<<maximumScore2(2, 3, 3)<<endl;
  return 0;
}
