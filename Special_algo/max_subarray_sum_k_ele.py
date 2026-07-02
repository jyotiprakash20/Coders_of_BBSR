def maxKsum(arr,k):
    n = len(arr)
    maxEndHere = [0]*n
    maxEndHere[0] = arr[0]

    for i in range(1,n):
        maxEndHere[i] = max(arr[i], maxEndHere[i-1]+arr[i])

    windowSum = sum(arr[:k]) 
    ans = windowSum
    for i in range(k,n):
        windowSum += arr[i]-arr[i-k]
        ans = max(ans, windowSum)
        ans = max(ans, windowSum+maxEndHere[i-k])
    return ans
arr = [1,2,3,4,5]

k = 5
print(maxKsum(arr,k))