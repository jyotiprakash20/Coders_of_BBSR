# using kaden's algorithim
def maxSum(arr):
    s = 0
    Max_sum = float('-inf')
    arr_start = -1
    arr_end = -1
    for i in range(0, len(arr)):
        if s == 0:
            start = i
        s += arr[i]

        if s > Max_sum:
            Max_sum = s
            arr_start = start
            arr_end = i
        if s < 0:
            s = 0
    print(arr[arr_start:arr_end+1])
    return Max_sum, arr_start, arr_end
nums = [-3, 2, -1, 4, -2]
print(maxSum(nums))

