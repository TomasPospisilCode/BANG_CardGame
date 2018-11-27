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


class CharactersDeck(Deck):
    # Stored data about characters in tuple
    bart_cassidy = ("Bart Cassidy", 4, "Ztratí-li život, lízne si kartu z balíčku")
    black_jack = ("Black Jack", 4, "Během první fáze svého tahu ukáže druhou kartu, kterou si líznul: je-li tato "
                                   "karta srdcová či kárová (červené barvy), lízne si ještě jednu kartu navíc(již "
                                   "opět skrytě)")
    calamity_janet = ("Calamity Janet", 4, "Může používat karty BANG! jako karty Vedle! a naopak. Zahraje-li kartu "
                                           "Vedle! jako BANG!(jako normální výstřel), nemůže zahrát další BANG!(tedy, "
                                           "pokud nemá ve hře Volcanic. Tuto schopnost může využívat při Duelu, "
                                           "Indiánech apod.)")
    el_gringo = ("El Gringo", 3, "Lízne si náhodně kartu z ruky hráče, který mu způsobí ztrátu života (za každý "
                                 "ztracený život jednu). Nemá-li protivník žádnou kartu v ruce, nic se neděje, "
                                 "Pozor na to, že zranění od Dynamitu není způsobeno hráčem, který dynamit vyložil. "
                                 "Pokud El Gringo ztratí život poté, co sám zahrál Duel, kartu si nedobírá")
    jesse_jones = ("Jesse Jones", 4, "Během první fáze svého tahu si může vybrat, jestli si lízne první kartu z "
                                     "balíčku nebo z ruky libovolného hráče. Druhou kartu si vždy líže z balíčku")
    jourdonnais = ("Jourdonnais", 4, "Má vlastně neustále ve hře fiktivní kartu Barel. Pokud se tedy brání proti "
                                     "výstřelu BANG!, vytáhne si náhodnou kartu z balíčku. Pokud je tato srdcová, "
                                     "střele se vyhnul a neztrácí život. Pokud má Jourddonais ve hře zahranou kartu "
                                     "Barel, může otáčet při útoku BANGem! dvě karty (Za každý barel jednu)")
    kit_carlson = ("Kit Carlson", 3, "Během první fáze svého kola se podívá na vrchní tři karty balíčku, vybere si z "
                                     "nich 2, které si nechá, a třetí vrátí zpět na vrchol balíčku")
    lucky_duke = ("Lucky Duke", 4, "Vždy, když si má líznout!(např. u karet Vězení, Dynamit), otočí si vrchní 2 karty "
                                   "balíčku a vybere si, která se mu hodí. Obě karty jsou následně odhozeny. Toto "
                                   "neplatí při dobírání dvou karet během první fáze tahu.")
    paul_regret = ("Paul Regret", 3, "Má vlastně neustále ve hře fiktivní kartu Mustang. Další skutečný Mustang se "
                                     "přičítá k fiktivnímu to znamená,že může být až o dvě místa dál než normálně.")
    pedro_ramirez = ("Pedro Ramirez", 4, "Během první fáze svého tahu si může líznout první kartu z odhazovacího "
                                         "balíčku (tu, která se nachází nahoře), druhou si dobere z hlavního lízacího"
                                         " balíčku.")
    rose_doolan = ("Rose Doolan", 4, "Má vlastně neustále ve hře fiktivní kartu Appaloosa. Další skutečná karta "
                                     "Appaloosa se přičítá k fiktivní,to znamená že si vidí ostatní hráče až o dvě "
                                     "místa blíže než normálně.")
    sid_ketchum = ("Sid Ketchum", 4, "Kdykoli může odhodit jakékoliv dvě karty z ruky, aby si vrátil jeden život. "
                                     "Tuto schopnost může použít i několikrát za sebou v jednom tahu.")
    slab_the_killer = ("Slab the Killer", 4, "Protivníci, kteří chtějí zrušit jeho kartu BANG! musí zahrát 2 karty "
                                             "Vedle!. Schová-li se někdo úspěšně za Barel,bere se to jako zahrána "
                                             "karta Vedle! (je tedy nutné zahrát ještě jednu kartu Vedle!).")
    suzy_lafayette = ("Suzy Lafayette", 4, "Kdykoli nemá žádnou kartu v ruce lízne si novou z lízacího balíčku.")
    vulture_sam = ("Vulture Sam", 4, "Kdykoli je některý z hráčů vyřazen ze hry, Sam získá všechny jeho karty, "
                                     "které měl v ruce i na stole.")
    willy_the_kid = ("Willy the Kid", 4, "Může zahrát libovolný počet karet BANG! během svého tahu.")

    # Adding characters to the list
    characters_list = [bart_cassidy, black_jack, calamity_janet, el_gringo,
                       jesse_jones, jourdonnais, kit_carlson, lucky_duke, paul_regret,
                       pedro_ramirez, suzy_lafayette, vulture_sam,
                       rose_doolan, sid_ketchum, slab_the_killer, willy_the_kid]

    # List of cards of character
    character_cards_list = []

    def __init__(self):

        for character in self.characters_list:
            self.character_cards_list.append(CharacterCard(character[0],character[1], character[2]))

    def show(self):
        for card in self.character_cards_list:
            print("Card:\nName: {}\nLifes: {}\nDescription: {}\n".format(card.name, card.life_count, card.description))
