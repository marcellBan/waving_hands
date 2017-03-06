"""
    player object and methods
"""

class Player(object):
    """represents a player"""

    def __init__(self, health=14, effects=None):
        self.health = health
        self._left_hand = []
        self._right_hand = []
        if effects:
            self.effects = effects
        else:
            self.effects = {}#lollllll

    def get_hands(turns):
        """"""
