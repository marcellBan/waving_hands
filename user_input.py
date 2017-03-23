"""
    user input functions
    by night5word and grammar_naz1
"""

import os
from random import choice
from spell_helpers import check_reflection

# formatting constants
MAX_PRINTED_LINES = 10
SPACING_BETWEEN_COLUMNS = 10
DIVIDER_WIDTH = 50


def do_input(inputting_player, other_player, previous_turn_results):
    """
        gets a turn input from a player
    """
    # print previous turns
    print_input_layout(inputting_player, other_player, previous_turn_results)
    # check for amnesia
    if not inputting_player.effects["amnesia"]:
        # get valid input from player
        print(
            "Valid gesture format: X-Y | where X and Y are from [' ','stab','S','D','W','P','F','C']")
        gesture = input(inputting_player.name + ", please enter your gesture for this turn: ")
        while not is_valid_gesture(gesture, inputting_player.effects["fear"]):
            gesture = input(inputting_player.name + ", please enter a valid gesture: ")
        inputting_player.effects["fear"] = False
        # confusion effect
        if inputting_player.effects["confusion"]:
            gesture = alter_gesture(gesture, choice([True, False]), choice(["C", "D", "S", "W", "F", "P"]))
            if inputting_player.permanent != "confusion":
                inputting_player["confusion"] = False
    else:
        print("You are affected by Amnesia this turn, your gesture will be the same as last turn.")
        gesture = inputting_player.get_hand_str(-1)
        if inputting_player.permanent != "amnesia":
            inputting_player["amnesia"] = False
    # get gesture for Charm person spell's effect
    if other_player.effects["charm_person"]:
        chosen_gesture = None
        while chosen_gesture not in ["stab", " "]:
            chosen_gesture = input("Choose a gesture for " + other_player.name + "'s " +
                                   "left" if other_player.affected_hand == "l" else "right" + " hand. (stab/ )\n")
        other_player.new_gesture = chosen_gesture
    inputting_player.add_hand(gesture, other_player.effects["blindness"] > 0)


def alter_gesture(gesture, hand, new_gesture):
    """
        changes the gesture on the given hand to the new gesture and returns it\n
        hand = True  --> left hand\n
        hand = False --> right hand
    """
    tmp = gesture.split('-')
    if hand:
        tmp[0] = new_gesture
    else:
        tmp[1] = new_gesture
    return "-".join(tmp)


def is_valid_gesture(gesture, fear):
    """
        checks the validity of a given gesture
    """
    if fear:
        valid_gestures = [
            " ", "P", "stab", "W"
        ]
    else:
        valid_gestures = [
            # non-gestures
            " ", "stab",
            # one handed gestures
            "F", "P", "S", "W", "D",
            # two handed gestures
            "C"
        ]
    ges = gesture.split('-')
    # exactly 2 hands?
    if len(ges) != 2:
        return False
    # valid gesture on each hand?
    if ges[0] not in valid_gestures:
        return False
    if ges[1] not in valid_gestures:
        return False
    if ges[0] == 'C' or ges[1] == 'C':
        return ges[0] == ges[1]
    return True


def print_input_layout(input_player, other_player, previous_turn_results):
    """
        clears the screen\n
        prints the results of the previous turn\n
        prints the gestures from the previous turns\n
        prints the players' healths
    """
    # calculate the number of turns to print
    gestures_to_print = min(len(input_player.hands), MAX_PRINTED_LINES)
    # clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    # print previous turn results
    print("The following happened in the last turn:")
    # divider
    print("-" * DIVIDER_WIDTH)
    for item in previous_turn_results:
        if item != "":
            print(item)
    print("\nThese were the hands played in the previous turns:")
    # divider
    print("-" * DIVIDER_WIDTH)
    # print header with names
    print("     {0}{1}{2}".format(input_player.name, " " * SPACING_BETWEEN_COLUMNS,
                                  other_player.name))
    # print turns
    for i in range(gestures_to_print):
        # calculate index to use
        idx = len(input_player.hands) - gestures_to_print + i
        input_hand = input_player.get_hand_str(idx)
        # other player invisible
        if other_player.hands[idx][0] == "*":
            print("{1:2d}   {0}".format(input_hand, idx + 1) +
                  " " * (len(input_player.name) + SPACING_BETWEEN_COLUMNS -
                         len(input_hand)) +
                  "-----")
        # other player visible
        else:
            print("{1:2d}   {0}".format(input_hand, idx + 1) +
                  " " * (len(input_player.name) + SPACING_BETWEEN_COLUMNS -
                         len(input_hand)) +
                  "{0}".format(other_player.get_hand_str(idx)))
    # divider
    print("-" * DIVIDER_WIDTH)
    # print both player's health
    print("Your health: {0}     {1}'s health: {2}"
          .format(input_player.health, other_player.name, other_player.health))
    # divider
    print("-" * DIVIDER_WIDTH)


def choose_target(casting_player, other_player):
    """prompt player to choose target, returns the target and non target player in a tuple"""
    while True:
        answer = input(casting_player.name +
                       ": Choose your target: s = self, o = opponent\n").lower()
        if answer == "s":
            return check_reflection(casting_player, other_player)
        elif answer == "o":
            return check_reflection(other_player, casting_player)


def choose_hand(non_target_player, target_player, spell_name):
    """prompts the player to choose one of the hands of the other player to be affected"""
    while True:
        hand = input(non_target_player.name + " choose which hand of " +
                     target_player.name + " do you want to affect with" + spell_name + " spell! (l/r)\n").lower()
        if hand == "l" or hand == "r":
            target_player.affected_hand = hand
            return
