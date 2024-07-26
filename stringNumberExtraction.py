str = input("Enter a string to extract the required :")
upCase = ""
loCase = ""
digit = ""
others = ""
for cr in str:
    if cr >= "A" and cr <= "Z":
        upCase+=cr
    elif cr >= 'a' and cr <= 'z':
        loCase+=cr
    elif cr >= '0' and cr <= '9':
        digit+=cr
    else:
        others+=cr
print(upCase)
print(loCase)
print(digit)
print(others)

