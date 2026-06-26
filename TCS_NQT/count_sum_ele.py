def count_sum(arr):
    n = len(arr)

    sum = 0
    for i in range(n):
        sum += arr[i]
    return sum
arr = [1,2,1,1,5,1]
print(count_sum(arr))

#Time Complexity = O(n)