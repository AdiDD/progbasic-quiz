import sys
from util import clear_terminal
from view import start_screen, get_answer
from custom_quiz import custom_quiz
from basic_quiz import basic_quiz
from all_questions import all_questions


def main():
    try:
        start_screen()
        answer = get_answer("Make your choice: ")
        while answer not in ["1", "2", "3"]:
            answer = get_answer("Pleas enter 1, 2 or 3: ")
        if answer == "1":
            basic_quiz()
        elif answer == "3":
            all_questions()
        else:
            minutes = get_answer("How many minutes would you like? (max 5) ")
            while minutes not in ["1", "2", "3", "4", "5"]:
                minutes = get_answer("Please enter a number between 1 and 5: ")
            custom_quiz(int(minutes))
    except KeyboardInterrupt:
        clear_terminal()
        sys.exit("Program closed")


if __name__ == "__main__":
    main()
