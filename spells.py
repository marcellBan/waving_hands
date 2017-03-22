"""
    spell functions and dictionary and effect dictionary
    by night5word and grammar_naz1
"""


def choose_target_player(casting_player, other_player):
    """returns the target player depending on the existence of magic mirror"""
    if not check_counter_spell(casting_player) and not check_dispel_magic(casting_player):
        if "Magic Mirror" in other_player.spell_to_cast:
            return casting_player
    return other_player


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


def get_visible_results(casting_player, other_player, spell_result, always_visible=False, target_player=None):
    if (casting_player.effects["invisible"] or
            other_player.effects["Blindness"] > 0) \
            and (not always_visible and target_player != other_player):
        spell_result[1] = ""
    if casting_player.effects["Blindness"] > 0 \
            and target_player == other_player:
        spell_result[0] = ""
    return tuple(spell_result)


# Protection:


def shield(casting_player, other_player):
    """Shield spell"""
    res = [casting_player.name + ": Shield activated"] * 2
    return get_visible_results(casting_player, other_player, res)


def remove_enchantment(casting_player, other_player):
    """Remove Enchantment spell"""
    chosen_player = choose_target_player(casting_player, other_player)
    if not check_counter_spell(chosen_player):
        casting_player.effects["invisible"] = False
        casting_player.effects["protection_from_evil"] = 0
        casting_player.effects["resist_heat"] = False
        casting_player.effects["resist_cold"] = False
        casting_player.effects["disease"] = False
        casting_player.effects["poison"] = False
        res = ["Effects and enchantments are removed from: " + chosen_player.name] * 2
        vis = True
    else:
        res = ["Effects and enchantments could no be removed from: " + chosen_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, chosen_player)


def magic_mirror(casting_player, other_player):
    """Magic Mirror spell"""
    if not check_counter_spell(other_player) \
            and not check_dispel_magic(other_player) \
            and "Fire Storm" not in other_player.spell_to_cast \
            and "Ice Storm" not in other_player.spell_to_cast:
        res = [casting_player.name + ": Magic Mirror used"] * 2
    else:
        res = ["Magic Mirror could not be cast by: " + casting_player.name] * 2
    return get_visible_results(casting_player, other_player, res)


def counter_spell(casting_player, other_player):
    """Counter Spell spell"""
    if not check_dispel_magic(other_player):
        res = [casting_player.name + ": Counter Spell used"] * 2
    else:
        res = ["Counter spell could no be casted by " + casting_player.name] * 2
    return get_visible_results(casting_player, other_player, res)


def dispel_magic(casting_player, other_player):
    """Dispel Magic spell"""
    casting_player.effects["invisible"] = False
    casting_player.effects["protection_from_evil"] = 0
    casting_player.effects["resist_heat"] = False
    casting_player.effects["resist_cold"] = False
    casting_player.effects["disease"] = False
    casting_player.effects["poison"] = False
    casting_player.effects["Blindness"] = 0
    # other player
    other_player.effects["invisible"] = False
    other_player.effects["protection_from_evil"] = 0
    other_player.effects["resist_heat"] = False
    other_player.effects["resist_cold"] = False
    other_player.effects["disease"] = False
    other_player.effects["poison"] = False
    other_player.effects["Blindness"] = 0
    res = [casting_player.name + ": Dispel Magic casted"] * 2
    return get_visible_results(casting_player, other_player, res)


def raise_dead(casting_player, other_player):  # TODO: implement
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
    pass


def cure_light_wounds(casting_player, other_player):
    """Cure Light Wounds spell"""
    if casting_player.health < 15:
        casting_player.health += 1
        res = [casting_player.name + ": Restored 1 hp"] * 2
    else:
        res = ["Cure wasted: nothing to cure on " + casting_player.name] * 2
    return get_visible_results(casting_player, other_player, res)


def cure_heavy_wounds(casting_player, other_player):
    """Cure Heavy Wounds spell"""
    if casting_player.health < 14:
        casting_player.health += 2
        casting_player.effects["disease"] = False
        res = [casting_player.name + ": Restored 2 hp, disease effect removed."] * 2
    elif casting_player.health == 14:
        casting_player.health += 1
        casting_player.effects["disease"] = False
        res = [casting_player.name + ": Restored 1 hp, disease effect removed."] * 2
    else:
        res = ["Cure wasted: nothing to cure on " + casting_player.name] * 2
    return get_visible_results(casting_player, other_player, res)

# Damaging:


def missile(casting_player, other_player):
    """Missile spell"""
    chosen_player = choose_target_player(casting_player, other_player)
    if "Shield" not in chosen_player.spell_to_cast \
            and "Protection From Evil" not in chosen_player.spell_to_cast\
            and not check_counter_spell(other_player) \
            and not check_dispel_magic(other_player):  # TODO: pfe check other.effect for pfe > 0
        chosen_player.health -= 1
        res = ["Missile succesfully hit " + chosen_player.name] * 2
        vis = True
    else:
        res = ["Missile thwarted"] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, chosen_player)


def finger_of_death(casting_player, other_player):
    """Finger of Death spell"""
    chosen_player = choose_target_player(casting_player, other_player)
    if not check_dispel_magic(chosen_player):
        chosen_player.health = 0
        res = ["Wizard " + chosen_player.name +
               " got brutally fingered and died in a very painful way..."] * 2
        vis = True
    else:
        res = ["Finger of Death could not be casted on " + chosen_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, chosen_player)


def lightning_bolt(casting_player, other_player):
    """Lightning Bolt spell"""
    chosen_player = choose_target_player(casting_player, other_player)
    if not check_dispel_magic(chosen_player):
        chosen_player.health -= 5
        res = [chosen_player.name + "received 5 damage from " + casting_player.name] * 2
        vis = True
    else:
        res = ["Lightning Bolt could not be casted on " + chosen_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, chosen_player)


def cause_light_wounds(casting_player, other_player):
    """Cause Light Wounds spell"""
    chosen_player = choose_target_player(casting_player, other_player)
    if not check_dispel_magic(chosen_player):
        chosen_player.health -= 2
        res = [chosen_player.name + "received 2 damage from " + casting_player.name] * 2
        vis = True
    else:
        res = ["Cause Light Wounds could not be casted on " + chosen_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, chosen_player)


def cause_heavy_wounds(casting_player, other_player):
    """Cause Heavy Wounds spell"""
    chosen_player = choose_target_player(casting_player, other_player)
    if not check_dispel_magic(chosen_player):
        chosen_player.health -= 3
        res = [chosen_player.name + "received 3 damage from " + casting_player.name] * 2
        vis = True
    else:
        res = ["Cause Heavy Wounds could not be casted on " + chosen_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, chosen_player)


def fireball(casting_player, other_player):
    """Fireball spell"""
    chosen_player = choose_target_player(casting_player, other_player)
    if not check_dispel_magic(chosen_player) \
            and "Ice Storm" not in chosen_player.spell_to_cast:
        chosen_player.health -= 5
        res = [chosen_player.name + "received 5 damage from " + casting_player.name] * 2
        vis = True
    else:
        res = ["Fireball could not be casted on " + chosen_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, chosen_player)


def fire_storm(casting_player, other_player):
    """Fire Storm spell"""
    if not check_dispel_magic(other_player) and "Ice Storm" not in other_player.spell_to_cast:
        if not check_counter_spell(other_player):
            other_player.health -= 5
        casting_player.health -= 5
        res = ["Fire Storm casted by " + casting_player.name] * 2
        vis = True
    else:
        res = ["Fire Storm nullified"] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis)


def ice_storm(casting_player, other_player):
    """Ice Storm spell"""
    if not check_dispel_magic(other_player) and "Fire Storm" not in other_player.spell_to_cast:
        if not check_counter_spell(other_player):
            other_player.health -= 5
            # casting_player only gets damage if enemy doesn't have fireball
        if "Fireball" not in other_player.spell_to_cast:
            casting_player.health -= 5
        res = ["Ice Storm casted by " + casting_player.name] * 2
        vis = True
    else:
        res = ["Ice Storm nullified"] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis)

# Enchantment:


def amnesia(casting_player, other_player):
    """gestures D-P-P. If the subject of this spell is a wizard, next turn he must repeat identically
    the gestures he made in the current turn, including stabs. If the subject is a monster it will
    attack whoever it attacked this turn. If the subject is simultaneously the subject of any of
    confusion, charm person, charm monster, paralysis or fear then none of the spells work."""
    chosen_player = choose_target_player(casting_player, other_player)
    if not check_remove_enchantment(chosen_player):  # TODO: dispel magic and counter-spell cancel this
        chosen_player.effects["Amnesia"] = True
        res = ["Amnesia casted on " + chosen_player.name] * 2
        vis = True
    else:
        res = ["Amnesia could not be casted on " + chosen_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, chosen_player)


def confusion(casting_player, other_player):
    """gestures D-S-F. If the subject of this spell is a wizard, next turn he writes down his
    gestures as usual and after exposing them, rolls 2 dice to determine which gesture is
    superseded due to his being confused. The first die indicates left hand on 1-3, right on 4-6.
    The second roll determines what the gesture for that hand shall be replaced with: 1=C, 2=D,
    3=F, 4=P, 5=S, 6=W. If the subject of the spell is a monster, it attacks at random that turn.
    If the subject is also the subject of any of: amnesia, charm person, charm monster, paralysis
    or fear, none of the spells work."""
    chosen_player = choose_target_player(casting_player, other_player)
    if not check_remove_enchantment(chosen_player):  # TODO: dispel magic and counter-spell cancel this
        chosen_player.effects["Confusion"] = True
        res = ["Confusion casted on " + chosen_player.name] * 2
        vis = True
    else:
        res = ["Confusion could not be casted on " + chosen_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, chosen_player)


def charm_person(casting_player, other_playe):
    """gestures P-S-D-F. Except for cancellation with other enchantments, this spell only affects
    humans. The subject is told which of his hands will be controlled at the time the spell hits,
    and in the following turn, the caster of the spell writes down the gesture he wants the subject's
    named hand to perform. This could be a stab or nothing. If the subject is only so because of a
    reflection from a magic mirror the subject of the mirror assumes the role of caster and writes
    down his opponent's gesture. If the subject is also the subject of any of amnesia, confusion,
    charm monster, paralysis or fear, none of the spells work."""
    chosen_player = choose_target_player(casting_player, other_player)
    if not check_remove_enchantment(chosen_player):  # TODO: dispel magic and counter-spell cancel this
        chosen_player.effects["Charm Person"] = True
        res = ["Charm Person casted on " + chosen_player.name] * 2
        vis = True
    else:
        res = ["Charm Person could not be casted on " + chosen_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_playe, res, vis, chosen_player)


def paralysis(casting_player, other_player):
    """gestures F-F-F. If the subject of the spell is a wizard, then on the turn the spell is cast,
    after gestures have been revealed, the caster selects one of the wizard's hands and on the next
    turn that hand is paralyzed into the position it is in this turn. If the wizard already had a
    paralyzed hand, it must be the same hand which is paralyzed again. Certain gestures remain the
    same but if the hand being paralyzed is performing a C, S or W it is instead paralyzed into
    F, D or P respectively, otherwise it will remain in the position written down (this allows repeated stabs).
    A favourite ploy is to continually paralyze a hand (F-F-F-F-F-F etc.) into a non-P gesture and then set a
    monster on the subject so that he has to use his other hand to protect himself, but then has no defence
    against other magical attacks. If the subject of the spell is a monster (excluding elementals which are
    unaffected) it simply does not attack in the turn following the one in which the spell was cast.
    If the subject of the spell is also the subject of any of amnesia, confusion, charm person,
    charm monster or fear, none of the spells work."""
    chosen_player = choose_target_player(casting_player, other_player)
    if not check_remove_enchantment(chosen_player):  # TODO: dispel magic and counter-spell cancel this
        chosen_player.effects["Paralysis"] = True
        res = ["Paralysis casted on " + chosen_player.name] * 2
        vis = True
    else:
        res = ["Paralysis could not be casted on " + chosen_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, chosen_player)


def fear(casting_player, other_player):
    """gestures S-W-D. In the turn following the casting of this spell,
    the subject cannot perform a C, D, F or S gesture. This obviously
    has no effect on monsters. If the subject is also the subject of
    amnesia, confusion, charm person, charm monster or paralysis, then
    none of the spells work."""
    chosen_player = choose_target_player(casting_player, other_player)
    if not check_remove_enchantment(chosen_player):  # TODO: dispel magic and counter-spell cancel this
        chosen_player.effects["Fear"] = True
        res = ["Fear casted on " + chosen_player.name] * 2
        vis = True
    else:
        res = ["Fear could not be casted on " + chosen_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, chosen_player)


def anti_spell(casting_player, other_player):
    """gestures S-P-F. On the turn following the casting of this spell,
    the subject cannot include any gestures made on or before this turn
    in a spell sequence and must restart a new spell from the beginning
    of that spell sequence. The spell does not affect spells which are
    cast on the same turn nor does it affect monsters."""
    chosen_player = choose_target_player(casting_player, other_player)
    if not check_remove_enchantment(chosen_player):  # TODO: dispel magic and counter-spell cancel this
        chosen_player.effects["Anti-spell"] = True
        res = ["Anti-spell casted on " + chosen_player.name] * 2
        vis = True
    else:
        res = ["Anti-spell could not be casted on " + chosen_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, chosen_player)


def protection_from_evil(casting_player, other_player):
    """Protection From Evil spell"""
    chosen_player = choose_target_player(casting_player, other_player)
    if not check_remove_enchantment(chosen_player):
        chosen_player.effects["protection_from_evil"] = 3
        res = ["Protection From Evil casted on " + chosen_player.name] * 2
        vis = True
    else:
        res = ["Protection From Evil could not be casted on " + chosen_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, chosen_player)


def resist_heat(casting_player, other_player):
    """Resist Heat spell"""
    chosen_player = choose_target_player(casting_player, other_player)
    if not check_remove_enchantment(chosen_player):
        chosen_player.effects["resist_heat"] = True
        res = ["Resist Heat casted on " + chosen_player.name] * 2
        vis = True
    else:
        res = ["Resist Heat could not be casted on " + chosen_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, chosen_player)


def resist_cold(casting_player, other_player):
    """Resist Cold spell"""
    chosen_player = choose_target_player(casting_player, other_player)
    if not check_remove_enchantment(chosen_player):
        chosen_player.effects["resist_cold"] = True
        res = ["Resist Cold casted on " + chosen_player.name] * 2
        vis = True
    else:
        res = ["Resist Cold could not be casted on " + chosen_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, chosen_player)


def disease(casting_player, other_player):
    """Disease spell"""
    chosen_player = choose_target_player(casting_player, other_player)
    if not check_remove_enchantment(chosen_player) \
            and not check_dispel_magic(chosen_player) \
            and "Cure Heavy Wounds" not in chosen_player.spell_to_cast:
        chosen_player.effects["disease"] = 7
        res = ["Disease casted on " + chosen_player.name + ". Death is coming..."] * 2
        vis = True
    else:
        res = ["Disease could not be casted on " + chosen_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, chosen_player)


def poison(casting_player, other_player):
    """Poison spell"""
    chosen_player = choose_target_player(casting_player, other_player)
    if not check_remove_enchantment(chosen_player) \
            and not check_dispel_magic(chosen_player):
        chosen_player.effects["poison"] = 7
        res = ["Poison casted on " + chosen_player.name + ". Death will be slow and painful..."] * 2
        vis = True
    else:
        res = ["Poison could not be casted on " + chosen_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, chosen_player)


def blindness(casting_player, other_player):
    """gestures D-W-F-F-(d. For the next 3 turns not including the one in which the spell was cast, the subject
    is unable to see. If he is a wizard, he cannot tell what his opponent's gestures are, although he must be informed
    of any which affect him (e.g. summons spells, missile etc cast at him) but not counter- spells to his own attacks.
    Indeed he will not know if his own spells work unless they also affect him (e.g. a fire storm when he isn't
    resistant to fire.) He can control his monsters (e.g. "Attack whatever it was that just attacked me"). Blinded
    monsters are instantly destroyed and cannot attack in that turn."""
    chosen_player = choose_target_player(casting_player, other_player)
    if not check_remove_enchantment(chosen_player):
        chosen_player.effects["Blindness"] = 3
        res = ["Blindness casted on " + chosen_player.name] * 2
        vis = True
    else:
        res = ["Blindness could not be casted on " + chosen_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, chosen_player)


def invisibility(casting_player, other_player):
    """Invisibility spell"""
    chosen_player = choose_target_player(casting_player, other_player)
    if not check_remove_enchantment(chosen_player) \
            and not check_dispel_magic(chosen_player) \
            and not check_counter_spell(chosen_player):
        chosen_player.effects["invisible"] = True
        res = [chosen_player.name + " became invisible"] * 2
        vis = True
    else:
        res = [chosen_player.name + " could not become invisible"] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, chosen_player)


def haste(casting_player, other_player):
    """gestures P-W-P-W-W-C. For the next 3 turns, the subject (but not his monsters if a wizard) makes an extra set of
    gestures due to being speeded up. This takes effect in the following turn so that instead of giving one pair of
    gestures, 2 are given, the effect of both being taken simultaneously at the end of the turn. Thus a single
    counter-spell from his adversary could cancel 2 spells cast by the hastened wizard on 2 half-turns if the phasing is
    right. Non-hastened wizards and monsters can see everything the hastened individual is doing. Hastened monsters can
    change target in the extra turns if desired."""
    chosen_player = choose_target_player(casting_player, other_player)
    if not check_remove_enchantment(chosen_player):
        chosen_player.effects["Haste"] = 3
        res = ["Haste casted on " + chosen_player.name] * 2
        vis = True
    else:
        res = ["Haste could not be casted on " + chosen_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, chosen_player)


def time_stop(casting_player, other_player):
    """gestures S-P-P-C. The subject of this spell immediately takes an extra turn, on which no-one can see or know
    about unless they are harmed. All non-affected beings have no resistance to any form of attack, e.g. a wizard
    halfway through the duration of a protection from evil spell can be harmed by a monster which has had its time
    stopped. Time-stopped monsters attack whoever their controller instructs, and time-stopped elementals affect
    everyone, resistance to heat or cold being immaterial in that turn."""
    chosen_player = choose_target_player(casting_player, other_player)
    if not check_remove_enchantment(chosen_player):
        chosen_player.effects["Time Stop"] = True
        res = ["Time Stop on " + chosen_player.name] * 2
        vis = True
    else:
        res = ["Time Stop could not be casted on " + chosen_player.name] * 2
        vis = False
    return get_visible_results(casting_player, other_player, res, vis, chosen_player)


def delayed_effect(casting_player, other_player):  # TODO: WTF O.o
    """gestures D-W-S-S-S-P. This spell only works if cast upon a wizard. The next spell he completes, provided it is on
    this turn or one of the next 3 is "banked" until needed, i.e. it fails to work until its caster desires. This next
    spell which is to be banked does not include the actual spell doing the banking. The spell must be written down to
    be used by its caster at the same time that he writes his gestures. Note that spells banked are those cast by the
    subject not those cast at him. If he casts more than one spell at the same time he chooses which is to be banked.
    Remember that P is a shield spell, and surrender is not a spell. A wizard may only have one spell banked at any one
    time."""
    pass


def permanency(casting_player, other_player):  # TODO: WTF O.o
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
    pass


# Non-spells


def stab(casting_player, other_player):
    """Stab no-spell"""
    if "Shield" not in other_player.spell_to_cast \
            and "Protection From Evil" not in other_player.spell_to_cast \
            and not check_counter_spell(other_player) \
            and not check_dispel_magic(other_player):  # TODO: pfe check other.effect for pfe > 0
        other_player.health -= 1
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
    "surrender": False,
    "invisible": False,
    "protection_from_evil": 0,
    "resist_heat": False,
    "resist_cold": False,
    "poison": 0,
    # new effects:
    "Anti-spell": False,
    "Fear": False,
    "Paralysis": False,
    "Charm Person": False,
    "Confusion": False,
    "Amnesia": False,
    "Permanency": 0,
    "Delayed effect": 0,
    "Blindness": 0,
    "Haste": 0,
    "Time Stop", False
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
