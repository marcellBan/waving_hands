#!/usr/bin/env python3
"""
    waving hands game
    by night5word and grammar_naz1
"""

import os
from copy import deepcopy as dcp
from player import Player
from spells import SPELL_DICT, EFFECT_DICT


def play_game():
    """
        plays a whole game
    """
    # init
    print("First player:")
    player_one = Player(dcp(EFFECT_DICT), list(SPELL_DICT.keys()))
    print("Second player:")
    player_two = Player(dcp(EFFECT_DICT), list(SPELL_DICT.keys()))
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
    for item in ges:
        if valid_gestures.count(item) == 0:
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
    gestures_to_print = min(len(input_player.hands), 10)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("     {0}          {1}".format(input_player.name, other_player.name))
    for i in range(gestures_to_print):
        idx = -(i + 1)
        input_hand = input_player.get_hand_str(idx)
        if other_player.hands[idx][0] == "*":  # other player invisible
            print("{1:2d}   {0}".format(input_hand, input_player.hands
                                        .index(input_player.hands[idx]) + 1) +
                  " " * (10 - len(input_player.hands[idx])) +
                  "-----")
        else:
            print("{1:2d}   {0}".format(input_hand, input_player.hands
                                        .index(input_player.hands[idx]) + 1) +
                  " " * (10 - len(input_player.hands[idx])) +
                  "{0}".format(other_player.get_hand_str(idx)))
    print("-" * 30)
    print("Your health: {0}     {1}'s health: {2}"
          .format(input_player.health, other_player.name, other_player.health))


def calc_turn_result(p_one, p_two):
    """
        calculates the results of the last turn
    """


def do_game_end(p_one, p_two):
    """
        finishes a game
    """
    if p_one.health <= 0:
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
