"""
    player object for the waving hands game
    by night5word and grammar_naz1
"""


class Player(object):
    """
        represents a player
    """

    def __init__(self, effects, health=15):
        self.health = health
        self.hands = list()  # (* or _, left, right)
        self.spell_to_cast = list()
        self.permanent = ""
        self.banked = ""
        self.affected_hand = None
        self.new_gesture = ""
        self.damage_taken = 0
        self.effects = effects
        self.name = input("Enter a player name: ")

    def get_hand_str(self, idx):
        """
            returns a string representing the players hand in the specified turn
        """
        return "{0}-{1}".format(self.hands[idx][1], self.hands[idx][2])

    def add_hand(self, gesture, other_player_blind=False):
        """
            adds a hand to the list of hands
        """
        ges = gesture.split('-')
        self.hands.append(
            ('*' if self.effects["invisible"] or other_player_blind else '_', ges[0], ges[1]))

    def get_gesture(self, length):
        """
            returns a gesture with the desired length
            raises ValueError if the requested length is too long
        """
        if length > len(self.hands):
            raise ValueError
        else:
            gesture_l = ""
            gesture_r = ""
            ges_len = min(len(self.hands), length)
            for i in range(ges_len):
                idx = len(self.hands) - length + i
                gesture_l = "".join((gesture_l, self.hands[idx][1]))
                gesture_r = "".join((gesture_r, self.hands[idx][2]))
            if self.hands[-1][1] == " " or self.hands[-1][1] == "stab":
                gesture_l = self.hands[-1][1]
            if self.hands[-1][2] == " " or self.hands[-1][2] == "stab":
                gesture_r = self.hands[-1][2]
            return (gesture_l, gesture_r)
