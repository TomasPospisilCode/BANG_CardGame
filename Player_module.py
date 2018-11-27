#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This class represents player
class Player:
    def __init__(self, number):
        self.number = number
        self.role = None

    def get_role(self):
        return self.role

    def set_role(self, role):
        self.role = role

    def show_role(self):
        print("Hráč č.{0}".format(self.number))
        self.role.show()
