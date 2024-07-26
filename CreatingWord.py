#Problem link : https://codeforces.com/problemset/problem/1985/A

# Read the number of test cases
t = int(input())

#Process each test case
for i in range(t):
    #Read two string a and b
    a , b = input().split()

    #Swap the first character of a an b
    new_a = b[0] + a[1:]
    new_b = a[0] + b[1:]

    #Print the new strings
    print(new_a, new_b)