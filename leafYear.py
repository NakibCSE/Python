Year = int(input("Enter a year to test leaf year: "))
if Year%4 == 0:
    if Year%100 == 0:
        if Year % 400 == 0:
            print(Year," is a leaf year")
        else:
            print(Year," is not a leaf year")
    else:
        print(Year," is a leaf year.")
else:
    print(Year," is not a leaf year.")