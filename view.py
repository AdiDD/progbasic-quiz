import random


def print_color(string, color="w", linked=0, style="reset"):
    lightcolors = ["dgrey", "lr", "lg", "ly", "lb", "lm", "lc", "w"]
    colors = ["bk", "r", "g", "y", "b", "m", "c", "lgrey"]
    styles = ["reset", "bold", "dim","italic", "underline", "blink", "blink2", "reverse", "hidden", "crossout"]
    if color in lightcolors:
        num = lightcolors.index(color)
        c = "9"
    elif color in colors:
        num = colors.index(color)
        c = "3"
    elif color == "random":
        num = random.randrange(1, 6)
        c = random.choice(["3", "9"])
    else:
        num = 7
        c = "9"
    if style in styles:
        s = styles.index(style)
    elif style == "random":
        s = random.randrange(9)
    else:
        s = "10"
    if linked == "link":
        print(f'\033[{c + str(num)}m{string}\033[{s}m', end='')
    else:
        print(f'\033[{c + str(num)}m{string}\033[{s}m')


def start_screen():
    print_color("Welcome to the progbasiz quiz!", 'random')
    print_color("If you want to take a basic quiz (25 questions in 25 minutes), press 1", 'random')
    print_color("If you want to set your own time limit with unlimited questions, press 2", 'random')
    print_color("If you want to go through all the questions at your own pace, press 3", 'random')


def print_question(question):
    print_color(question[0], 'random')
    print_color(question[1], 'random')
    print_color(question[2], 'random')
    print_color(question[3], 'random')
    print_color(question[4], 'random')


def print_stats(questions_answered, mistakes, time_left, limit=0):
    mm, ss = time_left
    if limit == 0:
        print_color(f"Questions answered correctly: {questions_answered}, Mistakes: {mistakes}, Time left: {mm} minutes and {ss} seconds", 'random')
    else:
        print_color(f"Questions answered correctly: {questions_answered}/{limit}, Mistakes: {mistakes}, Time left: {mm} minutes and {ss} seconds", 'random')
    print_color("\n--------------------------------------------------\n", 'random')


def print_finish_screen(questions_answered_correctly, passed=True, limit=0):
    if passed and limit == 25 :
        print_color("Congratulations, you passed!", 'random')
        print_color(f"You answered {questions_answered_correctly} questions correctly out of {limit}.", 'random')
    elif not passed and limit == 25:
        print_color("You failed!", 'random')
        print_color(f"You answered {questions_answered_correctly} questions correctly out of {limit}.", 'random')
    elif limit == 1:
        print_color(f"You managed to answer {questions_answered_correctly} questions correctly in one minute.", 'random')
    else:
        print_color(f"You managed to answer {questions_answered_correctly} questions correctly in {limit} minutes.", 'random')


def get_answer(text):
    return input(f'\n{text}')
