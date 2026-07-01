# def anagrams(s1,s2):
#     s1 = s1.strip()
#     s2 = s2.strip()
#     if len(s1) != len(s2):
#         return False
#     freq = {}
#     for ch in s1:
#         freq[ch] = freq.get(ch,0)+1
#     for ch in s2:
#         if ch not in freq:
#             return False
#         freq[ch] -= 1
#         if freq[ch] == 0:
#             del freq[ch]
#     return len(freq)==0
# s1 = ' CAT'
# s2 = 'ACT'
# print(anagrams(s1,s2))

def anagrams(s1,s2):
    s1 = s1.strip()
    s2 = s2.strip()
    if len(s1) != len(s2):
        return False
    freq = [0]*26

    for ch in s1:
        freq[ord(ch)-ord('A')]+=1
    for ch in s2:
        freq[ord(ch)-ord('A')] -= 1
    for count in freq:
        if count != 0:
            return False
    return True
s1 = 'RULES'
s2 = 'LESRT'
print(anagrams(s1,s2))

#Time complexity = O(n)
    