import os
from view import print_color


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_color('''______               ______           _            _____       _     
| ___ \              | ___ \         (_)          |  _  |     (_)    
| |_/ / __ ___   __ _| |_/ / __ _ ___ _  ___ ___  | | | |_   _ _ ____
|  __/ '__/ _ \ / _` | ___ \/ _` / __| |/ __/ __| | | | | | | | |_  /
| |  | | | (_) | (_| | |_/ / (_| \__ \ | (__\__ \ \ \/' / |_| | |/ / 
\_|  |_|  \___/ \__, \____/ \__,_|___/_|\___|___/  \_/\_\\__,_|_/___|
                 __/ |                                               
                |___/
''', 'random')


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


def is_in_time_limit(time_passed, time_limit):
    return time_passed < time_limit
