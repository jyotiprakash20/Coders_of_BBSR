# def gre_two(n1,n2):
#     if n1 > n2:
#         return n1
#     elif n1 < n2:
#         return n2
#     else:
#         return None
# n1 = 3
# n2 = 3
# print(gre_two(n1,n2))

def gre_three(n1,n2,n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3
n1 = 3
n2 = 3
n3 = 2
print(gre_three(n1,n2,n3))

