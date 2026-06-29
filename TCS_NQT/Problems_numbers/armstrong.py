def armstrong(n):
    org = n
    power = len(str(n))
    temp = 0
    while n != 0:
        d = n % 10
        temp += d ** power
        n //= 10
    return temp == org
n = 153
print(armstrong(n))



