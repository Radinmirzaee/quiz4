def new_game():

    guesses = []
    question_num = 1
    correct_answer = 0

    for key in questions:
        print(key)
        guess = input("A, B, C, or D?: ").upper()
        guesses.append(guess)
        correct_answer += check_answer(questions.get(key),guess)
        question_num += 1

    print(correct_answer)

# ----------------------------------------------------------------
def check_answer(answer,guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0
def display_score():
    pass
def play_again():
    pass

questions = {"How many elements are in the periodic table?: ": "C",
             "Which animal lays the largest eggs?: ": "D",
             "What is the most abundant gas in Earth's atmosphere?: ": "A",
             "How many bones are in the human body?: ": "A",
             "Which planet in the solar system is the hottest?: ": "B"
             }

options = [["A. 116", "B. 117", "C. 118", "D. 119"],
           ["A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"],
           ["A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"],
           ["A. 206", "B. 207", "C. 208", "D. 209"],
           ["A. Mercury", "B. Venus", "C. Earth", "D. Mars"]]


new_game()