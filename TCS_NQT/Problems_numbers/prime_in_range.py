def prime(n):
    count = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            count += 1
            if n // i != i:
                count +=1
    return count == 2
def prime_range(min, max):
    res = []
    for i in range(min, max+1):
        if prime(i):
            res.append(i)
    return res
n1 = 10
n2 = 16
print(prime_range(n1,n2))

#Time complexity = O(n**0.5)