from sys import exit
import random

result = []

def build_list(x):
    for i in range(x+1):
        if i == 0:
            pass
        else:
            result.append(i)
    return result

build_list(100000)
answer = random.randint(1, result[-1])


def guessing():
    guess_min = 1
    guess_max = 100000
    guess = 0
    while int(guess) != int(answer):
        print("Guess between " + str(guess_min) + " and " + str(guess_max) + ":")
        guess = input()
        if int(guess) > answer:
            guess_max = guess
            print("Too high, try again")
        elif int(guess) < answer:
            guess_min = guess
            print("Too low, try again")
        else:
            print( str(guess) + " is Correct!")

guessing()
