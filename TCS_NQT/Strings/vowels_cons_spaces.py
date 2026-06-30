def v_c_s(n):
    v = 'aeiouAEIOU'
    vowels = 0
    cons = 0
    space = 0
    for i in n:
        if i in v:
            vowels += 1
        elif i == ' ':
            space += 1
        elif i.isalpha():
            cons += 1
    return vowels, cons, space
n = "India won the cricket match"
print(v_c_s(n))

