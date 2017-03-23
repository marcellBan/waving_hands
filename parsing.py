"""
    input parsing functions
    by night5word and grammar_naz1
"""

from random import choice
from copy import deepcopy as dcp
from spell_data import SPELL_DATA, MAX_GESTURE_LENGTH


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
