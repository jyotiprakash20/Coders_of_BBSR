
def count_freq(arr):
    freq = {}

    for num in arr:
        if num in freq:
            freq[num] +=1
        else:
            freq[num] = 1
    return freq

arr = [10,5,10,15,10,5]
print(count_freq(arr))

# def count_freq(arr):
#     freq = {}

#     for num in arr:
#         freq[num] = freq.get(num,0)+1
#     return freq
# arr = [10,5,10,15,10,5]
# print(count_freq(arr))