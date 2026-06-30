# def palindrome_str(n):
#     rev = ''
#     for i in n:
#         rev = i + rev
#     if s == rev:
#         return True
#     else:
#         return False
# s = 'ABCDCBA'
# print(palindrome_str(s))

def palindrome_str(n):
    left = 0
    right = len(n)-1
    

    while left < right:
        if n[left] != n[right]:
            
            return False
        left += 1
        right -= 1
    return True
s = 'TAKE U FORWARD'
if palindrome_str(s):
    print('Palindrome')
else:
    print('Not palindrome')

#Time complexity= O(n)
