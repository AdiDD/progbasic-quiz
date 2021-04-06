def start_screen():
    print("Welcome to the progbasiz quiz!")
    print("If you want to take a basic quiz (25 questions in 25 minutes), press 1")
    print("If you want to set your own time limit with unlimited questions, press 2")


def print_question(question):
    print(question[0])
    print(question[1])
    print(question[2])
    print(question[3])
    print(question[4])


def print_stats(questions_answered, mistakes, time_left, limit=0):
    mm, ss = time_left
    if limit == 0:
        print(f"Questions answered correctly: {questions_answered}, Mistakes: {mistakes}, Time left: {mm} minutes and {ss} seconds")
    else:
        print(f"Questions answered correctly: {questions_answered}/{limit}, Mistakes: {mistakes}, Time left: {mm} minutes and {ss} seconds")
    print("\n--------------------------------------------------\n")


def print_finish_screen(questions_answered_correctly, passed=True, limit=0):
    if passed and limit > 0:
        print("Congratulations, you passed!")
        print(f"You answered {questions_answered_correctly} questions correctly out of {limit}.")
    elif not passed and limit > 0:
        print("You failed!")
        print(f"You answered {questions_answered_correctly} questions correctly out of {limit}.")
    else:
        print(f"You managed to answer {questions_answered_correctly} questions correctly in one minute.")


def get_answer(text):
    return input(text)
