# This class represents basic card
class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def show(self):
        print("{} of {}".format(self.value, self.suit))


# This class represents role card
# Every role card has role and description
class RoleCard(Card):
    def __init__(self, role, description):
        self.role = role
        self.description = description

    def show(self):
        print("Role: {0}\nDescription: {1}\n".format(self.role, self.description))
