def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start +=1
        end -=1
def rotateArr(nums,k, direction):
    n = len(nums)
    if n == 0 or k == 0:
        return nums
    k %= n
    if direction == 'right' or direction == 'Right':
        reverse(nums, 0, n-1)
        reverse(nums,0,k-1)
        reverse(nums,k, n-1)
    elif direction == 'left' or direction == 'Left':
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)
        reverse(nums,0,n-1)
    return nums

arr =  [1, 2, 3, 4, 5, 6]
k = 2
# direction1 = 'right'
# print(rotateArr(arr,k,direction1))
direction2= 'left'
print(rotateArr(arr,k,direction2))

#Time complexity = O(n)

        