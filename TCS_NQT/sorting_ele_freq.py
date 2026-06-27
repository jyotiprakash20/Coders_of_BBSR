def sorting_ele_freq(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0)+1
    arr.sort(key = lambda x: (freq[x],x))
    return arr
arr =  [-199,6,7,-199,3,5]
print(sorting_ele_freq(arr))

#Time complexity = O(nlog n)