import random
from os import system, name
from guess_the_number_art import logo

def clear(): 
    _ = system('clear')

def random_number():
    number = random.randint(1, 100)
    return number

def guess_checker(guess, number):
    if guess == number:
        return f"   You got it! The answer was {number}"
    elif guess > number:
        return "   Too high.\n   Guess again."
    elif guess < number:
        return "   Too low.\n   Guess again."

def play_game():

    print(logo)

    picked_number = random_number()
    is_game_over = False

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")

    def difficulty_check():
        if difficulty == 'easy':
            attempts = 10
            return attempts
        if difficulty == 'hard':
            attempts = 5
            return attempts
        else:
            clear()
            play_game()

    def user_guess():
        guess = int(input("Make a guess: "))
        if 0 < guess < 100:
            return guess
        else:
            user_guess()

    difficulty = input("Choose your difficulty. Type 'easy' or 'hard: ").lower()
    attempts = difficulty_check()

    while not is_game_over:
        user_number = user_guess()
        print(guess_checker(user_number, picked_number))
        if user_number == picked_number:
            is_game_over = True
        elif attempts == 1:
            print("You lose. You ran out of attempts.")
            is_game_over = True
        else:
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number.")

clear()
while input("Would you like to play Guess The Number? Type 'y' or 'n': ").lower() == "y":
    clear()
    play_game()
