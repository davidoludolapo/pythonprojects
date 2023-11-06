# Create a dictionary that will store questions and answers
# Create a variable that tracks the score of the student
# Lopp through the dictionary using the key value pairs
# Display each question to the user and allow them to answer
# Display if they are right or wrong
# Show final result when quiz is completed

quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "what is the capital of Germany?",
        "answer": "Berlin"
    },
    "question3": {
        "question": "what is the capital of Nigeria?",
        "answer": "Abuja"
    },
    "question4": {
        "question": "what is the capital of America?",
        "answer": "Washington"
    },
    "question5": {
        "question": "what is the capital of England?",
        "answer": "London"
    },
}

score = 0

for key, value in quiz.items():
    print(value["question"])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print("Correct!")
        score = score+1
        if score == 1:
            print("Your score: " + str(score) + " point")
            print("")
            print("")
        else: 
            print("Your score: " + str(score) + " points")
            print("")
            print("")
    
    else:
        print("Wrong")
        print("The answer is : " + value['answer'])
        print("Your score: " + str(score) + " points")
        print("")
        print("")

print("You scored " + str(score) + " out of 5 questions correctly")
print("Your percentage is " + str(int(score/5 * 100)) + "%")
