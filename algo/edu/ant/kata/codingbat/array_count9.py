def array_count9(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] == 9:
            count = count + 1

    return count

# or

def array_count9_2(nums):
    count = 0
    for num in nums:
        if num == 9:
            count = count + 1

    return count
