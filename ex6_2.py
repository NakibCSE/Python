str = input("Please enter a string: ")
Iterator = 0
str_len = len(str)
new_str = ""
while Iterator < str_len-1:
    new_str+=str[Iterator+1]
    new_str+=str[Iterator]
    Iterator+=2
    
print(new_str)

    