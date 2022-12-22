
def search(arr, n):
    l,r = 0, len(arr)-1
    while l<=r:
        m = int((l + r)/2)
        if n == arr[m]:
            return m
        elif n < arr[m]:
            r = m - 1
        else:
            l = m + 1

    return l


arr = [3,6,10,23,56,77,80,91,92,94,99]
for ix,i in enumerate(arr):
    assert(search(arr, i) == ix)


assert(search(arr, 5) == 1)
assert(search(arr, 100) == len(arr))
assert(search(arr, 98) == len(arr) - 1)
assert(search(arr, 1) == 0)