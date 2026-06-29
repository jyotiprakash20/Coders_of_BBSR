def palindrom(num):
    org = num
    rev = 0

    while num > 0:
        dig = num % 10
        rev = rev * 10 + dig
        num //= 10
    return org == rev
def palindrome_in_range(min, max):
    for i in range(min, max+1):
        if palindrom(i):
            print(i, end=' ')
    
n1 = 10
n2 = 50
palindrome_in_range(n1,n2)
   