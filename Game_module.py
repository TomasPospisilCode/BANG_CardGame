#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This class represents instance of game

from Player_module import Player
from random import shuffle


class Game:
    def __init__(self, player_count):
        self.player_list = []
        self.current_game_role_deck = []
        # Entered value has to be integer
        if type(player_count) != int:
            raise ValueError('Player count has to be integer')
        # Minimum count of player is 4 and maximum is 7, so if it's less or more, exception is thrown
        if player_count < 4 or player_count > 7:
            raise ValueError('Incorrect range of player_count')

        self.playerCount = player_count

        # Add every player to player list
        for player in range(player_count):
            current_player = Player(player + 1)  # In parameters I give numbers to player, starting with one
            self.player_list.append(current_player)

    # Based on player count - filter role cards to one deck
    def make_actual_role_deck(self, role_deck):
        self.current_game_role_deck = {
            4: [role_deck.list_of_roles[0], role_deck.list_of_roles[3], role_deck.list_of_roles[4],
                role_deck.list_of_roles[5]],
            5: [role_deck.list_of_roles[0], role_deck.list_of_roles[1], role_deck.list_of_roles[3],
                role_deck.list_of_roles[4], role_deck.list_of_roles[5]],
            6: [role_deck.list_of_roles[0], role_deck.list_of_roles[1], role_deck.list_of_roles[3],
                role_deck.list_of_roles[4], role_deck.list_of_roles[5], role_deck.list_of_roles[6]],
            7: [role_deck.list_of_roles[0], role_deck.list_of_roles[1], role_deck.list_of_roles[2],
                role_deck.list_of_roles[3], role_deck.list_of_roles[4], role_deck.list_of_roles[5],
                role_deck.list_of_roles[6]]}.get(self.playerCount, "Something is wrong")

    # Shows the roles in current game
    def show_roles(self):
        for card in self.current_game_role_deck: card.show()

    # Deal roles to individual players
    def deal_roles(self):
        shuffle(self.current_game_role_deck)
        # Every player gets role card from randomly shuffled deck
        iteration = 0
        for player in self.player_list:
            player.set_role(self.current_game_role_deck[iteration])
            iteration = iteration + 1

    # Deal characters to individual players
    def deal_characters(self, characters_deck):
        shuffle(characters_deck.character_cards_list)
        # Every player gets 2 character card from randomly shuffled deck
        for player in self.player_list:
            player.set_characters(tuple(characters_deck.character_cards_list[0:2]))
            del characters_deck.character_cards_list[0:2]

    def show_characters(self):
        for player in self.player_list:
            print("\nPlayer: {}".format(player.number))
            player.get_role().show()
            player.get_characters()[0].show()
            player.get_characters()[1].show()
            # print("Characters: {}\n".format())

