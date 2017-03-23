#!/usr/bin/env python3
"""
    main game logic
    by night5word and grammar_naz1
"""

import os
from copy import deepcopy as dcp
from player import Player
from spell_data import EFFECT_DICT, SPELL_DATA
from user_input import do_input
from parsing import parse_for_player


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
