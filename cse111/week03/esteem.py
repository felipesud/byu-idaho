# 06 Team Activity: Troubleshooting Functions
# From: https://byui-cse.github.io/cse111-course/lesson06/teach.html
# By: Felipe dos Santos Belisário

"""
As a team, write a Python program named esteem.py that implements the Rosenberg self-esteem scale. Your program must ask the user to respond to each of the ten statements with D, d, a, or A which mean strongly disagree, disagree, agree, and strongly agree. Your program must compute the score for each answer and sum and display the person's total score. You should think about how you will separate this program into functions before you begin writing the program.

Core Requirements
    1. Your program prints the introductory text as shown in the Testing Procedure section below.
    2. Your program prints each of the ten statements and gets a response from the user.
    3. Your program computes the score for each response and sums all the scores and displays the total score.

"""

def main():
    print('This program is an implementation of the Rosenberg Self-Esteem Scale. This program will show you ten statements that you could possibly apply to yourself. Please rate how much you agree with each of the statements by responding with one of these four letters:')
    print('\n D means you strongly disagree with the statement.')
    print('d means you disagree with the statement.')
    print('a means you agree with the statement.')
    print('A means you strongly agree with the statement.\n')

    print('I feel that I am a person of worth, at least on an equal plane with others.')
    first = input('Enter D, d, a, or A: ')

    print('I feel that I have a number of good qualities. ')
    second = input('Enter D, d, a, or A: ')

    print('All in all, I am inclined to feel that I am a failure. ')
    third = input('Enter D, d, a, or A: ')

    print('I am able to do things as well as most other people.')
    fourth = input('Enter D, d, a, or A: ')

    print('I feel I do not have much to be proud of.')
    fifth = input('Enter D, d, a, or A: ')

    print('I take a positive attitude toward myself.')
    sixth = input('Enter D, d, a, or A: ')

    print('On the whole, I am satisfied with myself.')
    seventh = input('Enter D, d, a, or A: ')

    print('I wish I could have more respect for myself.')
    eighth = input('Enter D, d, a, or A: ')

    print('I certainly feel useless at times.')
    nineth = input('Enter D, d, a, or A: ')

    print('At times I think I am no good at all.')
    tenth = input('Enter D, d, a, or A: ')

    positive = [first, second, fourth, sixth, seventh]
    negative = [third, fifth, eighth, nineth, tenth]

    print(f'Your score is {get_positive(positive) + get_negative(negative)}.')
    print('A score below 15 may indicate problematic low self-esteem.')

def get_positive(answers):
    score = 0
    for i in answers:
        if i == "D":
            score += 0
        if i == "d":
            score += 1
        if i == "a":
            score += 2
        if i == "A":
            score += 3
    return score

def get_negative(answers):
    score = 0
    for i in answers:
        if i == "D":
            score += 3
        if i == "d":
            score += 2
        if i == "a":
            score += 1
        if i == "A":
            score += 0
    return score

main()