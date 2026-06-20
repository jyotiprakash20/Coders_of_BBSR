'''Count of substrings that start and end with 1 in given Binary String'''

def count_one(str):
    n= len(str)

    count=0

    for i in range(n):
        for j in range(i+1, n):
            if str[j]=='1' and str[i]=='1':
                count +=1
    return count

str= '10101'
result= count_one(str)
print(result)

