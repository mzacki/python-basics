def array_front9(nums):
    if len(nums) < 4:
        end_index = len(nums)
    else:
        end_index = 4

    for i in range(end_index):
        if nums[i] == 9:
            return True

    return False

