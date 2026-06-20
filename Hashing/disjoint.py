'''Check for Disjoint Arrays or Sets'''

def is_disjoint(a,b):

    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j]:
                return False
    return True

a=[2,3,4,6]
b=[1,9,7,8]

if is_disjoint(a,b):
    print('True')
else:
    print('False')