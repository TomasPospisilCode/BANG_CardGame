# This class represents basic deck
import copy
from Cards_module import *


class Deck:
    def __init__(self):
        pass


# This class represents deck of role cards
class RoleDeck(Deck):
    def __init__(self):
        self.list_of_roles = []
        for role in range(4):  # Cycle fills the deck with role cards
            # Something like switch using dictionaries. In every iteration different role is added to the deck of the
            # role cards. At first, the information about card are saved to a list
            current_role = {0: ["Šerif", "Zabij všechny bandity a odpadlíka"],
                            1: ["Pomocník šerifa", "Ochraňuj šerifa, zabij všechny bandity a odpadlíka"],
                            2: ["Odpadlík", "Zůstaň poslední ve hře"],
                            3: ["Bandita", "Zabij šerifa"]}.get(role, "Something is wrong")
            # Create RoleCard object and initialize it with information from the list
            current_role_card = RoleCard(current_role[0], current_role[1])

            # If role is Vice or Bandit, the card is added to a deck multiple times
            # Since we want different instances of the object, we need to append deepcopy of current instance
            if role == 1:
                for x in range(2):
                    self.list_of_roles.append(copy.deepcopy(current_role_card))
            elif role == 3:
                for x in range(3):
                    self.list_of_roles.append(copy.deepcopy(current_role_card))
            else:
                self.list_of_roles.append(current_role_card)

    # Go through every card in the deck and display it individually
    def show(self):
        for card in self.list_of_roles:
            card.show()
