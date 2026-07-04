def prime_check(n):
    count = 0
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            count +=1

            if n//i != i:
                count +=1
    return count == 2
def prime_factor(n):
    prime_fact = []
    for i in range(1, n+1):
        if n % i == 0:
            if prime_check(i):
                prime_fact.append(i)
    return prime_fact

N = 60
print(prime_factor(N))