import time
import random
import sys

from util import clear_terminal, convert_time, is_correct, is_in_time_limit
import view
from questions import questions


def custom_quiz(minutes):
    mistakes = 0
    questions_answered_correctly = 0
    TIME_LIMIT = minutes * 60
    START_TIME = time.time()
    try:
        while is_in_time_limit(time.time() - START_TIME, TIME_LIMIT):
            question = random.choice(questions)
            questions.remove(question)
            clear_terminal()
            time_left = convert_time(time.time() - START_TIME, minutes * 60)
            view.print_stats(questions_answered_correctly, mistakes, time_left, 0)
            view.print_question(question)
            answer = view.get_answer("Please select your answer: ").upper()
            while answer not in ["A", "B", "C", "D"]:
                answer = view.get_answer("Pleas enter A, B, C or D: ").upper()

            if is_correct(answer, question) and is_in_time_limit(time.time() - START_TIME, TIME_LIMIT):
                questions_answered_correctly += 1
            elif is_in_time_limit(time.time() - START_TIME, TIME_LIMIT):
                mistakes += 1
            else:
                break
    except IndexError:
        clear_terminal()
        sys.exit(f"You managed to answer {questions_answered_correctly} questions correctly!")
    except KeyboardInterrupt:
        clear_terminal()
        sys.exit("Program closed")

    clear_terminal()
    view.print_finish_screen(questions_answered_correctly, mistakes)
