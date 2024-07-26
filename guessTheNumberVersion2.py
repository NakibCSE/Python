import random

number = random.randint(1, 1000)
attempts = 0
low = 1
high = 1000
while True:
    print("Guess the number (between 1 and 1000): ")
    input_number = (high + low) // 2    #Only integer division
    print("My guess is ", input_number)
    attempts += 1
    if input_number == number:
        print("Your guess number is correct!")
        break
    if input_number > number:
        print("Your guess is incorrect! Please try to guess a smaller number!")
        high = input_number - 1
    else:
        print("Your guess is incorrect! Please try to guess a larger number!")
        low = input_number + 1
print("You tried ", attempts, " times to guess the correct number")