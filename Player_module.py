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
        lst=[]
        for character in self.characters:
            lst.append(str(character))
        display_lst = "\n\n".join(lst)

        return display_lst

    def set_characters(self, characters):
        self.characters = characters

