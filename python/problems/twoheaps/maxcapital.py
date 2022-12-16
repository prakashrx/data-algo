from heapq import heappush, heappop, heapify

def maximum_capital(c, k, capitals, profits):
    minheap = []
    maxheap = []
    total = c
    for i, c in enumerate(capitals):
        heappush(minheap, (c,i))
    for i in range(k):
        while minheap and total >= minheap[0][0]:
            _, i = heappop(minheap)
            heappush(maxheap, -profits[i])
        if not maxheap:
            break
        
        total += -(heappop(maxheap))
        

    return total

    

print(maximum_capital(1 , 2 , [1,2,2,3] , [2,4,6,8]))