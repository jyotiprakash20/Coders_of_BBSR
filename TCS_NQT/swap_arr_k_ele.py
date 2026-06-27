#Using Temporary array
# def rotate(arr, k):
#     n = len(arr)
#     k %= n
#     temp = [0]*n

#     for i in range(n-k):
#         temp[i] = arr[k+i]
#     for i in range(k):
#         temp[n-k+i] = arr[i]
#     for i in range(n):
#         arr[i] = temp[i]
    
# arr = [1, 2, 3, 4, 5]
# k = 2
# print(rotate(arr,k))

#Time complexity = O(n)

#Using reverse algorithim
def reverse(arr,start,end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
        
def left_rotate(arr,k):
    n = len(arr)
    k %= n

    reverse(arr,0,k-1)
    reverse(arr,k,n-1)
    reverse(arr,0,n-1)
    return arr

   
arr = [1, 2, 3, 4, 5]
k = 2
print(left_rotate(arr,k))

#Time Complexity = O(n)