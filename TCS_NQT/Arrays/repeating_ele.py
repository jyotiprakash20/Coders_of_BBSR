# def repeating_ele(arr):
#     arr.sort()
#     res = []
#     for i in range(len(arr)-1):
#         if arr[i] == arr[i+1]:
#             res.append(arr[i])
#     return res

# arr = [1, 1, 2, 3, 4, 4, 5]
# print(repeating_ele(arr))

#Time complexity = O(nlogn)

from collections import Counter
def repeating_ele(arr):
    Occ = Counter(arr)

    res = []
    for key,value in Occ.items():
        if value > 1:
            res.append(key)
    return res

arr = [1, 1, 2, 3, 4, 4, 5,2]
print(repeating_ele(arr))

#Time complexity = O(n)