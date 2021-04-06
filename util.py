import os


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def is_correct(answer, question):
    return answer == question[-1]
