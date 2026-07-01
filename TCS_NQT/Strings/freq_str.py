# def freq_str(n):
#     res = list(n)
#     freq = {}
#     for i in res:
#         freq[i] = freq.get(i, 0)+1
#     for ch in sorted(freq):
#         print(ch, freq[ch], sep=' ', end=' ')
# s = 'takeuforward'
# freq_str(s)

#Time complexity = O(n+ klogk)

def freq_chr(n):
    freq = [0]*26
    for ch in n:
        freq[ord(ch)-ord('a')]+=1
    for i in range(26):
        if freq[i] != 0:
            print(f"{chr(i+ord('a'))}{freq[i]}", end = ' ')
s = 'articles'
freq_chr(s)