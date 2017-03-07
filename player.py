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
        self.hands = [] # (* or _, left, right)
        self.spell_to_cast = [(x, y) for x in spell_list for y in [False]]
        self.effects = effects
        self.name = input("Enter a player name: ")
