# def gp(a,r,n):
#     sum = 0
#     term = a
#     for _ in range(n):
#         sum += term
#         term *= r
#     return sum
# a=1 
# r=0.5 
# n=3
# print(gp(a,r,n))

#Time complexity = O(n)

def gp(a,r,n):
    if r==0 or r==1:
        return a*n
    else:
        return a*(r**n-1)/(r-1)

a=3 
r=5 
n=2
print(gp(a,r,n))

#Time complexity = O(1)
