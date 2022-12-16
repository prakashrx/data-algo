from heapq import *


def k_smallest_number(lists, k):
    mh = []
    for list in lists:
        if list:
            heappush(mh, (list[0], list, 0))
    c = 0
    last = 0
    while c < k and mh:
        (x, list, i) = heappop(mh)
        last = x
        if i + 1 < len(list):
            heappush(mh, (list[i+1],list, i+1))

        c += 1
    return last

print(k_smallest_number([[2,6,8],[3,7,10],[5,8,11]] , 5))
print(k_smallest_number([[],[],[]] , 5))