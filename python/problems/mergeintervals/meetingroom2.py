from interval import Interval
import heapq

def find_sets(intervals):
    mh = []
    intervals = sorted(intervals, key=lambda x: x[0])
    mh.append(intervals[0][1])
    for i in range(1, len(intervals)):
        if intervals[i][0] >= mh[0]:
            heapq.heappop(mh)
        heapq.heappush(mh, intervals[i][1])
    return len(mh)