str = input("Enter a string to swap the consecuitve character: ")
new_string = ""
for i in range(0, len(str), 2):
    if i == len(str)-1:
        break
    new_string+=str[i+1]
    new_string+=str[i]
print(new_string)