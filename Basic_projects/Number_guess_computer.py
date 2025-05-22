import random

user_num = int(input("Enter a number to guess (between 10 and 30): "))
low = 10
high = 30
chance = 1

while True:
    computer_guess = random.randint(low, high)
    print(f'Computer choice: {computer_guess}')
    
    if user_num > computer_guess:
        print('Too low, try again!')
        low = computer_guess + 1
    elif user_num < computer_guess:
        print('Too high, try again!')
        high = computer_guess - 1
    else:
        print(f'You guessed it at the {chance}th try!')
        break

    chance += 1