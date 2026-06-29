def remove_dup_unsorted(arr):
    seen = {}
    result = []
    for num in arr:
        if num not in seen:
            result.append(num)
            seen[num] = True
    return result
arr = [4,3,9,2,4,1,10,89,34]
print(remove_dup_unsorted(arr))

#Time complexity = O(n)