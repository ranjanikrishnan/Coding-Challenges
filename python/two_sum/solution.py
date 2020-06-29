def two_sum(nums, target):
    sum_indexes = {}
    for index, value in enumerate(nums):
        if (target - value) in sum_indexes:
            return index, sum_indexes[target-value]
        sum_indexes[value] = index


two_sum_indexes = two_sum([2, 7, 11, 15], 9)
print(two_sum_indexes)
