'''Binary String'''

def binary_string(s):
    n= len(s)

    for i in range(n):
        if s[i] == '0' or s[i]=='1':
            return True
    return False

str='abc'
result= binary_string(str)
print(result)
