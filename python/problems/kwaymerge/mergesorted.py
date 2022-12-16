
def merge_sorted(nums1, m, nums2, n):
    
    p1 = m-1
    p2 = n-1
    p = len(nums1) - 1

    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p -= 1
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p -= 1
            p2 -= 1

    return nums1


print(merge_sorted([6, 7, 8, 9, 10, 0, 0, 0, 0, 0] , 5 , [1, 2, 3, 4, 5] , 5))