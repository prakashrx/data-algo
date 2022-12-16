def min_sub_array_len(target, nums):
    left = 0
    length = float('inf')
    s = 0
    for right in range(len(nums)):
        s += nums[right]
        while s >= target:
            s -= nums[left] 
            length = min(length, right - left + 1) 
            left += 1

    return 0 if length > len(nums) else length



print(min_sub_array_len(7, [2,3,1,2,4,3]))
print(min_sub_array_len(11, [1,1,1,1,1,3]))
print(min_sub_array_len(4, [1,4,4]))
print(min_sub_array_len(10, [1,2,3,4]))
print(min_sub_array_len(5, [1,2,1,3]))
