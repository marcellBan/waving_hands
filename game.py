#!/usr/bin/env python3
"""
    waving hands game
    by night5word and grammar_naz1
"""

import os
from copy import deepcopy as dcp
from player import Player
from spells import GESTURE_DICT, SPELL_DICT, EFFECT_DICT

MAX_PRINTED_LINES = 10
SPACING_BETWEEN_COLUMNS = 10
MAX_GESTURE_DEATH = 8


def play_game():
    """
        plays a whole game
    """
    # init
    print("First player:")
    player_one = Player(dcp(EFFECT_DICT))
    print("Second player:")
    player_two = Player(dcp(EFFECT_DICT))
    # main game loop
    while player_one.health > 0 and player_two.health > 0 and \
            not player_one.effects["surrender"] and not player_two.effects["surrender"]:
        do_input(player_one, player_two)
        do_input(player_two, player_one)
        calc_turn_result(player_one, player_two)
    do_game_end(player_one, player_two)


def do_input(inputting_player, other_player):
    """
        gets a turn input from the player
    """
    print_input_layout(inputting_player, other_player)
    gesture = input("Please enter your gesture for this turn: ")
    while not is_valid_gesture(gesture):
        gesture = input("Gesture format: L-R\nPlease enter a valid gesture: ")
    inputting_player.add_hand(gesture)


def is_valid_gesture(gesture):
    """
        checks the validity of a given gesture
    """
    valid_gestures = [
        # non-gestures
        " ", "stab",
        # one handed gestures
        "F", "P", "S", "W", "D",
        # two handed gestures
        "C"
    ]
    ges = gesture.split('-')
    if len(ges) != 2:
        return False
    if valid_gestures.count(ges[0]) == 0:
        return False
    if valid_gestures.count(ges[1]) == 0:
        return False
    if ges[0] == 'C' or ges[1] == 'C':
        return ges[0] == ges[1]
    return True


def print_input_layout(input_player, other_player):
    """
        clears the screen\n
        prints the gestures from the previous turns\n
        prints the players healths
    """
    gestures_to_print = min(len(input_player.hands), MAX_PRINTED_LINES)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("     {0}{2}{1}".format(input_player.name, other_player.name,
                                  " " * SPACING_BETWEEN_COLUMNS))
    for i in range(gestures_to_print):
        idx = len(input_player.hands) - gestures_to_print + i
        input_hand = input_player.get_hand_str(idx)
        if other_player.hands[idx][0] == "*":  # other player invisible
            print("{1:2d}   {0}".format(input_hand, idx + 1) +
                  " " * (len(input_player.name) + SPACING_BETWEEN_COLUMNS -
                         len(input_hand)) +
                  "-----")
        else:
            print("{1:2d}   {0}".format(input_hand, idx + 1) +
                  " " * (len(input_player.name) + SPACING_BETWEEN_COLUMNS -
                         len(input_hand)) +
                  "{0}".format(other_player.get_hand_str(idx)))
    print("-" * 40)
    print("Your health: {0}     {1}'s health: {2}"
          .format(input_player.health, other_player.name, other_player.health))


def calc_turn_result(p_one, p_two):
    """
        calculates the results of the last turn
        and displays it
    """
    parse_for_player(p_one)
    parse_for_player(p_two)
    # TODO does this work properly?
    for spell in p_one.spell_to_cast:
        SPELL_DICT[spell](p_one, p_two)
    for spell in p_two.spell_to_cast:
        SPELL_DICT[spell](p_two, p_one)


def parse_for_player(parsed_player):
    """
        parses the hands of the given player and marks the appropriate spell(s) for casting
    """
    parsed_player.spell_to_cast.clear()
    try:
        for i in range(MAX_GESTURE_DEATH):
            ges_l, ges_r = parsed_player.get_gesture(i + 1)
            ges_l_zip = ""
            ges_r_zip = ""
            for left, right in zip(ges_l, ges_r):
                if left == right:
                    ges_l_zip = "".join((ges_l_zip, "(", left.lower()))
                    ges_r_zip = "".join((ges_r_zip, "(", left.lower()))
                else:
                    ges_l_zip = "".join((ges_l_zip, left))
                    ges_r_zip = "".join((ges_r_zip, right))
            for key in GESTURE_DICT:
                if key == ges_l_zip and parsed_player.spell_to_cast.count(GESTURE_DICT[key]) == 0:
                    parsed_player.spell_to_cast.append(GESTURE_DICT[key])
                if key == ges_r_zip and parsed_player.spell_to_cast.count(GESTURE_DICT[key]) == 0:
                    parsed_player.spell_to_cast.append(GESTURE_DICT[key])
    except ValueError:
        pass  # TODO do we need to do anything here????


def do_game_end(p_one, p_two):
    """
        finishes a game
    """
    if p_one.health <= 0 and p_two.health <= 0:
        print("It's a draw. Both players died.")
    elif p_one.effects["surrender"] and p_two.effects["surrender"]:
        print("It's a draw. Both players surrendered.")
    elif p_one.health <= 0:
        print("{0} wins by killing {1}.".format(p_two.name, p_one.name))
    elif p_two.health <= 0:
        print("{0} wins by killing {1}.".format(p_one.name, p_two.name))
    elif p_one.effects["surrender"]:
        print("{0} surrenders. {1} wins.".format(p_one.name, p_two.name))
    elif p_two.effects["surrender"]:
        print("{0} surrenders. {1} wins.".format(p_two.name, p_one.name))


def main():
    """
        main game logic
    """
    running = True
    while running:
        answer = input("Do you want to play? (Yes/No) ")
        if answer.lower() == "yes" or answer.lower() == "y":
            play_game()
        elif answer.lower() == "no" or answer.lower() == "n":
            running = False

main()
