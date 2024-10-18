import random

# Constants for card values
FACE_CARD_VALUE = 10
ACE_HIGH_VALUE = 11
ACE_LOW_VALUE = 1
DEALER_STAND_VALUE = 17
BLACKJACK_VALUE = 21


def create_deck():
    """Create and return a shuffled deck of cards."""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck


def calculate_hand_value(hand):
    """Calculate and return the value of a hand."""
    value = 0
    aces = 0
    for card in hand:
        rank = card.split()[0]
        if rank in ['Jack', 'Queen', 'King']:
            value += FACE_CARD_VALUE
        elif rank == 'Ace':
            aces += 1
        else:
            value += int(rank)

    # Add Aces
    for _ in range(aces):
        if value + ACE_HIGH_VALUE <= BLACKJACK_VALUE:
            value += ACE_HIGH_VALUE
        else:
            value += ACE_LOW_VALUE

    return value


def display_hand(name, hand, show_all=True):
    """Display a player's hand."""
    print(f"{name}'s hand:")
    if show_all:
        for card in hand:
            print(f"  {card}")
        print(f"Total value: {calculate_hand_value(hand)}")
    else:
        print(f"  {hand[0]}")
        print("  [Hidden card]")
    print()


def player_turn(deck, player_hand):
    """Handle the player's turn."""
    while True:
        display_hand("Player", player_hand)
        choice = input("Do you want to hit or stand? ").lower().strip()

        if choice == 'hit':
            player_hand.append(deck.pop())
            if calculate_hand_value(player_hand) > BLACKJACK_VALUE:
                display_hand("Player", player_hand)
                print("Bust! You lose.")
                return False
        elif choice == 'stand':
            return True
        else:
            print("Invalid choice. Please enter 'hit' or 'stand'.")


def dealer_turn(deck, dealer_hand):
    """Handle the dealer's turn."""
    while calculate_hand_value(dealer_hand) < DEALER_STAND_VALUE:
        dealer_hand.append(deck.pop())
        display_hand("Dealer", dealer_hand)
        if calculate_hand_value(dealer_hand) > BLACKJACK_VALUE:
            print("Dealer busts! You win!")
            return False
    return True


def play_blackjack():
    """Main game loop for Blackjack."""
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print("Welcome to Blackjack!")
    display_hand("Dealer", dealer_hand, show_all=False)

    if calculate_hand_value(player_hand) == BLACKJACK_VALUE:
        display_hand("Player", player_hand)
        print("Blackjack! You win!")
        return

    if player_turn(deck, player_hand):
        if dealer_turn(deck, dealer_hand):
            # Both player and dealer have valid hands, compare values
            player_value = calculate_hand_value(player_hand)
            dealer_value = calculate_hand_value(dealer_hand)
            display_hand("Player", player_hand)
            display_hand("Dealer", dealer_hand)

            if player_value > dealer_value:
                print("You win!")
            elif player_value < dealer_value:
                print("Dealer wins!")
            else:
                print("It's a tie!")


def play_again():
    """Ask the player if they want to play again."""
    while True:
        choice = input("Do you want to play again? (yes/no): ").lower().strip()
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            return False
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")


def main():
    """Main function to run the Blackjack game with replay option."""
    while True:
        play_blackjack()
        if not play_again():
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()