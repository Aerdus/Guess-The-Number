import random
import sys


def main():
    score = 0
    round = 0
    while True:
        play_again = input("\nWould you like to play again? Yes/No? ").strip().lower()
        print("")
        if play_again == "no":
            print("\nScore:", score, "\nThanks for playing!")
            sys.exit(0)
        elif play_again == "yes":
            incorrect_guess = 0
            correct_ans = rand_num()
            while True:
                try:
                    if incorrect_guess == 3:
                        print("\nGame Over! \nScore:", score)
                        break
                    else:
                        user_input = int(input("Enter a number: "))
                        if input_check(user_input):
                            print(int_check(user_input, correct_ans))
                            print("Answer: ", correct_ans)
                            print("Score: ", score)
                            print("Round: ", round)
                            print("Incorrect Guess: ", incorrect_guess)
                            if int_check(user_input, correct_ans) == "Correct!":
                                incorrect_guess == 0
                                score += 1
                                round += 1
                                break
                            else:
                                incorrect_guess += 1
                                round += 1
                                score = 0
                        else:
                            print("Please enter a number between 1 and 10")
                            continue
                except ValueError:
                    print("Please enter a number")
        else:
            print("Please only enter Yes/No")        


def input_check(user_input):
    if user_input <= 0 or user_input >= 11:
        return False
    else:
        return True



def rand_num():
    return random.randint(1, 10)




def int_check(user_input, rand_num):
    if rand_num == user_input:
        return f"Correct!"
    elif rand_num > user_input:
        return f"Higher!"
    elif rand_num < user_input:
        return f"Lower!"
    else:
        return f"Incorrect!"


main()