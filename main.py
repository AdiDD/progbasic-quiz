from view import start_screen, get_answer
from one_min_quiz import one_min_quiz
from basic_quiz import basic_quiz


def main():
    start_screen()
    answer = get_answer("Make your choice: ")
    while answer not in ["1", "2"]:
        answer = get_answer("Pleas enter 1 or 2: ")
    if answer == "1":
        basic_quiz()
    else:
        one_min_quiz()


if __name__ == "__main__":
    main()
