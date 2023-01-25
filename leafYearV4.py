Year = int(input("Enter a year to check leaf year: "))
if Year%100 != 0 and Year%4 == 0:
    print(Year," is a leaf year.")
elif Year%100 == 0 and Year%400 == 400:
    print(Year," is a leaf year.")
else:
    print(Year," is not a leaf year.")
