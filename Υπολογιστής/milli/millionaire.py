from questionslist import *
import random
import time
import colorama
from colorama import Fore, Style
import webbrowser

colorama.init(autoreset=True)

with open("milly.txt", "r") as f:
    try:
        print(Fore.BLUE + Style.BRIGHT + f.read())
        print("=" * 100)
    except FileNotFoundError as e:
        print(e)


def _helps_(help_list, answer, key):
    print("-" * 20)
    print("Welcome to the help-chapter!")
    print("-" * 20)
    if len(help_list) == 0:
        print("You have no remaining helps.I'm sorry")
        return 0, 0
    print("your available helps:")
    i = 1
    for elem in help_list:
        print(str(i) + "." + elem)
        i += 1
    choice = input("\nChoose the type of help you want to use for this question:").lower().strip()
    while choice != "50-50" and choice != "audience help" and choice != "phone":
        print("\nOops type the right help")
        choice = input("\nChoose the type of help do you want to use for this question:").lower().strip()

    if choice == "50-50":  # 50-50
        help_list.pop(0)
        if key == "A":
            number = 0
        elif key == "B":
            number = 1
        elif key == "C":
            number = 2
        else:
            number = 3
        number1 = random.randint(0, 3)
        while number1 == number:
            number1 = random.randint(0, 3)
        number2 = random.randint(0, 3)
        while number2 == number or number2 == number1:
            number2 = random.randint(0, 3)

        s1 = answer[number1]
        s2 = answer[number2]
        answer.remove(s1)
        answer.remove(s2)

        print("You have now only 2 choices! It's 50-50!")
        for elem in answer:
            print(f"+{28 * "-"}+")
            print(f"|{elem.strip().center(28)}|")
            print(f"+{28 * "-"}+")

        return 1, answer
    elif choice == "audience help":  # audience help
        help_list.remove("audience help")
        print("\nAudience voting", end="")
        for _ in range(3):
            print(".", end="")
            time.sleep(1)
        time.sleep(3)
        print(f"\n\nThe results go with:{key} with {random.uniform(50.00, 100.00):.3}%")
        return 2, 0
    elif choice == "phone":
        # phone help
        help_list.remove("phone")
        print("\n\nOk you have 35 seconds to take the phone-help that you want")
        input("press enter in order to start the countdown")
        for i in range(0, 35):
            print(str(i) + " ", end="")
            time.sleep(1)
        print("\nPut down you phone!The time passed!")
        return 3, 0


def main():
    helps_ = ["50-50", "audience help", "phone"]
    answer = input("\nDo you want the rules analytically?(yes/no):").lower()
    while answer != "yes" and answer != "no":
        print("you have to choose between yes or no")
        answer = input("\nDo you want the rules analytically?(yes/no):").lower()
    if answer == "yes":
        webbrowser.open("https://wwbm.com/rules")
        input("press enter to begin!")
    else:
        print("so let's get started!")
    i = 0
    bank = 0
    while True:
        try:
            # begin

            print(f"\nQuestion:{i + 1} for ${money_list[i]}!")
            input("\nAre you ready? then press enter!\n")
            print(list(questions_1)[i])
            key = list(questions_1)[i]
            answers = answers_1[i]
            for j in range(len(answers)):
                print(answers[j])
            # stop scenario
            if i > 1:
                remain = bank
                if bank < 1000:
                    remain /= 5
                else:
                    remain /= 100
                w = input(f"\n\nNow there are two choices: You stop and you leave with:${remain} "
                          f"or you continue and trust the process(type s for stop or just type anything else or press "
                          f"enter):").lower().strip()
                if w == "s":
                    print(f"\nok then! you chose to stop and and fill your bank account with:${remain} \n"
                          f"we are glad you played with us!")
                    break
            # check right answer
            input_choice = (input("Do you want to answer this or do you need help?(help/continue):")).lower().strip()
            while input_choice != "help" and input_choice != "continue":
                print("\nYou must choose between help (if you need help for this question) or continue(if you "
                      "know the answer)\n")
                input_choice = (input("Do you want to answer this or do you need help?(help/continue):")).lower().strip(
                )

            # help choice
            if input_choice == "help":
                choice, new = _helps_(help_list=helps_, answer=answers, key=questions_1[key])
                if choice == 1:
                    choice_ = input(f"Give me your choice please!:").strip()
                    while choice_ != "A" and choice_ != "B" and choice_ != "C" and choice_ != "D":
                        print("Wrong input!Try again")
                        choice_ = input(f"Give me your choice please!:").strip().upper()
                    right_answer = questions_1[key]
                    time.sleep(3)
                    # right answer
                    if right_answer == choice_:
                        i += 1
                        if i == 15:
                            print(Fore.RED)
                            print("\n\nWOH YOU JUST WON THE GAME AND 1.000.000$!")
                            print("\033[39m")
                            break

                        print(f"\nCongratulations, you just won ${money_list[i - 1]} with the help of 50-50")
                        bank = money_list[i]
                        print("-" * 20)

                        continue
                    else:
                        print(f"\nWrong answer, the right answer was:{right_answer}. I'm sorry")
                        # how much he/she takes home
                        if bank == 0 or bank < 300:
                            print("You are not ready for this game")
                        else:
                            if bank < 1000:
                                print(f"You go home with ${bank / 3}")
                            else:
                                print(f"You go home with ${bank / 10}")
                        break
                else:
                    players_answer = input("Give me your final answer(A,B,C,D) using your help:").strip().upper()
                    while (players_answer != "A" and players_answer != "B" and players_answer != "C" and players_answer
                           != "D"):
                        print("\nWrong input, please choose between A or B or C or D\n")
                        players_answer = input("Give me your final answer(A,B,C,D):").upper().strip()
                    time.sleep(3)
                    # continue the procedure
                    right_answer = questions_1[key]
                    # right answer
                    if right_answer == players_answer:
                        i += 1
                        if i == 15:
                            print(Fore.RED)
                            print("\n\nWOH YOU JUST WON THE GAME AND 1.000.000$!")
                            print("\033[39m")
                            break

                        print(f"\nCongratulations, you just won ${money_list[i - 1]}")
                        bank = money_list[i]
                        print("-" * 20)
                        continue
                    # wrong answer
                    else:
                        print(f"\nWrong answer, the right answer was:{right_answer}. I'm sorry")
                        # how much he/she takes home
                        if bank == 0 or bank < 300:
                            print("You are not ready for this game")
                        else:
                            if bank < 1000:
                                print(f"You go home with ${bank / 3}")
                            else:
                                print(f"You go home with ${bank / 10}")

                        break

            else:  # he/she knows the answer
                # check right input A,B,C,D
                players_answer = input("Give me your final answer(A,B,C,D):").upper()
                while (players_answer != "A" and players_answer != "B" and players_answer != "C" and players_answer !=
                       "D"):
                    print("\nWrong input, please choose between A or B or C or D\n")
                    players_answer = input("Give me your final answer(A,B,C,D):").upper()
                time.sleep(3)
                # continue the procedure
                right_answer = questions_1[key]
                # right answer
                if right_answer == players_answer:
                    i += 1
                    if i == 15:
                        print(Fore.RED)
                        print("\n\nWOH YOU JUST WON THE GAME AND 1.000.000$!")
                        print("\033[39m")
                        break
                    print(f"\nCongratulations, you just won ${money_list[i - 1]}")
                    bank = money_list[i]
                    print("-" * 20)

                    continue
                # wrong answer
                else:
                    print(f"\nWrong answer, the right answer was:{right_answer}. I'm sorry")
                    # how much he/she takes home
                    if bank == 0 or bank < 300:
                        print("You are not ready for this game")
                    else:
                        if bank < 1000:
                            print(f"You go home with ${bank / 3}")
                        else:
                            print(f"You go home with ${bank / 10}")

                    break
        except IndexError as error:
            print("oops I'm sorry , something went wrong")
            print(error)
        except Exception as error:
            print(f"bug was detected:{error}")


if __name__ == "__main__":
    main()
