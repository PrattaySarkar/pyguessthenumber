import random
from colorama import Fore, Back, Style, init

init(autoreset=True)

def user_input_or_guess_the_number(debug_mode=False):
    print(Fore.RED + "Oh hi! It's a number game! Choose a number!")
    print(Fore.BLUE + "Guess a number while I GENERATE the random NUMBER! It should be 1-100.")

    random_generated_number = random.randint(1, 100)

    if debug_mode:
        print(Fore.MAGENTA + Style.BRIGHT + f"[DEBUG MODE] Generated number: {random_generated_number}")

    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess or get out from here: "))
            attempts += 1

            if guess < random_generated_number:
                print(Fore.RED + "Too LOW!")

            elif guess > random_generated_number:
                print(Fore.RED + "Too HIGH!")

            else:
                print(Fore.GREEN + f"Congratulations! You successfully guessed my generated number in {attempts} attempts...")
                print(Fore.RED + Style.BRIGHT +
                      "NOW ALL YOU HAVE TO DO IS!!!! GET THE **** OUT OF HERE!!!")
                input(Fore.YELLOW + "Press Enter to exit and CRASH the program!")
                exit("Program crashed on demand.")
        except ValueError:
            print(Fore.RED + "HEY, THAT'S AN INVALID NUMBER! YOU'RE MAKING ME ANGRY!!")

user_input_or_guess_the_number(debug_mode=False)
