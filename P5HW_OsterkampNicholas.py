#Math Quiz
#12/7/23
#CTI-110 P5HW - Math Quiz
#Nicholas Osterkamp

import random

def generate_numbers():
    num1 = random.randint(100, 999)
    num2 = random.randint(100, 999)
    return num1, num2

def display_addition_problem(num1, num2):
    print(num1)
    print("+" + str(num2))

def display_subtraction_problem(num1, num2):
    print(num1 + num2)
    print("-" + str(num2))

def get_user_input():
    return int(input("Enter your answer: "))

def addition_quiz():
    correct_answer = None
    num_guesses = 0

    while True:
        if correct_answer is None:
            num1, num2 = generate_numbers()
            correct_answer = num1 + num2

        display_addition_problem(num1, num2)
        user_answer = get_user_input()
        num_guesses += 1

        if user_answer == correct_answer:
            print("Congratulations! Your answer is correct.")
            print(f"It took you {num_guesses} guesses.")
            return
        else:
            if user_answer < correct_answer:
                print("Incorrect! Your answer is too low. Try again.")
            else:
                print("Incorrect! Your answer is too high. Try again.")

def subtraction_quiz():
    correct_answer = None
    num_guesses = 0

    while True:
        if correct_answer is None:
            num1, num2 = generate_numbers()
            correct_answer = num1

        display_subtraction_problem(num1, num2)
        user_answer = get_user_input()
        num_guesses += 1

        if user_answer == correct_answer:
            print("Congratulations! Your answer is correct.")
            print(f"It took you {num_guesses} guesses.")
            return
        else:
            print("Incorrect! Try again.")

def play_math_quiz():
    while True:
        print("\nMAIN MENU:")
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit")
        choice = input("Please choose one of the menu options: ")

        if choice == "1":
            addition_quiz()
        elif choice == "2":
            subtraction_quiz()
        elif choice == "3":
            print("Exiting the Math Quiz Game.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    play_math_quiz()