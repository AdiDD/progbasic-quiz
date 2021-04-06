import time
import random

import util
import view
from questions import questions


def basic_quiz():
    mistakes = 0
    questions_answered_correctly = 0
    TIME_LIMIT = 25 * 60  # 25 minutes
    START_TIME = time.time()

    while questions_answered_correctly < 26 and mistakes < 5 and time.time() - START_TIME < TIME_LIMIT:
        question = random.choice(questions)
        questions.remove(question)
        util.clear_terminal()
        view.print_stats(questions_answered_correctly, mistakes, 2)
        view.print_question(question)
        answer = view.get_answer("Please select your answer: ").upper()
        while answer not in ["A", "B", "C", "D"]:
            answer = view.get_answer("Pleas enter A, B, C or D: ").upper()

        if answer == question[-1] and time.time() - START_TIME < TIME_LIMIT:
            questions_answered_correctly += 1
        elif time.time() - START_TIME < TIME_LIMIT:
            questions_answered_correctly += 1
            mistakes += 1
        else:
            break

    util.clear_terminal()
    if questions_answered_correctly > 20:
        view.print_stats(questions_answered_correctly, mistakes, True, 25)
    else:
        view.print_stats(questions_answered_correctly, mistakes, False, 25)
