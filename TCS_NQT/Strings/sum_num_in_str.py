def sum_num_str(n):
    sum = 0
    temp = ''
    for ch in n:
        if ch.isdigit():
            temp += ch
        else:
            if temp != '':
                sum += int(temp)
                temp = ''
    if temp != '':
        sum += int(temp)
    return sum
   
n = '1xyz23'
print(sum_num_str(n))