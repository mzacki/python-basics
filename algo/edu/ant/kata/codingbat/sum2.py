def sum2(nums):
    end_index = len(nums) if len(nums) < 2 else 2
    result = 0
    for i in range (end_index):
        result += nums[i]

    return result
