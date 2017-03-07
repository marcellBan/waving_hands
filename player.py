"""
    player object for the waving hands game
    by night5word and grammar_naz1
"""


class Player(object):
    """
        represents a player
    """

    def __init__(self, effects, spell_list, health=14):
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
