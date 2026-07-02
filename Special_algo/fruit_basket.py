def fruit_basket(arr):
    left = 0
    freq = {}
    ans = 0

    for right in range(len(arr)):
        freq[arr[right]] = freq.get(arr[right],0)+1

        while len(freq) > 2:
            freq[arr[left]] -= 1

            if freq[arr[left]] == 0:
                del freq[arr[left]] 
            left +=1
        ans = max(ans, right-left+1)
    return ans
arr = [1,2,3,2,2]
print(fruit_basket(arr))