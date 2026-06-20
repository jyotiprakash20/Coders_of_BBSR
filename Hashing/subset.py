'''Check if an array is subset of another array'''

def is_subset(a,b):
    hash_set=set(a)

    for num in b:
        if num not in hash_set:
            return False
    return True
a=[4,55,43,78,2,9]
b=[2,9,54]

if is_subset(a,b):
    print('True')
else:
    print('False')

       