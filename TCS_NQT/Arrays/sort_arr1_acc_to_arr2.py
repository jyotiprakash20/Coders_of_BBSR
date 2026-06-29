def sort_arr1_to_arr2(arr1,arr2):
    freq = {}
    for num in arr1:
        freq[num] = freq.get(num,0)+1
    res = []
    for num in arr2:
        if num in freq:
            res.extend([num] * freq[num])
            del freq[num]
    remaining = sorted(freq.keys())
    for num in remaining:
        res.extend([num]*freq[num])
    return res
arr1 = [2,1,2,5,7,1,9,3,6,8,8]
arr2 = [2,1,8,3]
print(sort_arr1_to_arr2(arr1,arr2))