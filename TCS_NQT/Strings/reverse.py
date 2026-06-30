# def reverse(n):
#     rev = ''
#     for ch in n:
#         rev = ch + rev
#     return rev
# s = 'I am iron man'
# print(reverse(s))

#Time complexity = O(n**0.5)

def reverse_optimal(n):
    res = list(s)
    left = 0
    right = len(s)-1

    while left < right:
        res[left], res[right] = res[right], res[left]
        left += 1
        right -= 1
    return ''.join(res)

s = 'I am iron man'
print(reverse_optimal(s))

#Time coplexity = O(n)    