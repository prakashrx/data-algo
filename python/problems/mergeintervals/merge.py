from interval import *


def merge_intervals(v):
    # write your code here
    result = []
    result.append(v[0])

    for i in range(1, len(v)):
        if v[i].start <= result[-1].end:
            result[-1].end = max(v[i].end, result[-1].end)
        else:
            result.append(v[i])

    return result