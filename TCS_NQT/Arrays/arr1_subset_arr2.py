def b_search(ele, arr, n):
    start = 0
    end = n-1

    while start <= end:
        mid = (start+end)//2
        if arr[mid] == ele:
            return mid
        elif arr[mid] < ele:
            start = mid+1
        else:
            end = mid-1
    return False
def arr_subset_(arr1,m,arr2,n):
    arr2.sort()
    if m > n:
        return False
    for i in range(m):
        present = b_search(arr1[i],arr2,n)

    if not present:
        return False
    return True
arr1 = [1,3,4,5,2]
m = len(arr1)
arr2 = [11,12,13,15,16]
n = len(arr2)
print(arr_subset_(arr1,m,arr2,n))


