from art import logo, vs
from game_data import data
from random import randint
from replit import clear


def print_score(score):
    if score > 0:
        print(f"You're right! Current score: {score}")
    return


def get_answer(count1, count2):
    if count1 > count2:
        correct = 'A'
    else:
        correct = 'B'
    print(f"Psssshhh Correct answer is {correct}")
    return correct


def show_choices(first, used, prev=0):

    if first:
        number1 = randint(0, len(data) - 1)
        while number1 in used:
            number1 = randint(0, len(data) - 1)
        used.add(number1)
    else:
        number1 = prev

    number2 = randint(0, len(data) - 1)
    while number2 in used:
        number2 = randint(0, len(data) - 1)
    used.add(number2)

    name = 'name'
    description = 'description'
    country = 'country'
    follower_count = 'follower_count'

    print(
        f"Compare A : {data[number1][name]}, a {data[number1][description]}, from {data[number1][country]}."
    )
    count1 = data[number1][follower_count]

    print(vs)
    print()

    print(
        f"Compare B : {data[number2][name]}, a {data[number2][description]}, from {data[number2][country]}.\n"
    )
    count2 = data[number2][follower_count]
    answer = get_answer(count1, count2)
    return answer, number2


def main():
    flag = True
    first = True
    score = 0
    prev = 0
    used = set()

    while flag:
        clear()
        print(logo)
        print_score(score)
        correct, prev = show_choices(first, used, prev)
        answer = input("Who has more followers? Type 'A' or 'B' : ")

        if answer == correct:
            score += 1
            first = False
        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            flag = False


main()
