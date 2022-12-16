from heapq import *


def k_smallest_pairs(list1, list2, k):
    result = []
    mh = []
    c = 0
    i = 0
    for j in range(len(list2)):
        heappush(mh, (list1[i] + list2[j], i, j))

    while c<k and mh:
        (_, x,y) = heappop(mh)
        result.append((list1[x],list2[y]))
        c += 1

        if (i+1 < len(list1)):
            i += 1
            for j in range(len(list2)):
                heappush(mh, (list1[i] + list2[j], i, j))
    
    return result


print(k_smallest_pairs([1,2,300] , [1,11,20,35,300] , 30))
#print(k_smallest_pairs([2,8,9] , [1,3,6] , 3))