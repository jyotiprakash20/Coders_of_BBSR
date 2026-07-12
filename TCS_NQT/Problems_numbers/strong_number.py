def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
def strong_num(n):
    org = n
    sum = 0
    while n > 0:
        d = n % 10
        sum += fact(d)
        n //=10
    return sum == org
N = 145
print(strong_num(N))