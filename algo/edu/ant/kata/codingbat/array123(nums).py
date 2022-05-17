def array123(nums):

    string = ""

    for item in nums:
        string += str(item)

    return "123" in string


# or

# for i in range(len(nums)-2):
    # if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
        # return True
# return False