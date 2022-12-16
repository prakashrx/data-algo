from interval import Interval

def employee_free_time(schedule):  
    result = []
    
    intervals = [item for l in schedule for item in l]
    intervals = sorted(intervals, key= lambda x: x.start)
    
    end = intervals[0].end

    for i in range(len(intervals)):
        if intervals[i].start > end:
            result.append(Interval(end, intervals[i].start))
        end = max(end, intervals[i].end)

    return result