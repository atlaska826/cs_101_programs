"""
Name: Atlas Mallams
Class Section: 0018
Program 3 Algorithm
Creation Date: October 3, 2023
Due Date: October 15, 2023
"""
import random


"""VARIABLES AND FUNCTIONS"""
correct_count = 0

questions = [
    {'question': 'Which app has the most total users?',
     'options': ['a) Tiktok', 'b) Snapchat', 'c) Instagram', 'd) Facebook'],
     'correct_answer': 3},

    {'question': 'What programming language is this game written in?',
     'options': ['a) Java', 'b) Python', 'c) C++', 'd) Ruby'],
     'correct_answer': 1},

    {'question': 'What number was the Apollo mission that successfully put a man on the moon for the first time in '
                 'human history?',
     'options': ['a) Apollo 11', 'b) Apollo 12', 'c) Apollo 13', 'd) Apollo 14'],
     'correct_answer': 0}]


def randomize_questions():
    """Returns order, a list of unique random numbers between 0 and 2 (inclusive)"""
    order = []

    for i in range(3):
        num = random.randint(0, 2)
        while num in order:
            num = random.randint(0, 2)
        order.append(num)
    return order


def ask_question(question_num, index):
    """Handles all the question output and conditional logic for answering"""
    accepted_answers = ['a', 'b', 'c', 'd']
    question = questions[index]

    # Prints the question and the question number
    print(f'Question {question_num}: {question["question"]}')
    for option in question['options']:
        print(option)

    # Asks the user for their answer and handles invalid answers
    user_answer = input('Enter your answer (a, b, c, d): ').lower()
    while user_answer not in accepted_answers:
        print('Invalid answer choice. Please try again.\n')
        user_answer = input('Enter your answer (a, b, c, d): ').lower()

    # Checks if user_answer is correct or incorrect
    if accepted_answers.index(user_answer) == question['correct_answer']:
        print('Correct!\n')
        return True
    else:
        print('Incorrect.\n')
        return False


def play_again():
    """Returns the truth value dependent on whether the user wishes to play again"""
    quiz_again = input('Do you want to play again? (yes/no): ').lower()

    # Continues to ask the user until 'yes' or 'no' is entered
    while quiz_again != 'yes' and quiz_again != 'no':
        print('Invalid response. Please try again.\n')
        quiz_again = input('Do you want to play again? (yes/no): ').lower()

    # Returns the truth value
    if quiz_again == 'yes':
        return True
    else:
        return False


"""MAIN CODE"""


print('Welcome to the Quiz Game!\n')

while True:  # Loop runs until terminated by break
    question_order = randomize_questions()
    question_count = 1

    # Iterates through question_order to ask question in a random order
    for i in question_order:
        if ask_question(question_count, i):
            correct_count += 1
        question_count += 1

    # Outputs the user's score as a percentage
    print(f'You got {correct_count}/3 questions correct ({(correct_count / 3) * 100:2.1f}%).\n')

    # Asks the user whether they would like to play again
    if not play_again():
        break
    correct_count = 0
    print()

print('Thank you for playing the Quiz Game. Goodbye!')