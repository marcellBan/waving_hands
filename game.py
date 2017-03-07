#!/usr/bin/env python3
"""
    waving hands game
    by night5word and grammar_naz1
"""


from copy import deepcopy as dcp
from player import Player
from spells import SPELL_DICT, EFFECT_DICT

main()


def main():
    """
        main game logic
    """
    running = True
    while running:
        answer = input("Do you want to play? (Yes/No) ")
        if answer.tolower() == "yes" or answer.tolower() == "y":
            play_game()
        elif answer.tolower() == "no" or answer.tolower() == "n":
            running = False


def play_game():
    """
        plays a whole game
    """
    # init
    player_one = Player(dcp(EFFECT_DICT))
    player_two = Player(dcp(EFFECT_DICT))
    # main game loop
    while player_one.health > 0 and player_two.health > 0:
        do_input(player_one)
        do_input(player_two)
        calc_turn_result(player_one, player_two)
    do_game_end()

def do_input(player):
    """
        gets a turn input from the player
    """


def calc_turn_result(p_one, p_two):
    """
        calculates the results of the last turn
    """

def do_game_end():
    """
        finishes a game
    """
