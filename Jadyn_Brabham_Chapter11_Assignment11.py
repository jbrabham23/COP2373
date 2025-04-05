# Jadyn Brabham
# Chapter 11 Assignment 11
# This program is a game program that deals a Poker hand of five cards. It
# then prompts the user to enter a series of numbers that selects cards to
# be replaced during a draw phase, then it prints the result of drawing
# the new cards.

import random

# Deck class
class Deck:
    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        self.cards_in_play_list = []
        self.discards_list = []
        random.shuffle(self.card_list)

    def deal(self):
        if len(self.card_list) < 1:
            random.shuffle(self.discards_list)
            self.card_list = self.discards_list
            self.discards_list = []
            print('Reshuffling...!!!')
        new_card = self.card_list.pop()
        self.cards_in_play_list.append(new_card)
        return new_card

    def new_hand(self):
        self.discards_list += self.cards_in_play_list
        self.cards_in_play_list.clear()

# Function to display a hand of cards
def display_hand(hand):
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']

    print('\nYour hand:')
    for card in hand:
        r = card % 13
        s = card // 13
        print(f"{ranks[r]} of {suits[s]}")

# Function to play the Poker game
def play_poker():
    # Create the deck of 52 cards
    my_deck = Deck(52)

    # Deal 5 cards
    hand = [my_deck.deal() for _ in range(5)]

    # Display the hand
    display_hand(hand)

    # Prompt the user to replace cards
    to_replace = input('\nEnter the positions (1-5) of the cards you want to replace,'
                       'separated by commas:')
    to_replace =  [int(x) - 1 for x in to_replace.split(',')]

    # Replace the selected cards
    print('\nReplacing selected cards...\n')
    for pos in to_replace:
        if 0 <= pos < 5:
            hand[pos] = my_deck.deal()

    # Display the new hand
    display_hand(hand)

# Run the poker game
play_poker()