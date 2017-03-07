"""
    player object for the waving hands game
"""

class Player(object):
    """
        represents a player
    """

    def __init__(self, effects=None, health=14):
        self.health = health
        self._left_hand = []
        self._right_hand = []
        if effects:
            self.effects = effects
        else:
            self.effects = {}

    def get_hands(self, turns):
        """
            returns a list of tuples with the players last turns
        """
