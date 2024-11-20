# Guess the Number Game
import colorama
from colorama import Fore, Style
import random

colorama.init()

attempts = 0
notcorrect = False
number = random.randint(1, 100)

while not notcorrect:
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "\nI Have Selected a Number Between 1 and 100! Can You Guess it?" + Style.RESET_ALL)
    guessed = input(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "> " + Style.RESET_ALL)

    if int(guessed) == number:
        print(Fore.GREEN + Style.BRIGHT + "Nice! You Did it After " + str(attempts) + " Attempt(s)!" + Style.RESET_ALL)
        break
    else:
        print(Fore.RED + Style.BRIGHT + "Wrong! Try Again!" + Style.RESET_ALL)
        attempts = attempts + 1

exit(number)
