import time
import random
import sys

from util import clear_terminal, convert_time, is_correct, is_in_time_limit
import view
from questions import questions


def basic_quiz():
    mistakes = 0
    questions_answered_correctly = 0
    TIME_LIMIT = 25 * 60  # 25 minutes
    START_TIME = time.time()
    try:
        while questions_answered_correctly < 26 and mistakes < 5 and is_in_time_limit(time.time() - START_TIME, TIME_LIMIT):
            question = random.choice(questions)
            questions.remove(question)
            clear_terminal()
            time_left = convert_time(time.time() - START_TIME, 20 * 60)
            view.print_stats(questions_answered_correctly, mistakes, time_left, 25)
            view.print_question(question)
            answer = view.get_answer("\nPlease select your answer: ").upper()
            while answer not in ["A", "B", "C", "D"]:
                answer = view.get_answer("Pleas enter A, B, C or D: ").upper()

            if is_correct(answer, question) and is_in_time_limit(time.time() - START_TIME, TIME_LIMIT):
                questions_answered_correctly += 1
            elif is_in_time_limit(time.time() - START_TIME, TIME_LIMIT):
                mistakes += 1
            else:
                break
    except KeyboardInterrupt:
        clear_terminal()
        sys.exit("Program closed")

    clear_terminal()
    if questions_answered_correctly > 20:
        view.print_finish_screen(questions_answered_correctly, True, 25)
    else:
        view.print_finish_screen(questions_answered_correctly, False, 25)
