def ap_series(n, a, d):
    sum = 0
    for i in range(1, n+1):
        sum += a
        a += d
    return sum
n = 8
a = 2
d = 5  
print(ap_series(n,a,d))

