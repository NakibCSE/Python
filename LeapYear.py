"""""
Check leap year version 1
"""""
year1 = int(input("Enter a year to check leap year: ")) 
if year1 % 4 == 0:
    if year1 % 100 == 0:
        if year1 % 400 == 0:
            print(year1, "is a leap year")
        else:
            print(year1," is not a leap year")
    else:
        print(year1," is a leap year")
else:
    print(year1,"is not a leap yaer")


"""""
Check leap year version 2
"""""
year2 = int(input("Enter a year to check leap yaer"))
if year2 % 4 != 0:
    print(year2, "is not a leap year")
else:
    if year2 % 100 != 0:
        print(year2," is a leap year")
    else:
        if year2 % 400 != 0:
            print(year2," is not a leap year")
        else:
            print(year2," is a leap year")

"""""
Check leap year version 3
"""""
year = int(input("Enter a year: "))
if year % 100 != 0 and year % 4 == 0:
    print(year," is a leap year")
elif year % 100 == 0 and year % 400 == 0:
    print(year, " is a leap year")
else:
    print(year," is not a leap year")