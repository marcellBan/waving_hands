"""
    spell functions and dictionary and effect dictionary
    by night5word and grammar_naz1
"""


def choose_target(casting_player, other_player):
    """prompt player to choose target"""
    while True:
        answer = input(casting_player.name + ": Choose your target: s = self, o = opponent\n").lower()
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
    if "Counter-Spell" in player.spell_to_cast:
        return True
    else:
        return False

def check_dispel_magic(player):
    if "Dispel Magic" in player.spell_to_cast:
        return True
    else:
        return False

# Protection:
def shield(casting_player, other_player):
    """shield spell"""
    return casting_player.name + ": Shield activated"


def remove_enchantment(casting_player, other_player):
    """Remove Enchantment spell"""
    chosen_player = check_magic_mirror(casting_player, other_player)
    if not check_counter_spell(chosen_player): #TODO untested

        casting_player.effects["invisible"] = False
        casting_player.effects["protection_from_evil"] = 0
        casting_player.effects["resist_heat"] = False
        casting_player.effects["resist_cold"] = False
        casting_player.effects["disease"] = False
        casting_player.effects["poison"] = False
        return "Effects and enchantments are removed from: " + chosen_player.name
    return "Effects and enchantments could no be removed from: " + chosen_player.name

def magic_mirror(casting_player, other_player):
    """magic mirror spell"""
    if not check_counter_spell(other_player) \
            and not check_dispel_magic(other_player) \
            and "Fire Storm" not in other_player.spell_to_cast \
            and "Ice Storm" not in other_player.spell_to_cast:

        return casting_player.name + ": Magic Mirror used"


def counter_spell(casting_player, other_player):
    """counter_spell spell"""
    if not check_dispel_magic(other_player) \
        and "Finger of Death" not in other_player.spell_to_cast:
        return casting_player.name + ": Counter Spell used"
    return "Counter spell could no be casted from: " + casting_player.name


def dispel_magic(casting_player, other_player):
    """dispel_magic spell"""
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
        # TODO act like a Shield too (put Shield in spell_to_cast?)
        return casting_player.name + ": Dispel Magic used"
    return "Dispel Magic could not be casted from: " + casting_player.name

def cure_light_wounds(casting_player, other_player):
    """cure_light_wounds spell"""
    if casting_player.health < 15:
        casting_player.health += 1
        return casting_player.name + ": Restored 1 hp"

    else:
        return "Cure wasted: nothing to cure on " + casting_player.name

def cure_heavy_wounds(casting_player, other_player):
    """cure_heavy_wounds spell"""
    if casting_player.health < 14:
        casting_player.health += 2
        restored = casting_player.name + ": Restored 2 hp, "

    elif casting_player.health == 14:
        casting_player.health += 1
        restored = casting_player.name + ": Restored 1 hp"

    else:
        return "Cure wasted: nothing to cure on " + casting_player.name

    casting_player.effects["disease"] = False
    restored += "Disease effect removed"
    return restored

# Damaging:
def missile(casting_player, other_player):
    """missile spell"""
    chosen_player = check_magic_mirror(casting_player, other_player)

    if "Shield" not in chosen_player.spell_to_cast \
        and "Protection From Evil" not in chosen_player.spell_to_cast\
        and not check_counter_spell(casting_player) \
        and not check_dispel_magic(casting_player):
        
        chosen_player.health -= 1
        return "Missile succesfully hit " + chosen_player.name

    else:
        return "Missile thwarted"


def finger_of_death(casting_player, other_player):
    """finger_of_death spell"""
    chosen_player = check_magic_mirror(casting_player, other_player)

    if not check_dispel_magic(chosen_player):
        chosen_player.health = 0
        return "Wizard " + chosen_player.name + " got brutally fingered and died in a very painful way..."
    return "Finger of Death could not be casted on " + chosen_player.name

def lightning_bolt(casting_player, other_player):
    """lightning_bolt spell"""
    chosen_player = check_magic_mirror(casting_player, other_player)
    if not check_dispel_magic(chosen_player):
        chosen_player.health -= 5
        return chosen_player.name + "received 5 damage from enemy wizard"
    return "Lightning Bolt could not be casted on " + chosen_player.name

def cause_light_wounds(casting_player, other_player):
    """cause_light_wounds spell"""
    chosen_player = check_magic_mirror(casting_player, other_player)
    if not check_dispel_magic(chosen_player):
        chosen_player.health -= 2
        return chosen_player.name + "received 2 damage from enemy wizard"
    return "Cause Light Wounds could not be casted on " + chosen_player.name

def cause_heavy_wounds(casting_player, other_player):
    """cause_heavy_wounds spell"""
    chosen_player = check_magic_mirror(casting_player, other_player)
    if not check_dispel_magic(chosen_player):
        chosen_player.health -= 3
        return chosen_player.name + "received 3 damage from enemy wizard"
    return "Cause Heavy Wounds could not be casted on " + chosen_player.name

def fireball(casting_player, other_player):
    """fireball spell"""
    chosen_player = check_magic_mirror(casting_player, other_player)
    if not check_dispel_magic(chosen_player):
        chosen_player.health -= 5
        return chosen_player.name + "received 5 damage from enemy wizard"
    return "Fireball could not be casted on " + chosen_player.name

def fire_storm(casting_player, other_player):
    """fire_storm spell"""
    if not check_dispel_magic(other_player) and "Ice Storm" not in other_player.spell_to_cast:
        if not check_counter_spell(other_player):
            other_player.health -= 5
            
        casting_player.health -= 5
        return "Fire Storm casted by " + casting_player.name

    else:
        return "Fire Storm nullified"

def ice_storm(casting_player, other_player): #TODO fireball counters it partially
    """ice_storm spell"""
    if not check_dispel_magic(other_player) and "Fire Storm" not in other_player.spell_to_cast:
        if not check_counter_spell(other_player):
            other_player.health -= 5
            
        casting_player.health -= 5
        return "Ice Storm casted by " + casting_player.name

    else:
        return "Ice Storm nullified"

# Enchantment:
def protection_from_evil(casting_player, other_player):
    """protection_from_evil spell"""
    chosen_player = check_magic_mirror(casting_player, other_player)
    chosen_player.effects["protection_from_evil"] = 3
    return "Protection From Evil casted on " + chosen_player.name

def resist_heat(casting_player, other_player):
    """resist_heat spell"""
    chosen_player = check_magic_mirror(casting_player, other_player)
    return "Resist Heat casted on " + chosen_player.name

def resist_cold(casting_player, other_player):
    """resist_cold spell"""
    chosen_player = check_magic_mirror(casting_player, other_player)
    return "Resist Cold casted on " + chosen_player.name

def disease(casting_player, other_player):
    """disease spell"""
    chosen_player = check_magic_mirror(casting_player, other_player)

    if "Remove Enchantment" not in other_player.spell_to_cast \
            and "Cure Heavy Wounds" not in other_player.spell_to_cast \
            and "Dispel Magic" not in other_player.spell_to_cast:

        chosen_player.effects["disease"] = 6  # TODO really 6?
        print("Disease given. Death is coming...")
    return "Disease casted on " + chosen_player.name

def poison(casting_player, other_player):
    """poison spell"""
    chosen_player = check_magic_mirror(casting_player, other_player)

    if "Remove Enchantment" not in other_player.spell_to_cast \
            and "Dispel Magic" not in other_player.spell_to_cast:

        chosen_player.effects["disease"] = 6  # TODO really 6?
        print("Poison given. Death will be slow and painful...")
    return "Poison casted on " + chosen_player.name

def invisibility(casting_player, other_player):
    """invisibility spell"""
    chosen_player = check_magic_mirror(casting_player, other_player)
    # TODO what counters and/or stops this spell?
    chosen_player.effects["invisible"] = True
    return "Invisibility started on " + chosen_player.name

# Non-spells
def stab(casting_player, other_player):
    """stab no-spell"""
    if "Shield" not in other_player.spell_to_cast \
        and "Protection From Evil" not in other_player.spell_to_cast:

        other_player.health -= 1
        return casting_player.name + " stabbed " + other_player.name
    return casting_player.name + " could not stab " + other_player.name

def nothing(casting_player, other_player):
    """nothing no-spell"""
    return casting_player.name + " did Nothing"

def surrender(casting_player, other_player):
    """surrender spell"""
    return casting_player + " surrendered "

GESTURE_DICT = {
    # Protection:
    "P": "Shield",
    "PDWP": "Remove Enchantment",
    "C(w": "Magic Mirror",
    "WPP": "Counter-Spell",
    "CDPW": "Dispel Magic",
    "DFW": "Cure Light Wounds",
    "DFPW": "Cure Heavy Wounds",

    # Damaging:
    "SD":       "Missile",
    "PWPFSSSD": "Finger of Death",
    "DFFDD":    "Lightning Bolt",
    "WFP":      "Cause Light Wounds",
    "WPFD":     "Cause Heavy Wounds",
    "FSSDD":    "Fireball",
    "SWWC":     "Fire Storm",
    "WSSC":     "Ice Storm",

    # Enchantment:
    "WWP":      "Protection From Evil",
    "WWFP":     "Resist Heat",
    "SSFP":     "Resist Cold",
    "DSFFFC":   "Disease",
    "DWWFWD":   "Poison",
    "PP(w(s":   "Invisibility",

    # Non-spells
    "stab":     "Stab",
    " ":        "Nothing",
    "(p":       "Surrender"
}

SPELL_DICT = {
    # Protection:
    "Shield": shield,
    "Remove Enchantment": remove_enchantment,
    "Magic Mirror": magic_mirror,
    "Counter-Spell": counter_spell,
    "Dispel Magic": dispel_magic,
    "Cure Light Wounds": cure_light_wounds,
    "Cure Heavy Wounds": cure_heavy_wounds,

    # Damaging:
    "Missile": missile,
    "Finger of Death": finger_of_death,
    "Lightning Bolt": lightning_bolt,
    "Cause Light Wounds": cause_light_wounds,
    "Cause Heavy Wounds": cause_heavy_wounds,
    "Fireball": fireball,
    "Fire Storm": fire_storm,
    "Ice Storm": ice_storm,

    # Enchantment:
    "Protection From Evil": protection_from_evil,
    "Resist Heat": resist_heat,
    "Resist Cold": resist_cold,
    "Disease": disease,
    "Poison": poison,
    "Invisibility": invisibility,

    # Non-spells
    "Stab": stab,
    "Nothing": nothing,
    "Surrender": surrender
}

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
