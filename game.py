import random


def check_number():
    correct_number_correct_position = 0
    correct_number_wrong_position = 0
    for m, n in zip(number, guessed_num):  # zip to change the lists into a list of tuples
        if m == n:
            print("Match")
            correct_number_correct_position = 1
            break
    if correct_number_correct_position != 1:
        for x in guessed_num:
            if x in number:
                print("Close")
                correct_number_wrong_position = 1
                break
    if (correct_number_wrong_position != 1) and (correct_number_correct_position != 1):  #execute if both the above have failed
        print("Nope")


digits = list(range(10))
random.shuffle(digits)
number = digits[:3]

while True:
    guess = input("What is your guess? ")
    guess = list(guess)  # co
    num = map(lambda x: int(x), guess)  # hepls convert the list of strings into a list of integers
    guessed_num = list(num)
    check_number()
    if guess == number:
        break
