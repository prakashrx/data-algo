def next(arr, index, direction):
    if index < 0 or index >= len(arr):
        return None
    forward = arr[index] > 0
    if forward != direction:
        return None
    
    if forward:
        return (index + arr[index]) % len(arr)
    else:
        return (len(arr) + index + arr[index]) % len(arr)

def is_cycle(arr, index):
    direction = arr[index] > 0
    slow = index
    fast = next(arr, index, direction)
    while fast != slow and fast is not None:
        slow = next(arr, slow, direction)
        fast = next(arr, fast, direction)
        if fast is not None:
            fast = next(arr, fast, direction)
    return fast is not None


def circular_array_loop(arr):  
    for i in range(len(arr)):
        if is_cycle(arr, i):
            return True
    return False

print(circular_array_loop([1,3,-2,-4,1]))
print(circular_array_loop([2,1,-1,2]))
