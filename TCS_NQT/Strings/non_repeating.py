def non_repeat(n):
    freq = {}
    for ch in n:
        freq[ch] = freq.get(ch, 0)+1
    res = []
    for ch in n:
        if freq[ch] == 1:
            res.append(ch)
    return ''.join(res)
s = 'google'
print(non_repeat(s))