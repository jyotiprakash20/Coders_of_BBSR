#Question
# def rain_pred(n):
    
#     if n == 'Yes' or n=='yes':
#         return 'Carry an Umbrella'
#     else:
#         return 'Bye'

# n= input("Is it raining?: ")
# print(rain_pred(n))

#Question 2
# def rain_pred(n):
    
#     if n == 'Yes' or n=='yes':
#         return 'Carry an Umbrella'
#     elif n=='No' or n=='no':
#         return 'No need to carry umbrella'
#     else:
#         return 'Bye'

# n= input("Is it raining?: ")
# print(rain_pred(n))

#Question 3
# def std_res(math, sci, Eng):
#     percentage= ((math+sci+Eng)/300)*100
#     if percentage >= 90 and percentage <=100:
#         return 'A'
#     elif percentage >=80 and percentage <=89:
#         return 'B'
#     elif percentage >= 70 and percentage <=79:
#         return 'C'
#     elif percentage >= 60 and percentage <= 69:
#         return 'D'
#     else:
#         return 'F'

# m, s, e= map(int, input('Enter the marks: ').split())
# print(std_res(m,s,e))

#Question 4
# def even_odd(n):
#     if n % 2 ==0:
#         return 'Even'
#     else:
#         return 'Odd'
# num= int(input('Enter a number: '))
# print(even_odd(num))

#Question 5
# def leap_year(year):
#     if year % 400==0 or year % 4==0 and year % 100 !=0:
#         return f'{year} is leap year'
#     else:
#         return f'{year} is not a leap year'
# year=int(input('Enter a year: '))
# print(leap_year(year))

#Question 6
# def prime_num(n):
#     for i in range(2,int(n*0.5)+1):
#         if n % i == 0:
#             return 'Not prime'    
#         else:
#             return 'Prime'
# num= int(input('Enter a number: '))
# print(prime_num(num))

#Question 6
def prime_num(n):
 
    for i in range(2,int(n*0.5)+1):
        if n % i == 0:
            return 'Not prime'    
        else:
            return 'Prime'
           
def sum(limit):
    sum=0
    for i in range(2,limit+1):
        if prime_num(i):
            sum +=i
    return sum 
num= int(input('Enter a number: '))
print(sum(num))

 
