#Read the number of test case
n = int(input())
#Process each test case 
for _ in range(n):
    answer = ''
    s,t = input().split()
    if len(s) > len(t):
        for i in range(len(t)):
            answer += s[i] + t[i]
        answer = answer + s[len(t):]
    elif len(t) > len(s):
        for i in range(len(s)):
            answer += s[i] + t[i]
        answer = answer + t[len(s):]
    else:
        for i in range(len(s)):
            answer += s[i] + t[i]
    print(answer)
