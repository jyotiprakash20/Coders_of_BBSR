# def remove_vowels(n):
#     v = 'aeiouAEIOU'
#     res = []
#     for ch in n:
#         if ch not in v:
#             res.append(ch)
#     return ''.join(res)
# s = 'take u forward'
# print(remove_vowels(s))


#Remove space
def remove_space(n):
    v = ' '
    res = ''
    for ch in n:
        if ch not in v:
            res += ch
    return res
s = 'take U forward'
print(remove_space(s))
