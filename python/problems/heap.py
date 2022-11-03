

def heapify(arr):
    for i in range(1, len(arr)):
        x = i
        p = int((x-1)/2)
        print(x,p)
        while x > 0 and arr[p] > arr[x]:
            print("Swap: ", arr[p], arr[x])
            arr[p], arr[x] = arr[x], arr[p]
            x = p
            p = int((x-1)/2)
            print(x,p)
        print("Arr: ", arr)

    return arr

def heappop(arr):
    
    if(len(arr) == 0):
        return -1
    if(len(arr) == 1):
        return arr.pop()
    ret = arr[0]
    arr[0] = arr.pop()

    i = 0
    l = 1
    r = 2
    while i < len(arr):
        s = i
        if l < len(arr) and arr[l] < arr[i]:
            s = l
        if r < len(arr) and arr[r] < arr[s]:
            s = r
        if s != i:
            arr[i], arr[s] = arr[s], arr[i]
            i  = s
            l = 2*i + 1
            r = 2*i + 2
        else:
            break
    print(arr)

    return ret

arr = heapify([2,5,1,27,10,4,3])

while len(arr) > 0:
    print(heappop(arr), sep=' ')


