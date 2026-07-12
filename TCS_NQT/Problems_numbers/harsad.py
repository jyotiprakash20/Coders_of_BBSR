def harsad(n):
    org = n
    sum = 0
    while n > 0:
        d = n % 10
        sum += d
        n //=10
    return org % sum == 0
n = 379
print(harsad(n))