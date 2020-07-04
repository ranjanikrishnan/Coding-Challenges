def contains_duplicate(nums):
    sorted_nums = sorted(nums)
    print('sorted_nums: ', sorted_nums)
    try:
        for index, value in enumerate(sorted_nums):
            if value == sorted_nums[index+1]:
                return True
        return False
    except IndexError as e:
        print(e)
