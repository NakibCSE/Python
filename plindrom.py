str = input("Enter a string to check palindrom: ")
new_str = ""
ln = len(str)-1
while ln >= 0:
    new_str += str[ln]
    ln -= 1

if str == new_str:
    print(str, " is a palindrom.")
else:
    print(str, " is not a palindrom.")