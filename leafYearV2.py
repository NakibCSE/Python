Year = int(input("Enter a year to check leaf year: "))
if Year % 4 != 0:
    print(Year," is not a leaf year")
else:
    if Year % 100 != 0:
        print(Year," is a leaf Year")
    else:
        if Year%400 != 0 :
            print(Year," is not a leaf year")
        else:
            print(Year," is a leaf year")