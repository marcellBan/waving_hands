"""
    non-spell functions
    by night5word and grammar_naz1
"""

from spell_helpers import check_counter_spell, check_dispel_magic
from spell_helpers import get_visible_results


def stab(casting_player, other_player):  # Neither reflectable, nor choosable
    """Stab no-spell"""
    if "Shield" not in other_player.spell_to_cast \
            and "Protection From Evil" not in other_player.spell_to_cast \
            and other_player.effects["protection_from_evil"] == 0 \
            and not check_counter_spell(other_player) \
            and not check_dispel_magic(other_player):
        other_player.damage_taken += 1
        res = [casting_player.name + " stabbed " + other_player.name] * 2
        vis = True
    else:
        res = [casting_player.name + " could not stab " + other_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis)


def nothing(casting_player, other_player):
    """Nothing no-spell"""
    res = [casting_player.name + " did nothing"] * 2
    return get_visible_results(casting_player, other_player, res)


def surrender(casting_player, other_player):
    """Surrender no-spell"""
    casting_player.effects["surrender"] = True
    res = [casting_player.name + " surrendered."] * 2
    return get_visible_results(casting_player, other_player, res, True)
