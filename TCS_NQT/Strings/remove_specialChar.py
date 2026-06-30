def remove_special(n):
    res = ''
    for ch in n:
        if  ch.isalpha() or ch == ' ':
            res += ch
    return res
s = 'take12% *&u ^$#forward'
print(remove_special(s))
