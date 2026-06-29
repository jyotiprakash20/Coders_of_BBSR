def avg_arr(arr):
    n = len(arr)

    sum = 0
    for i in range(n):
        sum += arr[i]
    return sum/n
arr = [1,2,1,1,5,1]
print(avg_arr(arr))

#Time Complexity = O(n)
