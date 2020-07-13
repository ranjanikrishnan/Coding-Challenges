def find_min(nums):
    left = 0
    right = len(nums) - 1

    if len(nums) == 0:
        return nums[0]
    if nums[right] > nums[0]:
        return nums[0]

    while right >= left:
        mid = (left + right) // 2
        print('mid: ', mid)
        if nums[mid] > nums[mid+1]:
            return nums[mid+1]
        if nums[mid-1] > nums[mid]:
            return nums[mid]
        if nums[mid] > nums[0]:
            left = mid + 1
        else:
            right = mid - 1


if __name__ == '__main__':
    min_value = find_min([3,4,5,1,2])
    print('min_value: ', min_value)
