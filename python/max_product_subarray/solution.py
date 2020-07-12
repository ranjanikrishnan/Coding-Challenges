def max_product(nums):
    maximum = curMax = curMin = nums[0]
    for i in range(1, len(nums)):
        c = curMax
        curMax = max(nums[i], max(c*nums[i], curMin*nums[i]))
        curMin = min(nums[i], min(c*nums[i], curMin*nums[i]))
        maximum = max(curMax, maximum)
    return maximum


if __name__ == '__main__':
    max_prod_value = max_product([2,3,-2,4])
    print(max_prod_value)
