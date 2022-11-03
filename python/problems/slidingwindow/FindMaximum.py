# Importing doubly ended queue
from collections import deque


def find_max_sliding_window(nums, window_size):
    result = []
    window = deque()
    if len(nums) == 0:
        return result
    if window_size > len(nums):
        window_size = len(nums)

    for i in range(0,window_size):
        while window and nums[i] >= nums[window[-1]]:
            window.pop()
        window.append(i)
    result.append(nums[window[0]])

    for i in range(window_size, len(nums)):

        while window and nums[i] >= nums[window[-1]]:
            window.pop()
        
        if window and window[0] <= i - window_size:
            window.popleft()
        window.append(i)
        result.append(nums[window[0]])
    
    
    return result


def main():
    target_list = [18, 2, 1, 2, 4, 3, 2]
    nums_list = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                 [10, 6, 9, -3, 23, -1, 34, 56, 67, -1, -4, -8, -2, 9, 10, 34, 67],
                 [4, 5, 6, 1, 2, 3],
                 [9, 5, 3, 1, 6, 3],
                 [2, 4, 6, 8, 10, 12, 14, 16],
                 [-1, -1, -2, -4, -6, -7],
                 [4, 4, 4, 4, 4, 4]]

    for i in range(len(nums_list)):
        print(i + 1, ". Original array:\t", nums_list[i], sep="")
        print("Input window size:\t\t\t", target_list[i])
        print("Result:\t", find_max_sliding_window(nums_list[i], target_list[i]))
        print("-"*100)


if __name__ == '__main__':
    main()
