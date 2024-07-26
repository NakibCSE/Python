#Read the number of test case
t = int(input())

#Process each test case
for _ in range(t):

    #Read inpt string
    s = input()

    #Convert the input string to upper case and compare with YES
    if s.upper() == "YES":
        print("YES")
    else:
        print("NO")