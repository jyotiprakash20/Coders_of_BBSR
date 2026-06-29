# def prime(num):
#     if num < 2:
#         return False
#     for i in range(2,int(num**0.5)+1):
#         if num % i == 0:
#             return False
#     return True
# num = 1033
# print(prime(num))

#Time complexity = O(n**0.5)

# def prime(num):
#     count = 0
#     for i in range(1,int(num**0.5)+1):
#         if num % i == 0:
#             count += 1
#             if num//i != i:
#                 count +=1
#     return  count
# n = 10
# print(prime(n))

def prime(num):
    res = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            res.append(i)
            if num // i != i:
                res.append(num//i)
    return sorted(res)
n = 10
print(prime(n))