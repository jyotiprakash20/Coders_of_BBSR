'''Check if two arrays are equal or not'''

def is_equal(a,b):
    if len(a) != len(b):
        return False
    return sorted(a) == sorted(b)

a=[1,2,3,4,5,6]
b=[6,5,4,3,2,0]

if is_equal(a,b):
    print('True')
else:
    print('False')
    