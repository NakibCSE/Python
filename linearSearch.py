numbers = [3,234,432,21,3,4,12,54,3]
max_n = numbers[0]

for i in numbers:
    if i > max_n:
        max_n = i
print("The largest number is = ", max_n)


# sum of numbers that divisible by 5 only

result = 0
for num in range(101):
    if num%5 == 0:
        print(num)
        result += num
print("Sum is = ", result)


#simpler version of the previous one
result = 0
for num in range(5, 101, 5):
    result += num
print(result)