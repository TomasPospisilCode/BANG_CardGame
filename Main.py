#!/usr/bin/python

# Object of this class represents one card
# Every card has suite and color
import copy
from random import shuffle
from Cards_module import *
from Deck_module import *
from Player_module import *
from Game_module import *


def main():
    testDeck = RoleDeck()
    # Sets game, if less or more than required count of player is set, error message is displayed
    try:
        game = Game(7)

    except ValueError as error:
        print("Minimum player count is 4 and maximum is 7")

    game.make_actual_role_deck(testDeck)  # Filter role deck based on player count
    game.deal_roles()  # Deal role cards to players

    # Show role of every player
    for player in game.player_list:
        player.show_role()


if __name__ == '__main__':
    main()
