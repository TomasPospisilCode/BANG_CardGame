#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from Game_module import Game


class TestGame(unittest.TestCase):
    def test_player_count(self):
        # Test that exception is raised when player count isn't in specified range
        # Test that exception is raised when player count is zero or negative

        self.assertRaises(ValueError, Game.__init__, self, 0)
        self.assertRaises(ValueError, Game.__init__, self, -5)
        self.assertRaises(ValueError, Game.__init__, self, 2)
        self.assertRaises(ValueError, Game.__init__, self, 8)

    def test_player_count_values(self):
        # Test that when we give as argument non-integer value, exception is raised
        self.assertRaises(ValueError, Game.__init__, self, 'blabla')
        self.assertRaises(ValueError, Game.__init__, self, None)
        self.assertRaises(ValueError, Game.__init__, self, True)



