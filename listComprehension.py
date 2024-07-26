#Normal code
li = [1,2,3,4,5,6,7,8,9,10]
evenNumber = []
for x in li:
    if x % 2 == 0:
        evenNumber.append(x)
print(evenNumber)

#Comprehensive version
evenNumbers = [x for x in range(1,11) if x % 2 == 0]
print(evenNumbers)