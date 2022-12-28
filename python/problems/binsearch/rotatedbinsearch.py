

def binary_search_rotated(arr,  n):
    
    l = 0
    r = len(arr)  - 1

    while l<=r:
        m = (l+r)//2
        if arr[m] == n:
            return m
        
        if arr[l] <= arr[m]:
            if  n >= arr[l] and n < arr[m]:
                r = m - 1
            else:
                l = m + 1
        else:
            if n > arr[m] and n <= arr[r]:
                l = m + 1
            else:
                r = m - 1
    return -1




print(binary_search_rotated([6,7,1,2,3,4,5] , 3))
print(binary_search_rotated([4] , 1))
