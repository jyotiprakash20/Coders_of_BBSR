def cap_first_last(n):
    res = list(n)
    n = len(res)
    start = 0
    while start < n:
        while start < n and res[start] == ' ':
            start += 1
        if start > n:
            break
        end = start
        while end < n and res[end] != ' ':
            end += 1
        if res[start].islower():
            res[start] = res[start].upper()
        if end-1 > start and res[end-1].islower():
            res[end-1] = res[end-1].upper()
        start = end
    return ''.join(res)
s = 'I am a boy'
print(cap_first_last(s))