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

    # Sets game, if less or more than required count of player is set, error message is displayed
    try:
        game = Game(7)
    except ValueError:
        print("Blablabla")

    game.make_actual_role_deck(role_deck)  # Filter role deck based on player count
    game.deal_roles()  # Deal role cards to players
    characters_deck.show()


if __name__ == '__main__':
    main()
