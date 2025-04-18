
    # Create the question bank using dictionary.........
def run_quiz():
    questions = {  "What is the capital of France?": "paris",
        "Who wrote 'Romeo and Juliet'?": "shakespeare",
        "What is the chemical symbol for water?": "h2o",
        "How many continents are there on Earth?": "7",
        "What is the square root of 64?": "8"
                }

# Build the quiz logic....................
    score =  0
    user_answers = {}
    for question,correct_answer in questions.items():
        answer = input(question + " ")
        if answer.strip().lower() == correct_answer.lower():
             print("Correct!")
             score += 1
             user_answers[question] = "Correct"
        else:
            print("Wrong")
            user_answers[question] = "Incorrect"

# Grade the user...........
    if score == 5:
        grade = "A+"
    elif score == 4:
        grade = "A"
    elif score == 3:
        grade = "B"
    elif score == 2:
        grade = "C"
    elif score == 1 or score == 0:
        grade = "F"

    print(f"\n Your Score : {score}/5")
    print(f"\n Your Grade : {grade}")


#List of wrong questions...............
    wrong_questions = [q for q in questions if user_answers[q] == "Incorrect"]
    print("\n Questions you got wrong : ")
    for q in wrong_questions:
        print("-" , q)

    result_dict = {q : ("Correct" if user_answers[q] == "Correct" else "Incorrect") for q in questions}
    print("\n Questions wise result ")
    for q, res in result_dict.items():
        print(f"{q}:{res}")

# replaying.........
    # Create the question bank using dictionary.........
def run_quiz():
    questions = {  "What is the capital of France?": "paris",
        "Who wrote 'Romeo and Juliet'?": "shakespeare",
        "What is the chemical symbol for water?": "h2o",
        "How many continents are there on Earth?": "7",
        "What is the square root of 64?": "8"
                }

# Build the quiz logic....................
    score =  0
    user_answers = {}
    for question,correct_answer in questions.items():
        answer = input(question + " ")
        if answer.strip().lower() == correct_answer.lower():
             print("Correct!")
             score += 1
             user_answers[question] = "Correct"
        else:
            print("Wrong")
            user_answers[question] = "Incorrect"

# Grade the user...........
    if score == 5:
        grade = "A+"
    elif score == 4:
        grade = "A"
    elif score == 3:
        grade = "B"
    elif score == 2:
        grade = "C"
    elif score == 1 or score == 0:
        grade = "F"

    print(f"\n Your Score : {score}/5")
    print(f"\n Your Grade : {grade}")


#List of wrong questions...............
    wrong_questions = [q for q in questions if user_answers[q] == "Incorrect"]
    print("\n Questions you got wrong : ")
    for q in wrong_questions:
        print("-" , q)

    result_dict = {q : ("Correct" if user_answers[q] == "Correct" else "Incorrect") for q in questions}
    print("\n Questions wise result ")
    for q, res in result_dict.items():
        print(f"{q}:{res}")

# replaying.........
while True:
    run_quiz()
    replay = input("\n Do you want to play ? (yes or No)" )
    if replay.lower() != "yes":
        print("...Thanks for playing...")
        break
    
    