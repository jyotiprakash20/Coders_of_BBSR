def longest_substring(s):
    left = 0
    freq = {}
    maxLen = 0
    start = 0

    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1

        while freq[s[right]] > 1:
            freq[s[left]] -= 1
            left += 1

        if right-left+1 > maxLen:
            maxLen = right-left+1
            start = left
    print(s[start:start+maxLen])
    return maxLen


s = "abcabcbb"
print(longest_substring(s))