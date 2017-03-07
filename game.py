#!/usr/bin/env python3
"""
    waving hands game
    by night5word and grammar_naz1
"""


from copy import deepcopy as dcp
from player import Player
from spells import SPELL_DICT, EFFECT_DICT


def play_game():
    """
        plays a whole game
    """
    # init
    player_one = Player(dcp(EFFECT_DICT), list(SPELL_DICT.keys()))
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


def print_input_layout(input_player, other_player):
    """
        prints the gestures from the previous turns
    """
    #TODO indexing error
    gestures_to_print = 10
    print("    p1          p2")
    for i in range(-1, -(gestures_to_print + 1), -1):
        if other_player.hands[i][0] == "*":  # other player invisible
            print("   {0}".format(input_player.hands[i]) +
                  " " * (10 - len(input_player.hands[i])) +
                  "-----")
        else:
            print("   {0}".format(input_player.hands[i]) +
                  " " * (10 - len(input_player.hands[i])) +
                  "{0}".format(other_player.hands[i]))


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
