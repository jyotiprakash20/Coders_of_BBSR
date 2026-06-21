#Find the smallest element in an array

def min_ele(arr):
    n = len(arr)
    min = arr[0]
    for i in range(n):
        if arr[i] < min:
            min = arr[i]
    return min

arr = [2, 5, 1, 3, 0] 
print(min_ele(arr))


#Find the largest element in an array
def max_ele(arr):
    n = len(arr)
    max = arr[0]
    for i in range(n):
        if arr[i] > max:
            max = arr[i]
    return max

arr = [2, 5, 1, 3, 0] 
print(max_ele(arr))