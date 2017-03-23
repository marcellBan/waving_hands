"""
    enchantment spell functions
    by night5word and grammar_naz1
"""

from spell_helpers import *


def amnesia(casting_player, other_player):  # Only reflectable
    """Amnesia spell"""
    targeted_player, _ = check_reflection(casting_player, other_player)
    if not check_remove_enchantment(targeted_player) \
            and not check_dispel_magic(targeted_player) \
            and not check_counter_spell(targeted_player) \
            and "Confusion" not in targeted_player.spell_to_cast \
            and "Charm Person" not in targeted_player.spell_to_cast \
            and "Paralysis" not in targeted_player.spell_to_cast \
            and "Fear" not in targeted_player.spell_to_cast:
        targeted_player.effects["amnesia"] = True
        res = ["Amnesia casted on " + targeted_player.name] * 2
        vis = True
    else:
        res = ["Amnesia could not be casted on " + targeted_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, targeted_player)


def confusion(casting_player, other_player):  # Only reflectable
    """Confusion spell"""
    targeted_player, _ = check_reflection(casting_player, other_player)
    if not check_remove_enchantment(targeted_player) \
            and not check_dispel_magic(targeted_player) \
            and not check_counter_spell(targeted_player) \
            and "Amnesia" not in targeted_player.spell_to_cast \
            and "Charm Person" not in targeted_player.spell_to_cast \
            and "Paralysis" not in targeted_player.spell_to_cast \
            and "Fear" not in targeted_player.spell_to_cast:
        targeted_player.effects["confusion"] = True
        res = ["Confusion casted on " + targeted_player.name] * 2
        vis = True
    else:
        res = ["Confusion could not be casted on " + targeted_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, targeted_player)


def charm_person(casting_player, other_player):
    """Charm person spell"""
    target_player, non_target_player = check_reflection(other_player, casting_player)
    if not check_remove_enchantment(target_player) \
            and not check_dispel_magic(target_player) \
            and not check_counter_spell(target_player) \
            and "Amnesia" not in target_player.spell_to_cast \
            and "Confusion" not in target_player.spell_to_cast \
            and "Paralysis" not in target_player.spell_to_cast \
            and "Fear" not in target_player.spell_to_cast:
        target_player.effects["charm_person"] = True
        choose_hand(non_target_player, target_player, "Charm person")
        res = ["Charm Person casted on " + target_player.name] * 2
        vis = True
    else:
        res = ["Charm Person could not be casted on " + target_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, target_player)


def paralysis(casting_player, other_player):
    """Paralysis spell"""
    target_player, non_target_player = check_reflection(other_player, casting_player)
    if not check_remove_enchantment(target_player) \
            and not check_dispel_magic(target_player) \
            and not check_counter_spell(target_player) \
            and "Amnesia" not in target_player.spell_to_cast \
            and "Confusion" not in target_player.spell_to_cast \
            and "Charm_person" not in target_player.spell_to_cast \
            and "Fear" not in target_player.spell_to_cast:
        target_player.effects["paralysis"] = True
        choose_hand(non_target_player, target_player, "Paralysis")
        res = ["Paralysis casted on " + target_player.name] * 2
        vis = True
    else:
        res = ["Paralysis could not be casted on " + target_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, target_player)


def fear(casting_player, other_player):
    """Fear spell"""
    targeted_player, _ = check_reflection(casting_player, other_player)
    if not check_remove_enchantment(targeted_player) \
            and not check_dispel_magic(targeted_player) \
            and not check_counter_spell(targeted_player) \
            and "Amnesia" not in targeted_player.spell_to_cast \
            and "Confusion" not in targeted_player.spell_to_cast \
            and "Charm_person" not in targeted_player.spell_to_cast \
            and "Paralysis" not in targeted_player.spell_to_cast:
        targeted_player.effects["fear"] = True
        res = ["Fear casted on " + targeted_player.name] * 2
        vis = True
    else:
        res = ["Fear could not be casted on " + targeted_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, targeted_player)


def protection_from_evil(casting_player, other_player):
    """Protection From Evil spell"""
    if not check_remove_enchantment(other_player) \
            and not check_dispel_magic(other_player) \
            and not check_counter_spell(other_player):
        other_player.effects["protection_from_evil"] = 4
        res = ["Protection From Evil casted on " + other_player.name] * 2
        vis = True
    else:
        res = ["Protection From Evil could not be casted on " + other_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis)


def resist_heat(casting_player, other_player):  # Neither reflectable, nor choosable
    """Resist Heat spell"""
    if not check_remove_enchantment(other_player) \
            and not check_dispel_magic(other_player) \
            and not check_counter_spell(other_player):
        other_player.effects["resist_heat"] = True
        res = ["Resist Heat casted on " + other_player.name] * 2
        vis = True
    else:
        res = ["Resist Heat could not be casted on " + other_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis)


def resist_cold(casting_player, other_player):  # Neither reflectable, nor choosable
    """Resist Cold spell"""
    if not check_remove_enchantment(other_player) \
            and not check_dispel_magic(other_player) \
            and not check_counter_spell(other_player):
        other_player.effects["resist_cold"] = True
        res = ["Resist Cold casted on " + other_player.name] * 2
        vis = True
    else:
        res = ["Resist Cold could not be casted on " + other_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis)


def disease(casting_player, other_player):  # Only reflectable
    """Disease spell"""
    targeted_player, _ = check_reflection(casting_player, other_player)
    if not check_remove_enchantment(targeted_player) \
            and not check_dispel_magic(targeted_player) \
            and not check_counter_spell(targeted_player) \
            and "Cure Heavy Wounds" not in targeted_player.spell_to_cast:
        targeted_player.effects["disease"] = 7
        res = ["Disease casted on " + targeted_player.name + ". Death is coming..."] * 2
        vis = True
    else:
        res = ["Disease could not be casted on " + targeted_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, targeted_player)


def poison(casting_player, other_player):  # Only reflectable
    """Poison spell"""
    targeted_player, _ = check_reflection(casting_player, other_player)
    if not check_remove_enchantment(targeted_player) \
            and not check_dispel_magic(targeted_player) \
            and not check_counter_spell(targeted_player):
        targeted_player.effects["poison"] = 7
        res = ["Poison casted on " + targeted_player.name + ". Death will be slow and painful..."] * 2
        vis = True
    else:
        res = ["Poison could not be casted on " + targeted_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, targeted_player)


def blindness(casting_player, other_player):
    """Blindness spell"""
    chosen_player = choose_target_player(casting_player, other_player)
    if not check_remove_enchantment(chosen_player) \
            and not check_dispel_magic(chosen_player) \
            and not check_counter_spell(chosen_player):
        chosen_player.effects["blindness"] = 4
        res = ["Blindness casted on " + chosen_player.name] * 2
        vis = True
    else:
        res = ["Blindness could not be casted on " + targeted_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, targeted_player)


def invisibility(casting_player, other_player):  # Neither reflectable, nor choosable
    """Invisibility spell"""
    if not check_remove_enchantment(other_player) \
            and not check_dispel_magic(other_player) \
            and not check_counter_spell(other_player):
        other_player.effects["invisible"] = True
        res = [other_player.name + " became invisible"] * 2
        vis = True
    else:
        res = [other_player.name + " could not become invisible"] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis)


def haste(casting_player, other_player):
    """Haste spell"""
    chosen_player = choose_target_player(casting_player, other_player)
    if not check_remove_enchantment(chosen_player) \
            and not check_dispel_magic(chosen_player) \
            and not check_counter_spell(chosen_player):
        chosen_player.effects["haste"] = 4
        res = ["Haste casted on " + chosen_player.name] * 2
        vis = True
    else:
        res = ["Haste could not be casted on " + other_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis)


def delayed_effect(casting_player, other_player):
    """Delayed Effect spell"""
    if not check_remove_enchantment(other_player) \
            and not check_dispel_magic(other_player) \
            and not check_counter_spell(other_player):
        other_player.effects["delayed_effect"] = 4
        res = ["Delayed Effect casted on " + other_player.name] * 2
        vis = True
    else:
        res = ["Delayed Effect could not be casted on " + other_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis)


def permanency(casting_player, other_player):
    """Permanency spell"""
    chosen_player = check_reflection(casting_player, other_player)
    if not check_remove_enchantment(chosen_player) \
            and not check_dispel_magic(chosen_player) \
            and not check_counter_spell(chosen_player):
        chosen_player.effects["permanency"] = 4
        res = ["Permanency casted on " + chosen_player.name] * 2
        vis = True
    else:
        res = ["Permanency could not be casted on " + chosen_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, chosen_player)
