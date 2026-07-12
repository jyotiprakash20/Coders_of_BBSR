def max_min(n):
    min = float('inf')
    max = float('-inf')

    while n > 0:
        d = n % 10
        if d < min:
            min = d
        if d > max:
            max = d
        n //= 10
    return min , max
N = 2746
print(max_min(N))
