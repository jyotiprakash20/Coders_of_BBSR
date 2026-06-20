'''Fizz Buzz'''

def fizz_buzz(n):

    res=[]

    for i in range(1, n+1):
        if i%3==0 and i%5==0:
            res.append('Fizz Buzz')
        elif i%3==0:
            res.append('Fizz')
        elif i%5==0:
            res.append('Buzz')
        else:
            res.append(str(i))
    return res

n=10
result= fizz_buzz(n)
print(' '.join(result))