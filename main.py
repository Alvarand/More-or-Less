import random


def check_num(check):
    return 1 <= check <= 100


def print_guess():
    print('Guess the number: ', end='')


def more_or_less(num, orig):
    if num > orig:
        print('Your number is more than my number')
        print("Let's try again")
        return False
    elif num < orig:
        print('Your number is less than my number')
        print("Let's try again")
        return False
    else:
        print('My congratulations, you guessed the number')
        return True


print('Welcome to the game MoL.')
original = random.randint(1, 100)  # original number

while True:
    print_guess()
    guess = int(input())  # guessing number
    if check_num(guess):
        if more_or_less(guess, original):
            break
    else:
        print("This number ain't in range 1-100")
        print("Let's try again")
