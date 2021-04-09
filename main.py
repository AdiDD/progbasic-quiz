import sys
from util import clear_terminal
from view import start_screen, get_answer, print_color
from custom_quiz import custom_quiz
from basic_quiz import basic_quiz
from all_questions import all_questions


def main():
    clear_terminal()
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
            minutes = get_answer("How many minutes would you like? (max 25) ")
            while minutes not in [str(x) for x in range(26)]:
                minutes = get_answer("Please enter a time limit, up to 25 minutes: ")
            custom_quiz(int(minutes))
    except KeyboardInterrupt:
        clear_terminal()
        sys.exit("Program closed")


if __name__ == "__main__":
    main()
