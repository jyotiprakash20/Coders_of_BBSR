def remove_brackets(n):
    b = '()[]{}'
    res = ''
    for ch in n:
        if ch not in b:
            res += ch
    return res
ex = 'a+((b-c)+d)'
print(remove_brackets(ex))