import sys

from util import clear_terminal, is_correct
import view
from questions import questions


def all_questions():
    try:
        for question in questions:
            clear_terminal()
            view.print_question(question)
            answer = view.get_answer("\nPlease select your answer: ").upper()
            while answer not in ["A", "B", "C", "D"]:
                answer = view.get_answer("Pleas enter A, B, C or D: ").upper()

            if is_correct(answer, question):
                print("That is correct")
                _ = input("Press Enter to continue... ")
            else:
                print("That is not correct")
                print(f'The correct answer was {question[-1]}')
                _ = input("Press Enter to continue... ")
    except KeyboardInterrupt:
        clear_terminal()
        sys.exit("Program closed")

    clear_terminal()
    print("Congratulations, you finished all the questions!")
