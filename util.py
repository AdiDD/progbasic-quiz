import os


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def is_correct(answer, question):
    return answer == question[-1]


def convert_time(time_passed, time_limit):
    if time_limit > 60:
        mm = int(time_limit - time_passed) // 60
        ss = int(time_limit - time_passed) % 60
    else:
        mm = 0
        ss = time_limit - time_passed % 60
    return int(mm), int(ss)
