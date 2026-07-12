def abundant(n):
    sum = 1
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            sum += i

            if n // i != i:
                sum+= n // i
    return sum > n
n = 21
print(abundant(n))
