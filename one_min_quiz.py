import time
import random
import sys

import util
import view
from questions import questions


def one_min_quiz():
    mistakes = 0
    questions_answered_correctly = 0
    TIME_LIMIT = 1 * 60  # 1 minute
    START_TIME = time.time()
    try:
        while time.time() - START_TIME < TIME_LIMIT:
            question = random.choice(questions)
            questions.remove(question)
            util.clear_terminal()
            time_left = util.convert_time(time.time() - START_TIME, 1 * 60)
            view.print_stats(questions_answered_correctly, mistakes, time_left, 0)
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
    except IndexError:
        util.clear_terminal()
        sys.exit(f"You managed to answer {questions_answered_correctly} questions correctly in {60 - time_left[1]} seconds!")

    util.clear_terminal()
    view.print_finish_screen(questions_answered_correctly, mistakes)
