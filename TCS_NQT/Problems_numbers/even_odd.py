def even_odd(n):
    if n & 1 == 0:
        return 'Even'
    else:
        return 'Odd'
n = 765486446183645375
print(even_odd(n))