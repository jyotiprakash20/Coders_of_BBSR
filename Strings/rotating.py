'''Left Rotation of a String'''

def left_rotate_string(s, d):
    n=len(s)
    s= list(s)

    for _ in range(d):
        first= s[0]

        for j in range(n-1):
            s[j]= s[j+1]
        s[n-1]= first
    return ''.join(s)

s= "abcdef"
d= 3
result= left_rotate_string(s,d)
print(f'Left rotated string: {result}')