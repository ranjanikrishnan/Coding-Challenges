def search_target(nums, target):
    left = 0
    right = len(nums) - 1

    while right >= left:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target and nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[right] >= target and nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    return -1


if __name__ == '__main__':
    item_index = search_target([3, 4, 5, 1, 2], 5)
    print('item_index: ', item_index)
