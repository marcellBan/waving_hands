#!/usr/bin/env python3
"""
    waving hands game
    by night5word and grammar_naz1
"""

import os
from copy import deepcopy as dcp
from random import choice
from player import Player
from spells import SPELL_DATA, EFFECT_DICT

MAX_PRINTED_LINES = 10
SPACING_BETWEEN_COLUMNS = 10
MAX_GESTURE_LENGTH = 8
DIVIDER_WIDTH = 50


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
    previous_turn_results = list()
    while player_one.health > 0 and player_two.health > 0 and \
            not player_one.effects["surrender"] and not player_two.effects["surrender"]:
        # get player inputs, twice if haste is active
        do_input(player_one, player_two, previous_turn_results[0])
        if player_one.effects["haste"] > 0:
            do_input(player_one, player_two, previous_turn_results[0])
        do_input(player_two, player_one, previous_turn_results[1])
        if player_two.effects["haste"] > 0:
            do_input(player_two, player_one, previous_turn_results[1])
        # handle Charm person and paralysis spells' effect
        for p in [player_one, player_two]:
            if p.effects["charm_person"]:
                tmp = list(p.hands[-1])
                if p.affected_hand == "l":
                    tmp[1] = p.new_gesture
                else:
                    tmp[2] = p.new_gesture
                p.hands[-1] = tuple(tmp)
                p.affected_hand = None
                p.new_gesture = ""
                p.effects["charm_person"] = False
            if p.effects["paralysis"]:
                tmp = list(p.hands[-1])
                if p.affected_hand == "l":
                    tmp[1] = swap_gesture(tmp[1])
                else:
                    tmp[2] = swap_gesture(tmp[2])
                p.hands[-1] = tuple(tmp)
                p.affected_hand = None
                p.effects["paralysis"] = False
        # calculate turn results
        previous_turn_results = calc_turn_result(player_one, player_two)
        for p in [player_one, player_two]:
            if not p.effects["raise_dead"]:
                p.health -= p.damage_taken
            else:
                if p.health - p.damage_taken > 0:
                    p.damage_taken -= 5
                    p.health -= p.damage_taken
                    if p.health > 15:
                        p.health = 15
                p.effects["raise_dead"] = False
    do_game_end(player_one, player_two)


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


def swap_gesture(gesture):
    """swaps a gesture for paralysis"""
    swap_dict = {
        "C": "F",
        "S": "D",
        "W": "P",
        "P": "P",
        "D": "D",
        "F": "F",
        " ": " ",
        "stab": "stab"
    }
    return swap_dict[gesture]


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


def calc_turn_result(p_one, p_two):
    """
        calculates the results of the last turn
        and displays it
    """
    # parse gestures
    parse_for_player(p_one)
    parse_for_player(p_two)
    # cast spells
    p_one_results = list()
    p_two_results = list()
    for spell in p_one.spell_to_cast:
        for item in SPELL_DATA:
            if item[0] == spell:
                p1, p2 = item[2](p_one, p_two)
                p_one_results.append(p1)
                p_two_results.append(p2)
    for spell in p_two.spell_to_cast:
        for item in SPELL_DATA:
            if item[0] == spell:
                p2, p1 = item[2](p_two, p_one)
                p_one_results.append(p1)
                p_two_results.append(p2)
    handle_effects(p_one, p_two)
    return [p_one_results, p_two_results]


def handle_effects(p_one, p_two):
    """
        calculatates the effect changes on the players
    """
    for p in [p_one, p_two]:
        # disease effect
        if p.effects["disease"] > 1:
            p.effects["disease"] -= 1
        elif p.effects["disease"] == 1:
            p.health = 0
        # poison effect
        if p.effects["poison"] > 1:
            p.effects["poison"] -= 1
        elif p.effects["poison"] == 1:
            p.health = 0
        # protection from evil effect
        if p.effects["protection_from_evil"] > 0:
            p.effects["protection_from_evil"] -= 1
        # blindness effect
        if p.effects["blindness"] > 0:
            p.effects["blindness"] -= 1
        # haste effect
        if p.effects["haste"] > 0:
            p.effects["haste"] -= 1
        # delayed effect
        if p.effects["delayed_effect"] > 0:
            p.effects["delayed_effect"] -= 1
        # permanency effect
        if p.effects["permanency"] > 0:
            p.effects["permanency"] -= 1


def parse_for_player(parsed_player):
    """
        parses the hands of the given player and marks the appropriate spell(s) for casting
    """
    # clear last turn's spells
    parsed_player.spell_to_cast.clear()
    left_hand = []
    right_hand = []
    try:
        for i in range(MAX_GESTURE_LENGTH):
            # get gestures from player object
            ges_l, ges_r = parsed_player.get_gesture(i + 1)
            # convert gestures to indicate double handed gestures in the last
            # two places
            last_index = -min(2, i + 1)
            ges_l_zip = ges_l[:last_index]
            ges_r_zip = ges_r[:last_index]
            for left, right in zip(ges_l[last_index:], ges_r[last_index:]):
                if left == right and left != 'C':
                    ges_l_zip = "".join((ges_l_zip, "(", left.lower()))
                    ges_r_zip = "".join((ges_r_zip, "(", left.lower()))
                else:
                    ges_l_zip = "".join((ges_l_zip, left))
                    ges_r_zip = "".join((ges_r_zip, right))
            # find spells in spell list and add them to a separate list
            for item in SPELL_DATA:
                if (item[1] == ges_l_zip or item[1] == ges_l) and item[0] not in left_hand:
                    left_hand.append(item[0])
                if (item[1] == ges_r_zip or item[1] == ges_r) and item[0] not in right_hand:
                    right_hand.append(item[0])
    except ValueError:
        pass
    finally:
        if "Surrender" in left_hand or "Surrender" in right_hand:
            parsed_player.spell_to_cast.append("Surrender")
        else:
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
    to_cast = dcp(left_hand)
    to_cast.extend(right_hand)
    for item in SPELL_DATA:
        if len(left_hand) != 0 and item[0] == left_hand[0] and \
                (item[1][-2:] in ["(f", "(p", "(s", "(w", "(d"] or item[1][-1] == 'C'):
            ask_player_which_spell_to_cast(parsed_player, to_cast, "hands")
            break
        if len(right_hand) != 0 and item[0] == right_hand[0] and \
                (item[1][-2:] in ["(f", "(p", "(s", "(w", "(d"] or item[1][-1] == 'C'):
            ask_player_which_spell_to_cast(parsed_player, to_cast, "hands")
            break
    # delayed effect
    if parsed_player.banked != "":
        res = ask_player_to_cast_banked_spell(parsed_player)
        if res:
            to_cast.append(parsed_player.banked)
            parsed_player.banked = ""
    if "Delayed Effect" in to_cast and len(to_cast) == 2:
        to_cast.remove("Delayed Effect")
        parsed_player.banked = to_cast[0]
        to_cast.clear()
    if parsed_player.effects["delayed_effect"] > 0:
        if len(to_cast) == 1:
            parsed_player.banked = to_cast[0]
            parsed_player.effects["delayed_effect"] = 0
            to_cast.clear()
        elif len(to_cast) == 2:
            parsed_player.banked = ask_player_which_spell_to_bank(parsed_player, to_cast)
            parsed_player.effects["delayed_effect"] = 0
            to_cast.remove(parsed_player.banked)
    # permanency effect
    if "Permanency" in to_cast and len(to_cast) == 2:
        to_cast.remove("Permanency")
        parsed_player.banked = to_cast[0]
        to_cast.clear()
    if parsed_player.effects["permanency"] > 0:
        if len(to_cast) == 1:
            parsed_player.permanent = to_cast[0]
            parsed_player.effects["permanency"] = 0
            to_cast.clear()
        elif len(to_cast) == 2:
            parsed_player.permanent = ask_player_which_spell_to_bank(parsed_player, to_cast)
            parsed_player.effects["permanency"] = 0
            to_cast.remove(parsed_player.permanent)
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
    # clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
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
