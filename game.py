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
    if (correct_number_wrong_position != 1) and (
            correct_number_correct_position != 1):  # execute if both the above have failed
        print("Nope")


digits = list(range(10))
random.shuffle(digits)
number = digits[:3]


def game():
    global guessed_num
    while True:
        try:
            guess = input("Please enter a 3-digit guess: ")
            if len(guess) > 3:
                print("You entered more than 3 characters")
                continue
            guess = list(guess)  # convert string into a list
            num = map(lambda x: int(x), guess)  # helps convert the list of strings into a list of integers
            guessed_num = list(num)
        except ValueError:
            print("Please enter a number")
            continue

        check_number()
        if guess == number:
            print("You got it !!!\n The number ")
            break
    play_again = input("Wud you like to play again? Y/N")
    if play_again.upper() == Y:
        print("Game loading........")
        game()
    elif play_again.upper() == N:
        print("Thanks for playing.\nGood bye")
    else:
        print("Invalid Input!!!!")


game()
