# def fib(n):
#     if n <= 1:
#         return n
    
#     return fib(n-1)+fib(n-2)
     
# n = 5
# for i in range(n+1):
#     print(fib(i), end = ' ')
#Time complexity = O(2^n)

def fibonacci(n):
    if n <= 1:
        return n
    
    a = 0
    b = 1
    for i in range(2,n+1):
        c = b + a
        a = b
        b = c
    return c
n = 5
for i in range(n+1):
    print(fibonacci(i), end = ' ')

#Time complexity = O(n)