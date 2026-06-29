def firstNonrepating(arr):
    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0)+1
    for num in arr:
        if freq[num] == 1:
            return num
    return 0
arr = [-1, 2, -1, 3, 2]
print(firstNonrepating(arr))  