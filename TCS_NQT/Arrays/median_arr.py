def median_arr(arr):
    n = len(arr)
    arr.sort()

    if n % 2 == 0:
        index1 = (n//2)-1
        index2 = (n//2)
        return (arr[index1] + arr[index2])/2
    else:
        return arr[n//2]

    

arr =  [2,5,1,7]
print(median_arr(arr))