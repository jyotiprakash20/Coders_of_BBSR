def circular_subarray(arr):
    arr_sum = 0
    maxSum = float('-inf')
    for i in range(0, len(arr)):
        arr_sum += arr[i]

        if arr_sum > maxSum:
            maxSum = arr_sum
        
        if arr_sum < 0:
            arr_sum = 0
    
    if maxSum < 0:
        return maxSum
    arr_sum = 0  
    minSum = float('inf')
    for i in range(0, len(arr)):
        arr_sum += arr[i]

        if arr_sum < minSum:
            minSum = arr_sum
        
        if arr_sum > 0:
            arr_sum = 0
        
    totalSum = sum(arr)
    circular_sum = totalSum - minSum
    return max(maxSum, circular_sum)
arr = [3, -2, 2, -3]
print(circular_subarray(arr))


    