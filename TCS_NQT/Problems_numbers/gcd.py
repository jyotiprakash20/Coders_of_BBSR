def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a
N1 = 9
N2 = 12
print(gcd(N1,N2))