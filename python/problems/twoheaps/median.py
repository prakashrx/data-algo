from heapq import *

def median_sliding_window1(nums, k):
    
    max_heap=[]
    min_heap = []
    for i in range(len(nums)):
        heappush(min_heap, nums[i])
        if len(min_heap) > len(max_heap) + 1:
            heappush(max_heap, -heappop(min_heap))

    while max_heap:
        print(-heappop(max_heap))
    print("---")
    while min_heap:
        print(heappop(min_heap))
    return []

def median_sliding_window(nums, k):
    max_heap=[]
    min_heap = []
    outputs = []
    for i in range(k):
        heappush(min_heap, (nums[i], i))
        
    while len(min_heap) > len(max_heap) + 1:
        (num, ix) = heappop(min_heap)
        heappush(max_heap, (-num, ix))
    if k % 2 == 0:
        outputs.append(float((min_heap[0][0] -max_heap[0][0])/2))
    else:
        outputs.append(float(min_heap[0][0]))

    for i in range(k, len(nums)):
        heappush(min_heap, (nums[i], i))
        if len(min_heap) > len(max_heap) + 1:
            (num, ix) = heappop(min_heap)
            heappush(max_heap, (-num, ix))
        
        while min_heap and min_heap[0][1] <= i - k:
            heappop(min_heap)
        while max_heap and max_heap[0][1] <= i - k:
            heappop(max_heap)

        while len(min_heap) > len(max_heap) + 1:
            (num, ix) = heappop(min_heap)
            heappush(max_heap, (-num, ix))

        while len(max_heap) > len(min_heap):
            (num, ix) = heappop(max_heap)
            heappush(min_heap, (-num, ix))

        if k % 2 == 0:
            outputs.append(float((min_heap[0][0] -max_heap[0][0])/2))
        else:
            outputs.append(float(min_heap[0][0]))

    return outputs


#median_sliding_window1([1,3,-1,-3,5,3,6,7] , 3)
#print(median_sliding_window([1,3,-1,-3,5,3,6,7] , 3))
print(median_sliding_window([10,-7,5,-10,-11,-5,3,7] , 7))

