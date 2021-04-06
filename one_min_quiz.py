import time
import random

import util
import view
from questions import questions


def one_min_quiz():
    mistakes = 0
    questions_answered_correctly = 0
    TIME_LIMIT = 60  # 1 minute
    START_TIME = time.time()

    while time.time() - START_TIME < TIME_LIMIT:
        question = random.choice(questions)
        questions.remove(question)
        util.clear_terminal()
        view.print_stats(questions_answered_correctly, mistakes)
        view.print_question(question)
        answer = view.get_answer("Please select your answer: ").upper()
        while answer not in ["A", "B", "C", "D"]:
            answer = view.get_answer("Pleas enter A, B, C or D: ").upper()

        if util.is_correct(answer, question) and time.time() - START_TIME < TIME_LIMIT:
            questions_answered_correctly += 1
        elif time.time() - START_TIME < TIME_LIMIT:
            mistakes += 1
        else:
            break

    util.clear_terminal()
    view.print_finish_screen(questions_answered_correctly, mistakes)
