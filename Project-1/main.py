from random import randint
from art import logo

EASY_DIFFICULTY_TURNS = 10
HARD_DIFFICULTY_TURNS = 5


def check_answer(guess, answer, turns):
    """Checks answer against guess, returns the number of turns remaining"""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print ("Too low.")
        return turns - 1
    elif guess == answer:
        print(f"You got it right! The answer was {answer}")

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_DIFFICULTY_TURNS
    else:
        return HARD_DIFFICULTY_TURNS


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, correct answer is {answer}")

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You ran out of guesses. You lose.")
            return
        elif guess != answer:
            print("Guess again.")
game()
