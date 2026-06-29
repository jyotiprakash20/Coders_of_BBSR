def palindrom(num):
    org = num
    rev = 0

    while num > 0:
        dig = num % 10
        rev = rev * 10 + dig
        num //= 10
    return org == rev
num = 7789 
if palindrom(num):
    print('Palindrome')
else:
    print('Not a palindrome')

#Time complexity = O(n)