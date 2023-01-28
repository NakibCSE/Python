def add_numbers(numbers):
    result = 0
    for number in numbers:
        result += number
    return result


summation = add_numbers([1,34,5,3,2,3,5,6])
print(summation)