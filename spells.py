"""
    spell functions and dictionary and effect dictionary
    by night5word and grammar_naz1
"""
def choose_target(casting_player, other_player):
    while True:
        answer = input("Choose your target: s = self, o = opponent\n").lower()
        if answer == "s":
            return casting_player
        elif answer == "o":
            return other_player

#Protection:
def shield(casting_player, other_player):
    """shield spell"""
    print("Shield activated")

def remove_enchantment(casting_player, other_player):
    """Remove Enchantment spell"""
    if "Counter-Spell" not in other_player.spell_to_cast \
        and "Cure Light Wounds" not in other_player.spell_to_cast:
        casting_player.effects["invisible"] = 0
        casting_player.effects["confusion"] = False
        casting_player.effects["charm"] = False
        casting_player.effects["fear"] = False
        casting_player.effects["anti_spell"] = False
        casting_player.effects["protection_from_evil"] = False
        casting_player.effects["resist_heat"] = False
        casting_player.effects["resist_cold"] = False
        casting_player.effects["disease"] = False
        casting_player.effects["poison"] = False
        casting_player.effects["time_stop"] = False
        casting_player.effects["permanency"] = False
        print("Effects and enchantments are removed from " + casting_player.name)

def magic_mirror(casting_player, other_player):
    """magic mirror spell"""
    if "Counter-Spell" not in other_player.spell_to_cast \ 
        and "Dispel Magic" not in other_player.spell_to_cast \
        and "Fire Storm" not in other_player.spell_to_cast \
        and "Ice Storm" not in other_player.spell_to_cast:

        print("Magic Mirror used")

def counter_spell(casting_player, other_player):
    """counter_spell spell"""
    if "Dispel Magic" not in other_player.spell_to_cast \
        and "Finger of Death" not in other_player.spell_to_cast:

        print("Counter Spell used")

def dispel_magic(casting_player, other_player):
    """dispel_magic spell"""
    if "Surrender" not in other_player.spell_to_cast \
        and "Stab" not in other_player.spell_to_cast \
        and "Cure Light Wounds" not in other_player.spell_to_cast:
        casting_player.effects["invisible"] = 0
        casting_player.effects["confusion"] = False
        casting_player.effects["charm"] = False
        casting_player.effects["fear"] = False
        casting_player.effects["anti_spell"] = False
        casting_player.effects["protection_from_evil"] = False
        casting_player.effects["resist_heat"] = False
        casting_player.effects["resist_cold"] = False
        casting_player.effects["disease"] = False
        casting_player.effects["poison"] = False
        casting_player.effects["time_stop"] = False
        casting_player.effects["permanency"] = False

        other_player.effects["invisible"] = 0
        other_player.effects["confusion"] = False
        other_player.effects["charm"] = False
        other_player.effects["fear"] = False
        other_player.effects["anti_spell"] = False
        other_player.effects["protection_from_evil"] = False
        other_player.effects["resist_heat"] = False
        other_player.effects["resist_cold"] = False
        other_player.effects["disease"] = False
        other_player.effects["poison"] = False
        other_player.effects["time_stop"] = False
        other_player.effects["permanency"] = False
        #TODO act like a Shield too (put Shield in spell_to_cast?)
        print("Dispel Magic used")

def cure_light_wounds(casting_player, other_player):
    """cure_light_wounds spell"""
    if casting_player.effects["received_damage"] != 0 and casting_player.health < 15:
        casting_player.health += 1
        print("Restored 1 hp")

    else:
        print("Cure wasted: nothing to cure")
   
def cure_heavy_wounds(casting_player, other_player):
    """cure_heavy_wounds spell"""
    if casting_player.effects["received_damage"] != 0 and casting_player.health < 15:
        if casting_player.effects["received_damage"] == 1
            casting_player.health += 1
            print("Restored 1 hp")
        else:
            casting_player.health += 2
            print("Restored 2 hp")

    else:       
        print("Cure wasted: nothing to cure")

    casting_player.effects["disease"] = False
    print("Disease and poison effect removed")
        
#Damaging:
def missile(casting_player, other_player):
    """missile spell"""
    if "Magic Mirror" in other_player.spell_to_cast:
        chosen_player = casting_player
    else:
        chosen_player = other_player

    if "Shield" not in chosen_player.spell_to_cast \
    and "Counter-Spell" not in chosen_player.spell_to_cast \
    and "Dispel Magic" not in chosen_player.spell_to_cast:

        chosen_player.effects["received_damage"] = 1
        chosen_player.health -= 1
        chosen_player.effects["did_receive_damage"] = True
        print("Missile hit")  

    else:
        print("Missile thwarted")

def finger_of_death(casting_player, other_player):
    """finger_of_death spell"""
    if "Magic Mirror" in other_player.spell_to_cast:
        chosen_player = casting_player
    else:
        chosen_player = other_player

    if "Dispel Magic" not in chosen_player.spell_to_cast \
        and "Anti-Spell" not in chosen_player.spell_to_cast:
        
        chosen_player.effects["did_receive_damage"] = True
        chosen_player.effects["received_damage"] = 15

def lightning_bolt(casting_player, other_player):
    """lightning_bolt spell"""
    if "Magic Mirror" in other_player.spell_to_cast:
        chosen_player = casting_player
    else:
        chosen_player = other_player
        
    chosen_player.effects["did_receive_damage"] = True
    chosen_player.effects["received_damage"] = 5

def cause_light_wounds(casting_player, other_player):
    """cause_light_wounds spell"""
    if "Magic Mirror" in other_player.spell_to_cast:
        chosen_player = casting_player
    else:
        chosen_player = other_player
        
    chosen_player.effects["did_receive_damage"] = True
    chosen_player.effects["received_damage"] = 2

def cause_heavy_wounds(casting_player, other_player):
    """cause_heavy_wounds spell"""
    if "Magic Mirror" in other_player.spell_to_cast:
        chosen_player = casting_player
    else:
        chosen_player = other_player
        
    chosen_player.effects["did_receive_damage"] = True
    chosen_player.effects["received_damage"] = 3

def fireball(casting_player, other_player):
    """fireball spell"""
    if "Magic Mirror" in other_player.spell_to_cast:
        chosen_player = casting_player
    else:
        chosen_player = other_player
        
    chosen_player.effects["did_receive_damage"] = True
    chosen_player.effects["received_damage"] = 5

def fire_storm(casting_player, other_player):
    """fire_storm spell"""
    other_player.effects["did_receive_damage"] = True
    other_player.effects["received_damage"] = 5

def ice_storm(casting_player, other_player):
    """ice_storm spell"""
    other_player.effects["did_receive_damage"] = True
    other_player.effects["received_damage"] = 5

#Enchantment:  
def confusion(casting_player, other_player):
    """confusion spell"""
    if "Magic Mirror" in other_player.spell_to_cast:
        chosen_player = casting_player
    else:
        chosen_player = other_player
        
def charm(casting_player, other_player):
    """charm spell"""
    if "Magic Mirror" in other_player.spell_to_cast:
        chosen_player = casting_player
    else:
        chosen_player = other_player
        
def paralysis(casting_player, other_player):
    """paralysis spell"""
    if "Magic Mirror" in other_player.spell_to_cast:
        chosen_player = casting_player
    else:
        chosen_player = other_player
        
def fear(casting_player, other_player):
    """fear spell"""
    if "Magic Mirror" in other_player.spell_to_cast:
        chosen_player = casting_player
    else:
        chosen_player = other_player
        
    chosen_player.effects["fear"] = True
    print("Fear induced. Next round will be limited...")
    
    

def anti_spell(casting_player, other_player):
    """anti_spell spell"""
    if "Magic Mirror" in other_player.spell_to_cast:
        chosen_player = casting_player
    else:
        chosen_player = other_player


def protection_from_evil(casting_player, other_player):
    """protection_from_evil spell"""
    if "Magic Mirror" in other_player.spell_to_cast:
        chosen_player = casting_player
    else:
        chosen_player = other_player


def resist_heat(casting_player, other_player):
    """resist_heat spell"""
    if "Magic Mirror" in other_player.spell_to_cast:
        chosen_player = casting_player
    else:
        chosen_player = other_player


def resist_cold(casting_player, other_player):
    """resist_cold spell"""
    if "Magic Mirror" in other_player.spell_to_cast:
        chosen_player = casting_player
    else:
        chosen_player = other_player
       

def disease(casting_player, other_player):
    """disease spell"""
    if "Magic Mirror" in other_player.spell_to_cast:
        chosen_player = casting_player
    else:
        chosen_player = other_player

    if "Remove Enchantment" not in other_player.spell_to_cast \
        and "Cure Heavy Wounds" not in other_player.spell_to_cast \
        and "Dispel Magic" not in other_player.spell_to_cast:

        chosen_player.effects["disease"] = 6 #TODO really 6?
        print("Disease given. Death is coming...")
       
def poison(casting_player, other_player):
    """poison spell"""
    if "Magic Mirror" in other_player.spell_to_cast:
        chosen_player = casting_player
    else:
        chosen_player = other_player

    if "Remove Enchantment" not in other_player.spell_to_cast \
        and "Dispel Magic" not in other_player.spell_to_cast:
    
        chosen_player.effects["disease"] = 6 #TODO really 6?
        print("Poison given. Death will be slow and painful...")
       
def invisibility(casting_player, other_player):
    """invisibility spell"""
    if "Magic Mirror" in other_player.spell_to_cast:
        chosen_player = casting_player
    else:
        chosen_player = other_player
    #TODO what counters and/or stops this spell?
    chosen_player.effects["invisible"] = 3 #TODO really 3?
    print("Invisibility started")

    
def time_stop(casting_player, other_player):
    """time_stop spell"""
    print("Time Stop")

def permanency(casting_player, other_player):
    """permanency spell"""

#Non-spells
def stab(casting_player, other_player):
    """stab no-spell"""
    if "Shield" not in other_player.spell_to_cast
        other_player.health -= 1
        casting_player.effects["stab_used"] = True #TODO is this needed? can only stab once in a turn
    
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
    #checks:
    "did_receive_damage": False,
    "received_damage": 0,

    #effects:
    "disease": 0,
    "surrender": False,
    "invisible": 0,
    "confusion": False,
    "charm": False,
    "paralysis": False,
    "fear": False,
    "anti_spell": False,
    "protection_from_evil": False,
    "resist_heat": False,
    "resist_cold": False,
    "disease": False,
    "poison": False,
    "time_stop": False,
    "permanency": False
    }
