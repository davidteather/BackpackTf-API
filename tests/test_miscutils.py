from BackpackTF import MiscUtils


def test_quality_to_int():
    misc = MiscUtils()

    assert misc.quality_String_To_Int("Collector's") == 14
    assert misc.quality_String_To_Int("Decorated Weapon") == 15
    assert misc.quality_String_To_Int("Genuine") == 1
    assert misc.quality_String_To_Int("Haunted") == 13
    assert misc.quality_String_To_Int("Normal") == 0
    assert misc.quality_String_To_Int("Self-Made") == 9
    assert misc.quality_String_To_Int("Strange") == 11
    assert misc.quality_String_To_Int("Unique") == 6
    assert misc.quality_String_To_Int("Unusual") == 5
    assert misc.quality_String_To_Int("Vintage") == 3


def test_particle_to_int():
    misc = MiscUtils()

    assert misc.particle_String_To_Int("Abduction") == 91
    assert misc.particle_String_To_Int("Aces High") == 59
    assert misc.particle_String_To_Int("Acidic Bubbles of Envy") == 3017
    assert misc.particle_String_To_Int("Amaranthine") == 82
    assert misc.particle_String_To_Int("Bubbling") == 34
    assert misc.particle_String_To_Int("Burning Flames") == 13
    assert misc.particle_String_To_Int("Cauldron Bubbles") == 39
    assert misc.particle_String_To_Int("Cool") == 703
    assert misc.particle_String_To_Int("Dead Presidents") == 60


def test_rarity_to_int():
    misc = MiscUtils()

    assert misc.rarity_String_To_Int("") == 99
    assert misc.rarity_String_To_Int("Assassin") == 5
    assert misc.rarity_String_To_Int("Civilian") == 1
    assert misc.rarity_String_To_Int("Elite") == 6
    assert misc.rarity_String_To_Int("Freelance") == 2
    assert misc.rarity_String_To_Int("Immortal") == 7


def test_origin_to_int():
    misc = MiscUtils()

    assert misc.origin_String_To_Int("Achievement") == 1
    assert misc.origin_String_To_Int("CD Key") == 15
    assert misc.origin_String_To_Int("Collection Reward") == 16
    assert misc.origin_String_To_Int("Earned") == 9
    assert misc.origin_String_To_Int("Gifted") == 6


def test_wear_tier_to_int():
    misc = MiscUtils()

    assert misc.wear_tier_String_To_Int("Factory New") == 1
    assert misc.wear_tier_String_To_Int("Minimal Wear") == 2
    assert misc.wear_tier_String_To_Int("Field-Tested") == 3
    assert misc.wear_tier_String_To_Int("Well-Worn") == 4
    assert misc.wear_tier_String_To_Int("Battle Scarred") == 5


def test_killstreaker_to_int():
    misc = MiscUtils()

    assert misc.killstreaker_String_To_Int("Fire Horns") == 2002
    assert misc.killstreaker_String_To_Int("Cerebral Discharge") == 2003
    assert misc.killstreaker_String_To_Int("Tornado") == 2004
    assert misc.killstreaker_String_To_Int("Flames") == 2005
    assert misc.killstreaker_String_To_Int("Singularity") == 2006
    assert misc.killstreaker_String_To_Int("Incinerator") == 2007


def test_sheen_to_int():
    misc = MiscUtils()

    assert misc.sheen_String_To_Int("Team Shine") == 1
    assert misc.sheen_String_To_Int("Deadly Daffodil") == 2
    assert misc.sheen_String_To_Int("Manndarin") == 3
    assert misc.sheen_String_To_Int("Mean Green") == 4
    assert misc.sheen_String_To_Int("Agonizing Emerald") == 5
    assert misc.sheen_String_To_Int("Villainous Violet") == 6
    assert misc.sheen_String_To_Int("Hot Rod") == 7


def test_Killstreak_tier_to_int():
    misc = MiscUtils()

    assert misc.killstreak_tier_String_To_Int("None") == 0
    assert misc.killstreak_tier_String_To_Int("Standard") == 1
    assert misc.killstreak_tier_String_To_Int("Specialized") == 2
    assert misc.killstreak_tier_String_To_Int("Professional") == 3


def test_strange_parts_to_int():
    misc = MiscUtils()

    assert misc.strange_parts_String_To_Int("Airborne Enemies Killed") == 22
    assert misc.strange_parts_String_To_Int("Allied Healing Done") == 84
    assert misc.strange_parts_String_To_Int("Assists") == 95
    assert misc.strange_parts_String_To_Int("Critical Kills") == 33
    assert misc.strange_parts_String_To_Int("Damage Dealt") == 82


def test_paint_to_Int():
    misc = MiscUtils()

    assert misc.paint_String_To_Int("A Color Similar to Slate") == 3100495
    assert misc.paint_String_To_Int("A Deep Commitment to Purple") == 8208497
    assert misc.paint_String_To_Int("A Distinctive Lack of Hue") == 1315860
    assert misc.paint_String_To_Int("A Mann's Mint") == 12377523
    assert misc.paint_String_To_Int("After Eight") == 2960676
    assert misc.paint_String_To_Int("Aged Moustache Grey") == 8289918


def test_steam_id_to_account_id():
    misc = MiscUtils()

    assert misc.steam_id_to_account_id("76561198195716551") == "235450823"
