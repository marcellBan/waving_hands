"""
    spell functions and dictionary and effect dictionary
    by night5word and grammar_naz1
"""


def choose_target(casting_player, other_player):
    """prompt player to choose target"""
    while True:
        answer = input(casting_player.name +
                       ": Choose your target: s = self, o = opponent\n").lower()
        if answer == "s":
            return casting_player
        elif answer == "o":
            return other_player


def check_magic_mirror(casting_player, other_player):
    """returns the target player depending on the existence of magic mirror"""
    if not check_counter_spell(casting_player) and not check_dispel_magic(casting_player):
        if "Magic Mirror" in other_player.spell_to_cast:
            return casting_player
    return other_player


def check_counter_spell(player):
    """checks if the player casted counter spell"""
    if "Counter-Spell" in player.spell_to_cast:
        return True
    else:
        return False


def check_dispel_magic(player):
    """checks if the player casted dispel"""
    if "Dispel Magic" in player.spell_to_cast:
        return True
    else:
        return False

# Protection:


def shield(casting_player, other_player):
    """Shield spell"""
    return casting_player.name + ": Shield activated"


def remove_enchantment(casting_player, other_player):
    """Remove Enchantment spell"""
    chosen_player = check_magic_mirror(casting_player, other_player)
    if not check_counter_spell(chosen_player):

        casting_player.effects["invisible"] = False
        casting_player.effects["protection_from_evil"] = 0
        casting_player.effects["resist_heat"] = False
        casting_player.effects["resist_cold"] = False
        casting_player.effects["disease"] = False
        casting_player.effects["poison"] = False
        return "Effects and enchantments are removed from: " + chosen_player.name
    return "Effects and enchantments could no be removed from: " + chosen_player.name


def magic_mirror(casting_player, other_player):
    """Magic Mirror spell"""
    if not check_counter_spell(other_player) \
            and not check_dispel_magic(other_player) \
            and "Fire Storm" not in other_player.spell_to_cast \
            and "Ice Storm" not in other_player.spell_to_cast:

        return casting_player.name + ": Magic Mirror used"


def counter_spell(casting_player, other_player):
    """Counter Spell spell"""
    if not check_dispel_magic(other_player) \
            and "Finger of Death" not in other_player.spell_to_cast:
        return casting_player.name + ": Counter Spell used"
    return "Counter spell could no be casted by " + casting_player.name


def dispel_magic(casting_player, other_player):
    """Dispel Magic spell"""
    if "Surrender" not in other_player.spell_to_cast \
            and "Stab" not in other_player.spell_to_cast:

        casting_player.effects["invisible"] = False
        casting_player.effects["protection_from_evil"] = 0
        casting_player.effects["resist_heat"] = False
        casting_player.effects["resist_cold"] = False
        casting_player.effects["disease"] = False
        casting_player.effects["poison"] = False

        other_player.effects["invisible"] = False
        other_player.effects["protection_from_evil"] = 0
        other_player.effects["resist_heat"] = False
        other_player.effects["resist_cold"] = False
        other_player.effects["disease"] = False
        other_player.effects["poison"] = False
        return casting_player.name + ": Dispel Magic used"
    return "Dispel Magic could not be casted by " + casting_player.name


def raise_dead(casting_player, other_player):
    """Raise Dead spell"""
    pass


def cure_light_wounds(casting_player, other_player):
    """Cure Light Wounds spell"""
    if casting_player.health < 15:
        casting_player.health += 1
        return casting_player.name + ": Restored 1 hp"

    else:
        return "Cure wasted: nothing to cure on " + casting_player.name


def cure_heavy_wounds(casting_player, other_player):
    """Cure Heavy Wounds spell"""
    if casting_player.health < 14:
        casting_player.health += 2
        restored = casting_player.name + ": Restored 2 hp, "

    elif casting_player.health == 14:
        casting_player.health += 1
        restored = casting_player.name + ": Restored 1 hp, "

    else:
        return "Cure wasted: nothing to cure on " + casting_player.name

    casting_player.effects["disease"] = False
    restored += "Disease effect removed"
    return restored

# Damaging:


def missile(casting_player, other_player):
    """Missile spell"""
    chosen_player = check_magic_mirror(casting_player, other_player)

    if "Shield" not in chosen_player.spell_to_cast \
            and "Protection From Evil" not in chosen_player.spell_to_cast\
            and not check_counter_spell(other_player) \
            and not check_dispel_magic(other_player):
        chosen_player.health -= 1
        return "Missile succesfully hit " + chosen_player.name

    else:
        return "Missile thwarted"


def finger_of_death(casting_player, other_player):
    """Finger of Death spell"""
    chosen_player = check_magic_mirror(casting_player, other_player)

    if not check_dispel_magic(chosen_player):
        chosen_player.health = 0
        return "Wizard " + chosen_player.name + \
            " got brutally fingered and died in a very painful way..."
    return "Finger of Death could not be casted on " + chosen_player.name


def lightning_bolt(casting_player, other_player):
    """Lightning Bolt spell"""
    chosen_player = check_magic_mirror(casting_player, other_player)
    if not check_dispel_magic(chosen_player):
        chosen_player.health -= 5
        return chosen_player.name + "received 5 damage from enemy wizard"
    return "Lightning Bolt could not be casted on " + chosen_player.name


def cause_light_wounds(casting_player, other_player):
    """Cause Light Wounds spell"""
    chosen_player = check_magic_mirror(casting_player, other_player)
    if not check_dispel_magic(chosen_player):
        chosen_player.health -= 2
        return chosen_player.name + "received 2 damage from enemy wizard"
    return "Cause Light Wounds could not be casted on " + chosen_player.name


def cause_heavy_wounds(casting_player, other_player):
    """Cause Heavy Wounds spell"""
    chosen_player = check_magic_mirror(casting_player, other_player)
    if not check_dispel_magic(chosen_player):
        chosen_player.health -= 3
        return chosen_player.name + "received 3 damage from enemy wizard"
    return "Cause Heavy Wounds could not be casted on " + chosen_player.name


def fireball(casting_player, other_player):
    """Fireball spell"""
    chosen_player = check_magic_mirror(casting_player, other_player)
    if not check_dispel_magic(chosen_player) \
            and "Ice Storm" not in chosen_player.spell_to_cast:
        chosen_player.health -= 5
        return chosen_player.name + "received 5 damage from enemy wizard"
    return "Fireball could not be casted on " + chosen_player.name


def fire_storm(casting_player, other_player):
    """Fire Storm spell"""
    if not check_dispel_magic(other_player) and "Ice Storm" not in other_player.spell_to_cast:
        if not check_counter_spell(other_player):
            other_player.health -= 5

        casting_player.health -= 5
        return "Fire Storm casted by " + casting_player.name

    else:
        return "Fire Storm nullified"


def ice_storm(casting_player, other_player):
    """Ice Storm spell"""
    if not check_dispel_magic(other_player) and "Fire Storm" not in other_player.spell_to_cast:
        if not check_counter_spell(other_player):
            other_player.health -= 5
            # casting_player only gets damage if enemy doesnt have fireball
        if "Fireball" not in other_player.spell_to_cast:
            casting_player.health -= 5
        return "Ice Storm casted by " + casting_player.name

    else:
        return "Ice Storm nullified"

# Enchantment:


def amnesia(casting_player, other_player):
    """Amnesia spell"""
    pass


def confusion(casting_player, other_player):
    """Confusion spell"""
    pass


def charm_person(casting_player, other_playe):
    """Charm Person spell"""
    pass


def paralysis(casting_player, other_player):
    """Paralysis spell"""
    pass


def fear(casting_player, other_player):
    """Fear spell"""
    pass


def anti_spell(casting_player, other_player):
    """Anti-spell spell"""
    pass


def protection_from_evil(casting_player, other_player):
    """Protection From Evil spell"""
    chosen_player = check_magic_mirror(casting_player, other_player)
    chosen_player.effects["protection_from_evil"] = 3
    return "Protection From Evil casted on " + chosen_player.name


def resist_heat(casting_player, other_player):
    """Resist Heat spell"""
    chosen_player = check_magic_mirror(casting_player, other_player)
    chosen_player.effects["resist_heat"] = True
    return "Resist Heat casted on " + chosen_player.name


def resist_cold(casting_player, other_player):
    """Resist Cold spell"""
    chosen_player = check_magic_mirror(casting_player, other_player)
    chosen_player.effects["resist_cold"] = True
    return "Resist Cold casted on " + chosen_player.name


def disease(casting_player, other_player):
    """Disease spell"""
    chosen_player = check_magic_mirror(casting_player, other_player)

    if "Remove Enchantment" not in chosen_player.spell_to_cast \
            and not check_dispel_magic(chosen_player) \
            and "Cure Heavy Wounds" not in chosen_player.spell_to_cast:

        chosen_player.effects["disease"] = 7
        return "Disease given to " + chosen_player.name + ". Death is coming..."
    return "Disease casted on " + chosen_player.name


def poison(casting_player, other_player):
    """Poison spell"""
    chosen_player = check_magic_mirror(casting_player, other_player)

    if "Remove Enchantment" not in chosen_player.spell_to_cast \
            and not check_dispel_magic(chosen_player):

        chosen_player.effects["poison"] = 7
        return "Poison given to " + chosen_player.name + ". Death will be slow and painful..."
    return "Poison casted on " + chosen_player.name


def blindness(casting_player, other_player):
    """Blindness spell"""
    pass


def invisibility(casting_player, other_player):
    """Invisibility spell"""
    chosen_player = check_magic_mirror(casting_player, other_player)
    if not check_dispel_magic(chosen_player) \
            and not check_counter_spell(chosen_player):

        chosen_player.effects["invisible"] = True
        return chosen_player.name + " became invisible"


def haste(casting_player, other_player):
    """Haste spell"""
    pass


def time_stop(casting_player, other_player):
    """Time Stop spell"""
    pass


def delayed_effect(casting_player, other_player):
    """Delayed Effect spell"""
    pass


def permanency(casting_player, other_player):
    """Permanency spell"""
    pass


# Non-spells


def stab(casting_player, other_player):
    """Stab no-spell"""
    if "Shield" not in other_player.spell_to_cast \
            and "Protection From Evil" not in other_player.spell_to_cast \
            and not check_counter_spell(other_player) \
            and not check_dispel_magic(other_player):

        other_player.health -= 1
        return casting_player.name + " stabbed " + other_player.name
    return casting_player.name + " could not stab " + other_player.name


def nothing(casting_player, other_player):
    """Nothing no-spell"""
    return casting_player.name + " did nothing"


def surrender(casting_player, other_player):
    """Surrender no-spell"""
    casting_player.effects["surrender"] = True
    return casting_player.name + " surrendered."


EFFECT_DICT = {
    # effects:
    "disease": 0,
    "surrender": False,
    "invisible": False,
    "protection_from_evil": 0,
    "resist_heat": False,
    "resist_cold": False,
    "poison": 0
}

SPELL_DATA = [
    # Protection:
    ("Shield", "P", shield),
    ("Remove Enchantment", "PDWP", remove_enchantment),
    ("Magic Mirror", "C(w", magic_mirror),
    ("Counter Spell", "WPP", counter_spell),
    ("Dispel Magic", "CDPW", dispel_magic),
    ("Raise Dead", "D-W-W-F-W-C", raise_dead),
    ("Cure Light Wounds", "DFW", cure_light_wounds),
    ("Cure Heavy Wounds", "DFPW", cure_heavy_wounds),

    # Damaging:
    ("Missile", "SD", missile),
    ("Finger of Death", "PWPFSSSD", finger_of_death),
    ("Lightning Bolt", "DFFDD", lightning_bolt),
    ("Cause Light Wounds", "WFP", cause_light_wounds),
    ("Cause Heavy Wounds", "WPFD", cause_heavy_wounds),
    ("Fireball", "FSSDD", fireball),
    ("Fire Storm", "SWWC", fire_storm),
    ("Ice Storm", "WSSC", ice_storm),

    # Enchantment:
    ("Amnesia", "DPP", amnesia),
    ("Confusion", "DSF", confusion),
    ("Charm Person", "PSDF", charm_person),
    ("Paralysis", "FFF", paralysis),
    ("Fear", "SWD", fear),
    ("Anti-spell", "SPF", anti_spell),
    ("Protection From Evil", "WWP", protection_from_evil),
    ("Resist Heat", "WWFP", resist_heat),
    ("Resist Cold", "SSFP", resist_cold),
    ("Disease", "DSFFFC", disease),
    ("Poison", "DWWFWD", poison),
    ("Blindness", "DWFF(d", blindness),
    ("Invisibility", "PP(w(s", invisibility),
    ("Haste", "PWPWWC", haste),
    ("Time Stop", "SPPC", time_stop),
    ("Delayed Effect", "DWSSSP", delayed_effect),
    ("Permanency", "SPFPSDW", permanency),

    # Non-spells
    ("Stab", "stab", stab),
    ("Nothing", " ", nothing),
    ("Surrender", "(p", surrender),
]
