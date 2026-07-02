def sum_closest(arr, target):
    arr.sort()
    closest = arr[0]+arr[1]+arr[2]

    for i in range(0, len(arr)-2):
        left = i+1
        right = len(arr)-1

        while left < right:
            currSum = arr[i]+arr[left]+arr[right]

            if abs(currSum-target) < abs(closest-target):
                closest = currSum
            if currSum < target:
                left +=1
            elif currSum > target:
                right -= 1
            else:
                return currSum
    return closest
arr = [-1,2,1,-4]
target = 3                                      
print(sum_closest(arr,target)) 