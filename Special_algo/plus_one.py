def plus_one(nums):
    right = len(nums)-1
    for i in range(right, -1,-1):
        if nums[i] < 9:
            nums[i]+= 1
            return nums
        nums[i] = 0
    return [1]+nums
arr = [1, 2, 9]
print(plus_one(arr))