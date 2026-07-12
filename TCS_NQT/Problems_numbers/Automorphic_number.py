def automorphic(n):
    sq = n*n
    while n > 0:
        if n % 10 != sq % 10:
            return False
        n //= 10
        sq //= 10
    return True
N = 35
print(automorphic(N)) 