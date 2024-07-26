"""
    Author : Md. Nazim Uddin (Nakib)
    Date : 2024-07-26
    Solution to the problem: https://codeforces.com/contest/1996/problem/0
"""
t = int(input())
while t:
    t-=1
    n = int(input())
    count = n // 4
    r = n % 4
    if r > 0:
        count += r // 2
    print(count)
    count = 0
