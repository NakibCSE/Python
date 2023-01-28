str = input("Enter a string: ")
small_letter = ""
capital_letter = ""
digit = ""
others = ""
for c in str:
    if c>= 'A' and c<= 'Z':
        capital_letter+=c
    elif c>= 'a' and c<='z':
        small_letter+=c
    elif c>= '0' and c<='9':
        digit+=c
    else:
        others+=c
print(capital_letter)
print(small_letter)
print(digit)
print(others)