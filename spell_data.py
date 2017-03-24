"""
    spell data list and spell effect dictionary
    by night5word and grammar_naz1
"""

from protection_spells import *
from damaging_spells import *
from enchantment_spells import *
from non_spells import *

MAX_GESTURE_LENGTH = 8

EFFECT_DICT = {
    "amnesia": False,
    "confusion": False,
    "charm_person": False,
    "paralysis": False,
    "fear": False,
    # Anti-spell to be implemented
    "protection_from_evil": 0,
    "resist_heat": False,
    "resist_cold": False,
    "disease": 0,
    "poison": 0,
    "blindness": 0,
    "invisible": False,
    "haste": 0,
    # Time Stop to be implemented
    "delayed_effect": 0,
    "permanency": 0,
    # Non-enchantments:
    "surrender": False,
    "raise_dead": False,
}

SPELL_DATA = [
    # Protection:
    ("Shield", "P", shield),
    ("Remove Enchantment", "PDWP", remove_enchantment),
    ("Magic Mirror", "C(w", magic_mirror),
    ("Counter Spell", "WPP", counter_spell),
    ("Dispel Magic", "CDPW", dispel_magic),
    ("Raise Dead", "DWWFWC", raise_dead),
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
    # Anti-spell to be implemented
    ("Protection From Evil", "WWP", protection_from_evil),
    ("Resist Heat", "WWFP", resist_heat),
    ("Resist Cold", "SSFP", resist_cold),
    ("Disease", "DSFFFC", disease),
    ("Poison", "DWWFWD", poison),
    ("Blindness", "DWFF(d", blindness),
    ("Invisibility", "PP(w(s", invisibility),
    ("Haste", "PWPWWC", haste),
    # Time Stop to be implemented
    ("Delayed Effect", "DWSSSP", delayed_effect),
    ("Permanency", "SPFPSDW", permanency),

    # Non-spells
    ("Stab", "stab", stab),
    ("Nothing", " ", nothing),
    ("Surrender", "(p", surrender),
]
