result = 0
for i in range(50):
    result = result+1
print(result)


# using _ instead of i in loop structure
result = 0
for _ in range(50):
    result = result + 1
print(result)

# sum of the series 1 + 2 + 3 + ... n using for loop
result = 0
num = 1
for _ in range(50):
    result = result + num
    num = num + 1
print(result)

# sum of the series 1 + 2 + 3 + ... n using for loop Version 2
result = 0
for num in range(51):
    result = result + num
print(result)

# custom range in for loop 

result = 0
for num in range(1, 51):
    result = result + num
print(result)

# custom range and custom increment in for loop
result = 0
for num in range(1, 50 , 5):
    print(num)