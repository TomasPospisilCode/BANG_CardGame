#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This class represents player


class Player:
    def __init__(self, number):
        self.number = number
        self.role = None
        self.characters = None

    def get_role(self):
        return self.role

    def set_role(self, role):
        self.role = role

    def get_characters(self):
        return self.characters

    def set_characters(self, characters):
        self.characters = characters

    def show_role(self):
        print("Hráč č.{0}".format(self.number))
        print(self.role)

    def show_characters(self):
        print(self.characters[0])
        print(self.characters[1])
