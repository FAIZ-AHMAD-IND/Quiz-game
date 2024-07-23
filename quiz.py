print("***---welcome to quiz game---***\n")
print("********************************\n")
def my_questions():
    return [
        {"question": "Q 1. Who is father of computer?", "alternatives": ["A. Albert Einstein", "B. Blaise Pascal", "C. Larry Page", "D. Charles Babbage"], "answer": "D"},
        {"question": "Q 2. Which of the following is not a programming language ?", "alternatives": ["A. JAVA", "B. Firefox", "C. C++", "D. Python"], "answer": "B"},
        {"question": "Q 3. What is the formula of water?", "alternatives": ["A. CH4", "B. H2O", "C. D2O", "D. NaCl"], "answer": "B"}
    ]

def ask_question(question):
    print(question["question"])
    for option in question["alternatives"]:
        print(option)
    answer = input("Your answer: ")
    if answer.upper() == question["answer"]:
        return True
    else:
        print(f"Wrong! The correct answer is option {question['answer']}")
        return False

def quiz_game():
    questions = my_questions()
    score = 0

    for question in questions:
        if ask_question(question):
            print("Correct!")
            score += 1

    print(f"Your final score is {score}/{len(questions)}")


quiz_game()