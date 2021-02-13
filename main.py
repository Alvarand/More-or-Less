import random


def check_num(num):
    return 1 <= num <= 100


def print_guess():
    print('Guess the number: ', end='')


print('Welcome to the game MoL.')
print_guess()
num = int(input())

if check_num(num):
    pass
else:
    print("This number ain't in range 1-100")

