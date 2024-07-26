
# Problem link: https://codeforces.com/contest/1352/problem/A
#Read the number of test case
t = int(input())

#Process each test case
for _ in range(t):
    
    #Declare an empty list to hold the answers
    answer = []
    #Read input and process accordingly
    n = int(input())
    x = 1
    while n > 0:
        x = x * 10
        p = n % x
        if p > 0:
            answer.append(p)
        n = n -p
    print(len(answer))
    for ans in answer:
        print(ans, end=' ')
    print()
    
    

