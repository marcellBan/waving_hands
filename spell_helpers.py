"""
    spell function helper functions
    by night5word and gramarnaz1
"""


def check_reflection(target_player, non_target_player):
    """returns the tharget and non target players in a tuple"""
    if not check_counter_spell(non_target_player) and not check_dispel_magic(non_target_player):
        if "Magic Mirror" in target_player.spell_to_cast:
            # magic mirror effective, reflection happened
            return non_target_player, target_player
    # no reflection happened
    return target_player, non_target_player


def check_counter_spell(player):
    """checks if the player casted counter spell"""
    if "Counter-Spell" in player.spell_to_cast:
        return True
    return False


def check_dispel_magic(player):
    """checks if the player casted dispel"""
    if "Dispel Magic" in player.spell_to_cast:
        return True
    return False


def check_remove_enchantment(player):
    """checks if the player casted Remove Enchantment"""
    if "Remove Enchantment" in player.spell_to_cast:
        return True
    return False


def init_effects(casting_player, other_player):
    """initializes both player's effect dictionaries"""
    for i in [casting_player, other_player]:
        i.effects["disease"] = False
        i.effects["invisible"] = False
        i.effects["protection_from_evil"] = 0
        i.effects["resist_heat"] = False
        i.effects["resist_cold"] = False
        i.effects["poison"] = False
        i.effects["anti_spell"] = False
        i.effects["fear"] = False
        i.effects["paralysis"] = False
        i.effects["charm_person"] = False
        i.effects["confusion"] = False
        i.effects["amnesia"] = False
        i.effects["permanency"] = 0
        i.effects["delayed_effect"] = 0
        i.effects["blindness"] = 0
        i.effects["haste"] = 0
        i.effects["time_stop"] = False
        # permanent and banked spells
        i.permanent = ""
        i.banked = ""


def get_visible_results(casting_player, other_player, spell_result, always_visible=False, target_player=None):
    """returns a tuple of what the players saw from this spell cast"""
    if (other_player.effects["blindness"] > 0) \
            and (not always_visible and target_player != other_player):
        spell_result[1] = ""
    if casting_player.effects["blindness"] > 0 \
            and target_player == other_player:
        spell_result[0] = ""
    return tuple(spell_result)
