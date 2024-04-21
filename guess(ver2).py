import random
import sys


def main():
    print(welcome())
    user_start()
    level = user_level()
    answer = rand_int(level)
    incorrect_attempts = 0
    score = 0
    loop = 0
    while True:
        if incorrect_attempts == 3:
            print("\nGame Over!")
            while True:
                play = play_again()
                if play == True:
                    main()
                if play == False:
                    print("\nYour score is:", score, "\nGoodbye!\n")
                    sys.exit(0)
        guess = user_guess(level)
        check_answer = check_ans(guess, answer)
        if check_answer == True:
            score += 1
            loop += 1
            incorrect_attempts = 0
            print("\nScore:", score)
            print("\nCorrect!")
            while True:
                play = play_again()
                if play == True:
                    main()
                if play == False:
                    print("\nYour score is:", score, "\nGoodbye!\n")
                    sys.exit(0)
        if check_answer == False:
            loop += 1
            incorrect_attempts += 1
            print("\nAttempt Number", incorrect_attempts)
            print("Incorrect!\nTry again!")
            

    
def welcome():
    return f"\n ---- Welcome to Guess The Int! ----\n You have three chances to guess the correct number!\n"


def start():
    while True:
        try:
            start = input("Shall we begin? Y/N? ").strip().lower()
            if start == "y":
                return True
            elif start == "n":
                return False
            else:
                raise ValueError("Please enter Y for yes or N for no")
        except ValueError as e:
            print(e)
    

def user_start():
    user_start = start()
    if user_start == True:
        print("Let's begin!")
    elif user_start == False:
        print("Goodbye!")
        sys.exit(0)


def user_level():
    print("\nChoose a difficulty level of 1, 2, or 3.")
    while True:
        try:
            usr_lvl = int(input("Level: "))
            if usr_lvl in (1,2,3):
                return usr_lvl
            else:
                raise ValueError
        except ValueError as e:
            print("\nPlease choose a number from 1, 2 or 3")
    

def rand_int(usr_lvl):
    if usr_lvl == 1:
        return random.randint(1, 5)
    if usr_lvl == 2:
        return random.randint(1, 10)
    if usr_lvl == 3:
        return random.randint(1, 20)
    

def user_guess(level):
        if level == 1:
            print("\nGuess a number between 1 and 5!")
            while True:
                try:
                    usr_guess = int(input("Input: "))
                    if usr_guess in range(1, 6):
                        return usr_guess
                    else:
                        raise ValueError
                except ValueError:
                    print("\nPlease only choose a number between 1 and 5")
        elif level == 2:
            print("\nGuess a number between 1 and 10!")
            while True:
                try:
                    usr_guess = int(input("Input: "))
                    if usr_guess in range(1, 11):
                        return usr_guess
                    else:  
                        raise ValueError
                except ValueError:
                    print("\nPlease only choose a number between 1 and 10")
        else:
            print("\nGuess a number between 1 and 20!")
            while True:
                try:
                    usr_guess = int(input("Input: "))
                    if usr_guess in range(1, 21):
                        return usr_guess
                    else:
                        raise ValueError
                except ValueError:
                    print("\nPlease only choose a number between 1 and 20")


def check_ans(guess, answer):
    if guess == answer:
        return True
    elif guess != answer:
        return False


def play_again():
    while True:
        try:
            play_again = input("\nWould you like to play again?\nEnter Y for yes or N for no\n\nInput:").strip().lower()
            if play_again == "y":
                return True
            elif play_again == "n":
                return False
            else:
                raise ValueError
        except ValueError:
            print("Please enter Y for yes or N for no")
        

main()