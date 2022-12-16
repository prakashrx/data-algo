
#  [[1, 3], [4, 5], [7, 8], [9, 12], [13, 14]]

# [2, 10]


def insert_interval(existing_intervals, new_interval):

    result = []

    i = 0
    n = len(existing_intervals)

    while i < n and new_interval.start > existing_intervals[i].start:
        result.append(existing_intervals[i])
        i += 1

    if new_interval.start <= result[-1].end:
        result[-1].end = max(new_interval.end, result[-1].end)
    else:
        result.append(new_interval)

    while i < n:
        if existing_intervals[i].start <= result[-1].end:
            result[-1].end = max(existing_intervals[i].end, result[-1].end)
        else:
            result.append(existing_intervals[i])
        i += 1

    return result