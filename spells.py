"""
    spell functions and dictionary and effect dictionary
    by night5word and grammar_naz1
"""


def choose_target(casting_player, other_player):
    """prompt player to choose target, returns the target and non target player in a tuple"""
    while True:
        answer = input(casting_player.name +
                       ": Choose your target: s = self, o = opponent\n").lower()
        if answer == "s":
            return check_reflection(casting_player, other_player)
        elif answer == "o":
            return check_reflection(other_player, casting_player)


def check_reflection(target_player, non_target_player):
    """returns the tharget and non target players in a tuple"""
    if not check_counter_spell(non_target_player) and not check_dispel_magic(non_target_player):
        if "Magic Mirror" in target_player.spell_to_cast:
            # magic mirror effective, reflection happened
            return non_target_player, target_player
    # no reflection happened
    return target_player, non_target_player


def choose_hand(non_target_player, target_player, spell_name):
    """prompts the player to choose one of the hands of the other player to be affected"""
    while True:
        hand = input(non_target_player.name + " choose which hand of " +
                     target_player.name + " do you want to affect with" + spell_name + " spell! (l/r)\n").lower()
        if hand == "l" or hand == "r":
            target_player.affected_hand = hand
            return


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


# Protection:


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
    """gestures D-W-W-F-W-C. The subject of this spell is usually a recently-dead (not yet decomposing) human corpse
    though it may be used on a dead monster. When the spell is cast, life returns to the corpse and all damage is cured.
    All enchantments are also removed (as per the spell) so any diseases or poisons will be neutralized and all other
    enchantments removed. If swords, knives, or other implements of destruction still remain in the corpse when it is
    raised, they will of course cause it damage as usual. The subject will be able to act normally immediately after the
    spell is cast. On the turn a monster is raised it may attack. Wizards may begin gesturing on the turn following
    their return from the dead. This is the only spell which affects corpses. It therefore cannot be stopped by a
    counter-spell. A dispel magic spell will prevent its effect, since dispel magic affects all spells no matter what
    their subject. If the spell is cast on a live individual, the effect is that of a cure light wounds recovering five
    points of damage, or as many as have been sustained if less than five. Note that any diseases the live subject might
    have are not cured."""
    pass  # TODO: implement


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

# Damaging:


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

# Enchantment:


def amnesia(casting_player, other_player):  # Only reflectable

    """gestures D-P-P. If the subject of this spell is a wizard, next turn he must repeat
    identically the gestures he made in the current turn, including stabs. If the subject is a
    monster it will attack whoever it attacked this turn. If the subject is simultaneously the
    subject of any of confusion, charm person, charm monster, paralysis or fear then none of
    the spells work."""
    targeted_player, _ = check_reflection(casting_player, other_player)
    if not check_remove_enchantment(targeted_player) \
            and not check_dispel_magic(targeted_player) \
            and not check_counter_spell(targeted_player) \
            and not targeted_player.effects["confusion"] \
            and not targeted_player.effects["charm_person"] \
            and not targeted_player.effects["paralysis"] \
            and not targeted_player.effects["fear"]:
        targeted_player.effects["amnesia"] = True
        res = ["Amnesia casted on " + targeted_player.name] * 2
        vis = True
    else:
        res = ["Amnesia could not be casted on " + targeted_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, targeted_player)


def confusion(casting_player, other_player):  # Only reflectable
    """gestures D-S-F. If the subject of this spell is a wizard, next turn he writes down his
    gestures as usual and after exposing them, rolls 2 dice to determine which gesture is
    superseded due to his being confused. The first die indicates left hand on 1-3, right on 4-6.
    The second roll determines what the gesture for that hand shall be replaced with: 1=C, 2=D,
    3=F, 4=P, 5=S, 6=W. If the subject of the spell is a monster, it attacks at random that turn.
    If the subject is also the subject of any of: amnesia, charm person, charm monster, paralysis
    or fear, none of the spells work."""
    targeted_player, _ = check_reflection(casting_player, other_player)
    if not check_remove_enchantment(targeted_player) \
            and not check_dispel_magic(targeted_player) \
            and not check_counter_spell(targeted_player) \
            and not targeted_player.effects["amnesia"] \
            and not targeted_player.effects["charm_person"] \
            and not targeted_player.effects["paralysis"] \
            and not targeted_player.effects["fear"]:
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
            and not target_player.effects["amnesia"] \
            and not target_player.effects["confusion"] \
            and not target_player.effects["paralysis"] \
            and not target_player.effects["fear"]:
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
            and not target_player.effects["amnesia"] \
            and not target_player.effects["confusion"] \
            and not target_player.effects["charm_person"] \
            and not target_player.effects["fear"]:
        target_player.effects["paralysis"] = True
        choose_hand(non_target_player, target_player, "Paralysis")
        res = ["Paralysis casted on " + target_player.name] * 2
        vis = True
    else:
        res = ["Paralysis could not be casted on " + target_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, target_player)


def fear(casting_player, other_player):
    """gestures S-W-D. In the turn following the casting of this spell,
    the subject cannot perform a C, D, F or S gesture. This obviously
    has no effect on monsters. If the subject is also the subject of
    amnesia, confusion, charm person, charm monster or paralysis, then
    none of the spells work."""
    targeted_player, _ = check_reflection(casting_player, other_player)
    if not check_remove_enchantment(targeted_player) \
            and not check_dispel_magic(targeted_player) \
            and not check_counter_spell(targeted_player) \
            and not targeted_player.effects["amnesia"] \
            and not targeted_player.effects["confusion"] \
            and not targeted_player.effects["charm_person"] \
            and not targeted_player.effects["paralysis"]:
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
        other_player.effects["protection_from_evil"] = 3
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
        chosen_player.effects["blindness"] = 3
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
        chosen_player.effects["haste"] = 3
        res = ["Haste casted on " + chosen_player.name] * 2
        vis = True
    else:
        res = ["Haste could not be casted on " + other_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis)


def delayed_effect(casting_player, other_player):
    """gestures D-W-S-S-S-P. This spell only works if cast upon a wizard. The next spell he completes, provided it is on
    this turn or one of the next 3 is "banked" until needed, i.e. it fails to work until its caster desires. This next
    spell which is to be banked does not include the actual spell doing the banking. The spell must be written down to
    be used by its caster at the same time that he writes his gestures. Note that spells banked are those cast by the
    subject not those cast at him. If he casts more than one spell at the same time he chooses which is to be banked.
    Remember that P is a shield spell, and surrender is not a spell. A wizard may only have one spell banked at any one
    time."""
    if not check_remove_enchantment(other_player) \
            and not check_dispel_magic(other_player) \
            and not check_counter_spell(other_player):
        other_player.effects["delayed_effect"] = 3
        res = ["Delayed Effect casted on " + other_player.name] * 2
        vis = True
    else:
        res = ["Delayed Effect could not be casted on " + other_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis)


def permanency(casting_player, other_player):
    """gestures S-P-F-P-S-D-W. This spell only works if cast upon a wizard. The next spell he completes, provided it is
    on this turn or one of the next 3, and which falls into the category of "Enchantments" (except anti-spell, disease,
    poison, or time-stop) will have its effect made permanent. This means that the effect of the extended spell on the
    first turn of its duration is repeated eternally. For example, a confusion spell will be the same gesture rather
    than re-rolling the dice, a charm person will mean repetition of the chosen gesture, etc. If the subject of the
    permanency casts more than one spell at the same time eligible for permanency, he chooses which has its duration
    extended. Note that the person who has his spell made permanent does not necessarily have to make himself the
    subject of the spell. A permanency spell cannot increase its own duration, nor the duration of spells saved by a
    delayed effect (so if both a permanency and delayed effect are eligible for the same spell to be banked or extended,
    a choice must be made, the losing spell being neutralized and working on the next spell instead)."""
    chosen_player = check_reflection(casting_player, other_player)
    if not check_remove_enchantment(chosen_player) \
            and not check_dispel_magic(chosen_player) \
            and not check_counter_spell(chosen_player):
        chosen_player.effects["permanency"] = 3
        res = ["Permanency casted on " + chosen_player.name] * 2
        vis = True
    else:
        res = ["Permanency could not be casted on " + chosen_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, chosen_player)


# Non-spells


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


EFFECT_DICT = {
    # effects:
    "disease": 0,
    "invisible": False,
    "protection_from_evil": 0,
    "resist_heat": False,
    "resist_cold": False,
    "poison": 0,
    # new effects:
    "fear": False,
    "paralysis": False,
    "confusion": False,
    "amnesia": False,
    "permanency": 0,
    "delayed_effect": 0,
    "blindness": 0,
    "haste": 0,
    "time_stop": False,
    "surrender": False,
    "raise_dead": False
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
