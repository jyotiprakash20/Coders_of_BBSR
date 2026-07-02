def max_min(n):
    max = float('-inf')
    min = float('inf')
    while n > 0:
        d = n % 10
        if d > max:
            max = d
        if d < min:
            min = d
        n //= 10
    return min, max
n = 6
print(max_min(n))