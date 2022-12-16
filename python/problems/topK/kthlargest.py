from heapq import *
# Tip: You may use some of the code templates provided
# in the support files

class KthLargest:
    # constructor to initialize heap and add values in it
    def __init__(self, k, nums):
        mh = []
        for i in nums:
            if len(mh) < k:
                heappush(mh, i)
            elif mh[0] < i:
                heappop(mh)
                heappush(mh, i)
        self.mh = mh

    # adds element in the heap
    def add(self, val):
        if self.mh[0] < val:
            heappop(self.mh)
            heappush(self.mh, val)
        return self.return_Kth_largest()
        
    def return_Kth_largest(self):
        return self.mh[0]