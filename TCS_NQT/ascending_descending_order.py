def asc_des(arr):
    arr.sort()
    n = len(arr)

    arr[n // 2:] = reversed(arr[n//2:])
    return arr
arr = [4, 2, 8, 6, 15, 5, 9, 20]
print(asc_des(arr))

#Ttime Complexity = O(nlogn)