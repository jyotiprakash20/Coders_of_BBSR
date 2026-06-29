# def remove_duplicate(arr):
#     seen = set()
#     index = 0
#     for num in arr:
#         if num not in seen:
#             seen.add(num)
#             arr[index] = num
#             index +=1
#     return index
# arr = [1,1,2,2,2,3,3]        
# print(remove_duplicate(arr))
# print(arr[:remove_duplicate(arr)])

#Optimal solution
def remove_duplicate(arr):
    if not  arr:
        return 0
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i +=1
            arr[i] = arr[j]
    return i+1
arr = [1,1,2,2,2,3,3]        
length = remove_duplicate(arr)

print(length)
print(arr[:length])

#Time complexity = O(n)
