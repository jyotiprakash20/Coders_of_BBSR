def leap_year(n):
    is_leapYear = False
    if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
        is_leapYear = True
    return is_leapYear
n = 2028
print(leap_year(n))