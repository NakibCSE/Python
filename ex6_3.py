str = input("Enter a string: ")
new_str = ""
str_len = len(str)
iterator = str_len -1
while iterator >= 0:
    new_str+=str[iterator]
    iterator-=1
if str == new_str:
    print(str," is a palindrome")
else:
    print(str," is not a palindrome")
