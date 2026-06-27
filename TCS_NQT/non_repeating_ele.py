# from collections import Counter
# def non_repeating_ele(arr):
#     occ = Counter(arr)

#     res = []
#     for ele, val in occ.items():
#         if val == 1:
#             res.append(ele)
#     return res
   

# arr = [1,2,-1,1,3,1]
# print(non_repeating_ele(arr))

def non_repeating_ele(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0)+1
    res = []
    for num in arr:
        if freq[num] == 1:
            res.append(num)
    return res
arr = [1,2,-1,1,3,1]
print(non_repeating_ele(arr))