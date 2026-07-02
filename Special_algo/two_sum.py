#If array is sorted use two pointer method
# def two_sum(arr, target):
#     left = 0
#     right = len(arr)-1

#     while left < right:
#         sum = arr[left] + arr[right]

#         if sum == target:
#             return (left+1, right+1)
        
#         elif sum < target:
#             left+=1
#         else:
#             right -=1
#     return []
# arr = [8, 2, 11, 3, 5]
# target = 13
# print(two_sum(arr, target))

#Time complexity = O(n)

#If array is unsorted use hashmap
def hash_unsorted(arr,target):
    hash_map={}
    
    for i in range(len(arr)):
        complement = target - arr[i]

        if complement in hash_map:
            return (hash_map[complement], i)
        hash_map[arr[i]] = i
    return False
arr = [8, 2, 11, 3, 5]
target = 13
print(hash_unsorted(arr,target))