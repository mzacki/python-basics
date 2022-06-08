def max_end3(nums):
    max_item = max([nums[0], nums[-1]])
    new_list = []
    new_list.extend([max_item for i in range(3)])

    return new_list

