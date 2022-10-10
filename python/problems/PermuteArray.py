# https://www.hackerrank.com/challenges/two-arrays/problem

def twoArrays(k, A, B):
    
    a = sum([ max(0, k-x) for x in A])
    b = sum([ max(0, k-x) for x in B])
    return "YES" if a + b <= k*len(A) else "NO"


print(twoArrays(5, [1,2,2,1], [3,3,3,4]))
print(twoArrays(10, [2,1,3], [7,8,9]))
print(twoArrays(10, [10000, 1, 1, 1], [1,1,1,1]))
