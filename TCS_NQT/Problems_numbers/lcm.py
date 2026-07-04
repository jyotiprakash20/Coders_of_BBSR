def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)
def lcm(a,b):
    g = gcd(a,b)
    return ( a * b) // g
num1 = 4
num2 = 8
print(lcm(num1, num2))