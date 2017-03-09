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
MAX_GESTURE_LENGTH = 8


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
        gets a turn input from a player
    """
    # print previous turns
    print_input_layout(inputting_player, other_player)
    # get valid input from player
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


def print_input_layout(input_player, other_player):
    """
        clears the screen\n
        prints the gestures from the previous turns\n
        prints the players healths
    """
    # calculate the number of turns to print
    gestures_to_print = min(len(input_player.hands), MAX_PRINTED_LINES)
    # clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    # print header with names
    print("     {0}{2}{1}".format(input_player.name, other_player.name,
                                  " " * SPACING_BETWEEN_COLUMNS))
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
    print("-" * 40)
    # print both player's health
    print("Your health: {0}     {1}'s health: {2}"
          .format(input_player.health, other_player.name, other_player.health))


def calc_turn_result(p_one, p_two):
    """
        calculates the results of the last turn
        and displays it
    """
    # parse gestures
    parse_for_player(p_one)
    parse_for_player(p_two)
    # cast spells
    for spell in p_one.spell_to_cast:
        SPELL_DICT[spell](p_one, p_two)
    for spell in p_two.spell_to_cast:
        SPELL_DICT[spell](p_two, p_one)
    # TODO reset shields, decrease multi turn effects


def parse_for_player(parsed_player):
    """
        parses the hands of the given player and marks the appropriate spell(s) for casting
    """
    # clear last turns spells
    parsed_player.spell_to_cast.clear()
    left_hand = []
    right_hand = []
    try:
        for i in range(MAX_GESTURE_LENGTH):
            # get gestures from player object
            ges_l, ges_r = parsed_player.get_gesture(i + 1)
            # convert gestures to indicate double handed gestures in the last two places
            last_index = -min(2, i + 1)
            ges_l_zip = ges_l[:last_index]
            ges_r_zip = ges_r[:last_index]
            for left, right in zip(ges_l[last_index:], ges_r[last_index:]):
                if left == right:
                    ges_l_zip = "".join((ges_l_zip, "(", left.lower()))
                    ges_r_zip = "".join((ges_r_zip, "(", left.lower()))
                else:
                    ges_l_zip = "".join((ges_l_zip, left))
                    ges_r_zip = "".join((ges_r_zip, right))
            # find spells in dictionary and add them to a list
            for key in GESTURE_DICT:
                if (key == ges_l_zip or key == ges_l) and key not in left_hand:
                    left_hand.append(GESTURE_DICT[key])
                if (key == ges_r_zip or key == ges_r) and key not in right_hand:
                    right_hand.append(GESTURE_DICT[key])
    except ValueError:
        pass
    finally:
        resolve_conflicts(parsed_player, left_hand, right_hand)


def resolve_conflicts(parsed_player, left_hand, right_hand):
    """
        resolve conflicts between to be casted spells
    """
    # multiple spells can be cast
    if len(left_hand) > 1:
        ask_player_which_spell_to_cast(parsed_player, left_hand, "left hand")
    if len(right_hand) > 1:
        ask_player_which_spell_to_cast(parsed_player, right_hand, "right hand")
    # one spell has double handed finish
    to_cast = list(left_hand, right_hand)
    for key, value in GESTURE_DICT.items():
        if len(left_hand) != 0 and value == left_hand[0]  and \
                key[-2:] in ["(f", "(p", "(s", "(w", "(d"]:
            ask_player_which_spell_to_cast(parsed_player, to_cast, "hands")
            break
        if len(right_hand) != 0 and value == right_hand[0] and \
                key[-2:] in ["(f", "(p", "(s", "(w", "(d"]:
            ask_player_which_spell_to_cast(parsed_player, to_cast, "hands")
            break
    # mark spells to cast
    parsed_player.spell_to_cast.extend(to_cast)


def ask_player_which_spell_to_cast(player, spells, hand):
    """
        asks the player which spell do they want to cast with the given hand
    """
    # clear screen and print options
    os.system('cls' if os.name == 'nt' else 'clear')
    for idx, item in enumerate(spells):
        print(str(idx + 1) + ". " + item)
    # get input from player
    pick = -1
    while pick < 1 or pick > len(spells):
        answer = input("{0}, which spell do you want to cast with your {1}?\n"
                       .format(player.name, hand))
        try:
            pick = int(answer)
        except ValueError:
            pass
    # save only the chosen spell
    chosen_one = spells[pick - 1]
    spells.clear()
    spells.append(chosen_one)


def do_game_end(p_one, p_two):
    """
        finishes a game
    """
    # draw game
    if p_one.health <= 0 and p_two.health <= 0:
        print("It's a draw. Both players died.")
    elif p_one.effects["surrender"] and p_two.effects["surrender"]:
        print("It's a draw. Both players surrendered.")
    # one of the players dies
    elif p_one.health <= 0:
        print("{0} wins by killing {1}.".format(p_two.name, p_one.name))
    elif p_two.health <= 0:
        print("{0} wins by killing {1}.".format(p_one.name, p_two.name))
    # one of the players
    elif p_one.effects["surrender"]:
        print("{0} surrenders. {1} wins.".format(p_one.name, p_two.name))
    elif p_two.effects["surrender"]:
        print("{0} surrenders. {1} wins.".format(p_two.name, p_one.name))


def main():
    """
        main program loop
    """
    running = True
    while running:
        answer = input("Do you want to play? (Yes/No) ").lower()
        if answer == "yes" or answer == "y":
            play_game()
        elif answer == "no" or answer == "n":
            running = False

main()
