"""
    protection spell functions
    by night5word and grammar_naz1
"""

from spell_helpers import check_counter_spell, get_visible_results
from spell_helpers import init_effects, check_dispel_magic
from user_input import choose_target


def shield(casting_player, other_player):
    """Shield spell"""
    res = [casting_player.name + ": Shield activated"] * 2
    return get_visible_results(casting_player, other_player, res)


def remove_enchantment(casting_player, other_player):  # Both choosable and reflectable
    """Remove Enchantment spell"""
    targeted_player, _ = choose_target(casting_player, other_player)
    if not check_counter_spell(targeted_player):
        init_effects(casting_player, other_player)
        res = ["Effects and enchantments are removed from: " + targeted_player.name] * 2
        vis = True
    else:
        res = ["Effects and enchantments could no be removed from: " + targeted_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, targeted_player)


def magic_mirror(casting_player, other_player):  # Neither reflectable, nor choosable
    """Magic Mirror spell"""
    if not check_counter_spell(other_player) \
            and not check_dispel_magic(other_player) \
            and "Fire Storm" not in other_player.spell_to_cast \
            and "Ice Storm" not in other_player.spell_to_cast:
        res = [casting_player.name + ": Magic Mirror used"] * 2
    else:
        res = ["Magic Mirror could not be cast by: " + casting_player.name] * 2
    return get_visible_results(casting_player, other_player, res)


def counter_spell(casting_player, other_player):  # Neither reflectable, nor choosable
    """Counter Spell spell"""
    if not check_dispel_magic(other_player):
        res = [casting_player.name + ": Counter Spell used"] * 2
    else:
        res = ["Counter spell could no be casted by " + casting_player.name] * 2
    return get_visible_results(casting_player, other_player, res)


def dispel_magic(casting_player, other_player):  # Neither reflectable, nor choosable
    """Dispel Magic spell"""
    init_effects(casting_player, other_player)
    res = [casting_player.name + ": Dispel Magic casted"] * 2
    return get_visible_results(casting_player, other_player, res)


def raise_dead(casting_player, other_player):  # Neither reflectable, nor choosable
    """Raise dead spell"""
    casting_player.effects["raise_dead"] = True
    res = [casting_player.name + ": Raise Dead casted"] * 2
    return get_visible_results(casting_player, other_player, res)


def cure_light_wounds(casting_player, other_player):  # Neither reflectable, nor choosable
    """Cure Light Wounds spell"""
    if casting_player.health < 15:
        casting_player.damage_taken -= 1
        res = [casting_player.name + ": Restored 1 hp"] * 2
    else:
        res = ["Cure wasted: nothing to cure on " + casting_player.name] * 2
    return get_visible_results(casting_player, other_player, res)


def cure_heavy_wounds(casting_player, other_player):  # Neither reflectable, nor choosable
    """Cure Heavy Wounds spell"""
    if casting_player.health < 14:
        casting_player.damage_taken -= 2
        casting_player.effects["disease"] = False
        res = [casting_player.name + ": Restored 2 hp, disease effect removed."] * 2
    elif casting_player.health == 14:
        casting_player.damage_taken -= 1
        casting_player.effects["disease"] = False
        res = [casting_player.name + ": Restored 1 hp, disease effect removed."] * 2
    else:
        res = ["Cure wasted: nothing to cure on " + casting_player.name] * 2
    return get_visible_results(casting_player, other_player, res)
