"""
    damaging spell functions
    by night5word and grammar_naz1
"""

from spell_helpers import check_counter_spell, check_reflection
from spell_helpers import check_dispel_magic, get_visible_results


def missile(casting_player, other_player):  # Only reflectable
    """Missile spell"""
    targeted_player, _ = check_reflection(other_player, casting_player)
    if "Shield" not in targeted_player.spell_to_cast \
            and "Protection From Evil" not in targeted_player.spell_to_cast\
            and targeted_player.effects["protection_from_evil"] == 0 \
            and not check_counter_spell(targeted_player) \
            and not check_dispel_magic(targeted_player):
        targeted_player.damage_taken += 1
        res = ["Missile succesfully hit " + targeted_player.name] * 2
        vis = True
    else:
        res = ["Missile thwarted"] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, targeted_player)


def finger_of_death(casting_player, other_player):  # Only reflectable
    """Finger of Death spell"""
    targeted_player, _ = check_reflection(other_player, casting_player)
    if not check_dispel_magic(targeted_player) \
            and not targeted_player.effects["raise_dead"]:
        targeted_player.damage_taken += 100
        res = ["Wizard " + targeted_player.name +
               " got brutally fingered and died in a very painful way..."] * 2
        vis = True
    else:
        res = ["Finger of Death could not be casted on " + targeted_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, targeted_player)


def lightning_bolt(casting_player, other_player):  # Only reflectable
    """Lightning Bolt spell"""
    targeted_player, non_targeted_player = check_reflection(other_player, casting_player)
    if not check_dispel_magic(targeted_player):
        targeted_player.damage_taken += 5
        res = [targeted_player.name + "received 5 damage from " + non_targeted_player.name] * 2
        vis = True
    else:
        res = ["Lightning Bolt could not be casted on " + targeted_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, targeted_player)


def cause_light_wounds(casting_player, other_player):  # Only reflectable
    """Cause Light Wounds spell"""
    targeted_player, non_targeted_player = check_reflection(other_player, casting_player)
    if not check_dispel_magic(targeted_player):
        targeted_player.damage_taken += 2
        res = [targeted_player.name + "received 2 damage from " + non_targeted_player.name] * 2
        vis = True
    else:
        res = ["Cause Light Wounds could not be casted on " + targeted_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, targeted_player)


def cause_heavy_wounds(casting_player, other_player):  # Only reflectable
    """Cause Heavy Wounds spell"""
    targeted_player, non_targeted_player = check_reflection(casting_player, other_player)
    if not check_dispel_magic(targeted_player):
        targeted_player.damage_taken += 3
        res = [targeted_player.name + "received 3 damage from " + non_targeted_player.name] * 2
        vis = True
    else:
        res = ["Cause Heavy Wounds could not be casted on " + targeted_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, targeted_player)


def fireball(casting_player, other_player):  # Only reflectable
    """Fireball spell"""
    targeted_player, non_targeted_player = check_reflection(casting_player, other_player)
    if not check_dispel_magic(targeted_player) \
            and "Ice Storm" not in targeted_player.spell_to_cast:
        targeted_player.damage_taken += 5
        res = [targeted_player.name + "received 5 damage from " + non_targeted_player.name] * 2
        vis = True
    else:
        res = ["Fireball could not be casted on " + targeted_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, targeted_player)


def fire_storm(casting_player, other_player):  # Neither reflectable, nor choosable
    """Fire Storm spell"""
    if not check_dispel_magic(other_player) and "Ice Storm" not in other_player.spell_to_cast:
        if not check_counter_spell(other_player):
            other_player.damage_taken += 5
        casting_player.damage_taken += 5
        res = ["Fire Storm casted by " + casting_player.name] * 2
        vis = True
    else:
        res = ["Fire Storm nullified"] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis)


def ice_storm(casting_player, other_player):  # Neither reflectable, nor choosable
    """Ice Storm spell"""
    if not check_dispel_magic(other_player) and "Fire Storm" not in other_player.spell_to_cast:
        if not check_counter_spell(other_player):
            other_player.damage_taken += 5
            # casting_player only gets damaged if enemy doesn't have fireball
        if "Fireball" not in other_player.spell_to_cast:
            casting_player.damage_taken += 5
        res = ["Ice Storm casted by " + casting_player.name] * 2
        vis = True
    else:
        res = ["Ice Storm nullified"] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis)
