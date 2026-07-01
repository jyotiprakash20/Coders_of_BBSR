def reverse_digit(n):
    rev = 0
    while n > 0:
        d = n % 10
        rev = rev * 10 + d
        n //=10
    return rev
n = 7789 
print(reverse_digit(n))