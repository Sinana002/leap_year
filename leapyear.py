#if is_leap_year(year)==True: SAME AS if is_leap_year(year)
if is_leap_year(year)==True:def is_leap_year(year):
    if year%4 == 0:
        if year%100 ==0:
            if year%400 ==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
year=int(input("enter the year:"))
if is_leap_year(year)==True:
    print(f"year {year} is leap year")
else:
    print(f"year {year} is not a leap year")


