# This class represents basic card
class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        print("This is text representation of Card class")


# This class represents role card
# Every role card has role and description
class RoleCard(Card):
    def __init__(self, role, description):
        self.role = role
        self.description = description

    def __str__(self):
        return "Role: {0}\nDescription: {1}".format(self.role, self.description)


class CharacterCard(Card):

    def __init__(self, name, life_count, description):
        self.name = name
        self.life_count = life_count
        self.description = description

    def __str__(self):
        return "Name: {}\nLife count {}\nDescription {}".format(self.name, str(self.life_count), self.description)




