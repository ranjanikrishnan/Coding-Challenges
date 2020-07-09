def max_subarray(nums):
    size = len(nums)
    current_max = nums[0]
    max_ends = 0
    for i in range(0, size):
        max_ends = max_ends + nums[i]
        if (current_max < max_ends):
            current_max = max_ends
        if max_ends < 0:
            max_ends = 0
    return current_max
