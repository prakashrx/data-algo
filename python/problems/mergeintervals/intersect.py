from interval import Interval

# Function to find the intersecting points between two intervals
def intervals_intersection(a, b):
    
    i,j = 0,0
    result = []
    while i<len(a) and j<len(b):

        start = max(a[i].start, b[j].start)
        end = min(a[i].end, b[j].end)
        
        if start <= end:
            result.append(Interval(start,end))
        
        if a[i].end < b[j].end:
            i += 1
        else:
            j += 1

    return result