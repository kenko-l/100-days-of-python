from email.contentmanager import get_and_fixup_unknown_message_content
from msilib.schema import BBControl
from token import AMPER

from art import logo
from art import vs
from game_data import data
import random


score = 0

def check_answer(follower_countA, follower_countB):
    global score
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    if follower_countA > follower_countB and answer == 'A':
        score += 1
        return True
    elif follower_countB > follower_countA and answer == 'B':
        score += 1
        return True
    else:
        return False


def game():
    global score
    print(logo)
    game_over = False

    while not game_over:
        # Select two random entries
        random_entryA = random.choice(data)
        random_entryB = random.choice(data)

        # Ensure A and B are different
        while random_entryA == random_entryB:
            random_entryB = random.choice(data)

        nameA = random_entryA['name']
        follower_countA = random_entryA['follower_count']
        descriptionA = random_entryA['description']
        countryA = random_entryA['country']

        nameB = random_entryB['name']
        follower_countB = random_entryB['follower_count']
        descriptionB = random_entryB['description']
        countryB = random_entryB['country']

        print(f"\nCompare A: {nameA}, a {descriptionA}, from {countryA}.")
        print(vs)
        print(f"Against B: {nameB}, a {descriptionB}, from {countryB}.")

        result = check_answer(follower_countA, follower_countB)

        if result:
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True

game()
# in my data I need to be able to get the name of a person, and then i should be able to extract their name, occupation, and country, and follower count

# I should be able to print those different stuff

# Values will be called personA, and personB

# print out those stuff for person a and b, but not the follower count

# Who has more followers? Type 'A' or 'B':
    # need a randomizer for all the people
    # If personA > personB, and answer == A,
    # If personB > personA, and answer == B
        # then
        # continue game and loop back to the "Who had more followers"
        # If answer wrong then "Sorry, that's wrong. Final scpre: {score}

        #keep a counter for every loop count

