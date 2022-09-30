
from functools import reduce

def lonelyinteger(a):
    return reduce(lambda i,j: i ^ j, a)

print(lonelyinteger([1,2,3,4,3,2,1]))