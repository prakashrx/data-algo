def find_sum_of_three(nums, target):
   # your code will replace this placeholder return statement
    nums = sorted(nums)
    for i in range(len(nums) - 1):
        t = target - nums[i]
        left = i + 1
        right = len(nums) - 1
        while left < right:
            s = nums[left] + nums[right]
            if s == t:
                return True
            if s < t:
                left += 1
            else:
                right -= 1
    return False


print(find_sum_of_three([3,7,1,2,8,4,5], 20))