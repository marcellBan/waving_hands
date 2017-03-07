"""
    player object for the waving hands game
    by night5word and grammar_naz1
"""


class Player(object):
    """
        represents a player
    """

    def __init__(self, effects, spell_list, health=15):
        self.health = health
        self.hands = []  # (* or _, left, right)
        self.spell_to_cast = [(x, y) for x in spell_list for y in [False]]
        self.effects = effects
        self.name = input("Enter a player name: ")

    def get_hand_str(self, idx):
        """
            returns a string representing the players hand in the specified turn
        """
        return "{0}-{1}-{2}".format(self.hands[idx][0], self.hands[idx][1], self.hands[idx][2])

    def add_hand(self, gesture):
        """
            adds a hand to the list of hands
        """
        ges = gesture.split('-')
        self.hands.append(('*' if self.effects["invisible"] > 0 else '_', ges[0], ges[1]))
