"""
    spell functions and dictionary and effect dictionary
    by night5word and grammar_naz1
"""
def choose_target(casting_player, other_player):
    answer = input("Choose your target: s = self, o = opponent")
    return casting_player

#Protection:
def shield(casting_player, other_player):
    """shield spell"""

def remove_enchantment(casting_player, other_player):
    """Remove Enchantment spell"""
    target = choose_target(casting_player, other_player)

def magic_mirror(casting_player, other_player):
    """magic mirror spell"""

def counter_spell(casting_player, other_player):
    """counter_spell spell"""

def dispel_magic(casting_player, other_player):
    """dispel_magic spell"""

def cure_light_wounds(casting_player, other_player):
    """cure_light_wounds spell"""
    
def cure_heavy_wounds(casting_player, other_player):
    """cure_heavy_wounds spell"""

#Damaging:
def missile(casting_player, other_player):
    """missile spell"""

def finger_of_death(casting_player, other_player):
    """finger_of_death spell"""

def lightning_bolt(casting_player, other_player):
    """lightning_bolt spell"""

def cause_light_wounds(casting_player, other_player):
    """cause_light_wounds spell"""

def cause_heavy_wounds(casting_player, other_player):
    """cause_heavy_wounds spell"""

def fireball(casting_player, other_player):
    """fireball spell"""

def fire_storm(casting_player, other_player):
    """fire_storm spell"""

def ice_storm(casting_player, other_player):
    """ice_storm spell"""

#Enchantment:  
def amnesia(casting_player, other_player):
    """amnesia spell"""

def confusion(casting_player, other_player):
    """confusion spell"""

def charm(casting_player, other_player):
    """charm spell"""

def paralysis(casting_player, other_player):
    """paralysis spell"""

def fear(casting_player, other_player):
    """fear spell"""

def anti_spell(casting_player, other_player):
    """anti_spell spell"""

def protection_from_evil(casting_player, other_player):
    """protection_from_evil spell"""

def resist_heat(casting_player, other_player):
    """resist_heat spell"""

def resist_cold(casting_player, other_player):
    """resist_cold spell"""

def disease(casting_player, other_player):
    """disease spell"""

def poison(casting_player, other_player):
    """poison spell"""

def invisibility(casting_player, other_player):
    """invisibility spell"""
    
def time_stop(casting_player, other_player):
    """time_stop spell"""

def delayed_effect(casting_player, other_player):
    """delayed_effect spell"""

def permanency(casting_player, other_player):
    """permanency spell"""

#Non-spells
def stab(casting_player, other_player):
    """stab no-spell"""
    
def nothing(casting_player, other_player):
    """nothing no-spell"""
def surrender(casting_player, other_player):
    """surrender spell"""

GESTURE_DICT = {
    #Protection:
    "P": "Shield",
    "PDWP": "Remove Enchantment",
    "C(w": "Magic Mirror",
    "WPP": "Counter-Spell",
    "CDPW": "Dispel Magic",
    "DFW": "Cure Light Wounds",
    "DFPW": "Cure Heavy Wounds",
    
    #Damaging:
    "SD":       "Missile",
    "PWPFSSSD": "Finger of Death",
    "DFFDD":    "Lightning Bolt",
    "WFP":      "Cause Light Wounds",
    "WPFD":     "Cause Heavy Wounds",
    "FSSDD":    "Fireball",
    "SWWC":     "Fire Storm",
    "WSSC":     "Ice Storm",

    #Enchantment:
    "DPP":      "Amnesia",
    "DSF":      "Confusion",
    "PSDF":     "Charm", #Charm person is the original name
    "FFF":      "Paralysis",
    "SWD":      "Fear",
    "SPF":      "Anti-Spell",
    "WWP":      "Protection From Evil",
    "WWFP":     "Resist Heat",
    "SSFP":     "Resist Cold",
    "DSFFFC":   "Disease",
    "DWWFWD":   "Poison",
    "PP(w(s":   "Invisibility",
    "SPPC":     "Time Stop",
    "DWSSSP":   "Delayed Effect",
    "SPFPSDW":  "Permanency",

    #Non-spells
    "stab":     "Stab",
    " ":        "Nothing",
    "(p":       "Surrender"
    }
SPELL_DICT = {
    #Protection:
    "Shield": shield,
    "Remove Enchantment": remove_enchantment,
    "Magic Mirror": magic_mirror,
    "Counter-Spell": counter_spell,
    "Dispel Magic": dispel_magic,
    "Cure Light Wounds": cure_light_wounds,
    "Cure Heavy Wounds": cure_heavy_wounds,

    #Damaging:
    "Missile": missile,
    "Finger of Death": finger_of_death,
    "Lightning Bolt": lightning_bolt,
    "Cause Light Wounds": cause_light_wounds,
    "Cause Heavy Wounds": cause_heavy_wounds,
    "Fireball": fireball,
    "Fire Storm": fire_storm,
    "Ice Storm": ice_storm,

    #Enchantment:
    "Amnesia": amnesia,
    "Confusion": confusion,
    "Charm": charm,
    "Paralysis": paralysis,
    "Fear": fear,
    "Anti-Spell": anti_spell,
    "Protection From Evil": protection_from_evil,
    "Resist Heat": resist_heat,
    "Resist Cold": resist_cold,
    "Disease": disease,
    "Poison": poison,
    "Invisibility": invisibility,
    "Time Stop": time_stop,
    "Delayed Effect": delayed_effect,
    "Permanency": permanency,

    #Non-spells
    "Stab": stab,
    "Nothing": nothing,
    "Surrender": surrender

    }
EFFECT_DICT = {
    "surrender": False,
    "invisible": 0
    }
