Problem link: https://codeforces.com/problemset/problem/1976/A
#Read the number of test case
t = int(input())

#Process each test case
for i in range(t):
    #Read the length of the password
    n = int(input())

    #Read the password
    password = input()

    #Check if password contains only lower case or digit
    valid = all(('a' <= char <= 'z' or '0' <= char <= '9') for char in password)
    if not valid:
        print("NO")
        continue

    #Sort the password
    sorted_passsword = ''.join(sorted(password))
    
    #Check sorted password match the original password
    if sorted_passsword == password:
        print("YES")
    else:
        print("NO")