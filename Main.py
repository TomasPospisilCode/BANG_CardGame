#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Object of this class represents one card
# Every card has suite and color
import copy
from random import shuffle
from Cards_module import *
from Deck_module import *
from Player_module import *
from Game_module import *


def main():
    # Initialize Role and character decks
    role_deck = RoleDeck()
    characters_deck = CharactersDeck()

    print(role_deck)

    # Sets game, if less or more than required count of player is set, error message is displayed
    # try:
    #     game = Game(7)
    # except ValueError:
    #     print("This game can play only 4-7 players")
    #
    # game.make_actual_role_deck(role_deck)  # Sets Role deck for given number of players
    # game.deal_roles()  # Deal role cards to players
    # game.deal_characters(characters_deck)
    # game.show_characters()


if __name__ == '__main__':
    main()
