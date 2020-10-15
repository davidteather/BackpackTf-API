import requests
import json
import struct


class MiscUtils:
    def __init__(self):
        r = requests.get("https://backpack.tf/filters")

        obj = json.loads(r.text)

        particles = obj["particle"]
        qualities = obj["quality"]
        rarities = obj["rarity"]
        paints = obj["paint"]
        origins = obj["origin"]
        wear_tiers = obj["wear_tiers"]
        killstreakers = obj["killstreakers"]
        sheens = obj["sheens"]
        killstreak_tiers = obj["killstreak_tiers"]
        strange_parts = obj["strange_parts"]

        self.particleObj = {}
        self.qualitiesObj = {}
        self.raritiesObj = {}
        self.paintsObj = {}
        self.originsObj = {}
        self.wear_tiersObj = {}
        self.killstreakers = {}
        self.sheensObj = {}
        self.killstreak_tiers = {}
        self.strange_partsObj = {}

        for particle in particles:
            self.particleObj[particle["name"].lower()] = int(particle["id"])

        for quality in qualities:
            self.qualitiesObj[quality["name"].lower()] = int(quality["id"])

        for rarity in rarities:
            self.raritiesObj[rarity["name"].lower()] = int(rarity["id"])

        for paint in paints:
            self.paintsObj[paint["name"].lower()] = int(paint["id"])

        for particle in origins:
            self.originsObj[particle["name"].lower()] = int(particle["id"])

        for particle in wear_tiers:
            self.wear_tiersObj[wear_tiers[particle]["name"].lower()] = int(
                wear_tiers[particle]["id"]
            )

        for particle in killstreakers:
            self.killstreakers[particle["name"].lower()] = int(particle["id"])

        for particle in sheens:
            self.sheensObj[particle["name"].lower()] = int(particle["id"])

        for particle in killstreak_tiers:
            self.killstreak_tiers[particle["name"].lower()] = int(particle["id"])

        for particle in strange_parts:
            self.strange_partsObj[particle["name"].lower()] = int(particle["id"])

    #
    # Converts quality string to quality int
    #
    def quality_string_to_int(self, string):
        try:
            return self.qualitiesObj[string.lower()]
        except:
            return ""

    # alias for compatibility with older versions
    # please use the new name, "quality_string_to_int"
    quality_String_To_Int = quality_string_to_int

    #
    # Converts particle string to particle int
    #
    def particle_string_to_int(self, string):
        try:
            return self.particleObj[string.lower()]
        except:
            return ""

    # alias for compatibility with older versions
    # please use the new name, "particle_string_to_int"
    particle_String_To_Int = particle_string_to_int

    #
    # Converts rarity string to rarity int
    #
    def rarity_string_to_int(self, string):
        try:
            return self.raritiesObj[string.lower()]
        except:
            return ""

    # alias for compatibility with older versions
    # please use the new name, "rarity_string_to_int"
    rarity_String_To_Int = rarity_string_to_int

    #
    # Origin quality string to origin int
    #
    def origin_string_to_int(self, string):
        try:
            return self.originsObj[string.lower()]
        except:
            return ""

    # alias for compatibility with older versions
    # please use the new name, "origin_string_to_int"
    origin_String_To_Int = origin_string_to_int

    #
    # Converts wear_tier string to wear_tier int
    #
    def wear_tier_string_to_int(self, string):
        try:
            return self.wear_tiersObj[string.lower()]
        except:
            return ""

    # alias for compatibility with older versions
    # please use the new name, "wear_tier_string_to_int"
    wear_tier_String_To_Int = wear_tier_string_to_int

    #
    # Converts killstreaker string to killstreaker int
    #
    def killstreaker_string_to_int(self, string):
        try:
            return self.killstreakers[string.lower()]
        except:
            return ""

    # alias for compatibility with older versions
    # please use the new name, "killstreaker_string_to_int"
    killstreaker_String_To_Int = killstreaker_string_to_int

    #
    # Converts sheen string to sheen int
    #
    def sheen_string_to_int(self, string):
        try:
            return self.sheensObj[string.lower()]
        except:
            return ""

    # alias for compatibility with older versions
    # please use the new name, "sheen_string_to_int"
    sheen_String_To_Int = sheen_string_to_int

    #
    # Converts killstreak_tier string to killstreak_tier int
    #
    def killstreak_tier_string_to_int(self, string):
        try:
            return self.killstreak_tiers[string.lower()]
        except:
            return ""

    # alias for compatibility with older versions
    # please use the new name, "killstreak_tier_string_to_int"
    killstreak_tier_String_To_Int = killstreak_tier_string_to_int

    #
    # Converts strange_part string to strange_part int
    #
    def strange_parts_string_to_int(self, string):
        try:
            return self.strange_partsObj[string.lower()]
        except:
            return ""

    # alias for compatibility with older versions
    # please use the new name, "strange_parts_string_to_int"
    strange_parts_String_To_Int = strange_parts_string_to_int

    #
    # Converts paint string to paint int
    #
    def paint_string_to_int(self, string):
        try:
            return self.paintsObj[string.lower()]
        except:
            return ""

    # alias for compatibility with older versions
    # please use the new name, "paint_string_to_int"
    paint_String_To_Int = paint_string_to_int

    #
    # Converts steam ID into the account_id account ID is used in trading requests
    #
    def steam_id_to_account_id(self, steam_id):
        return str(
            struct.unpack(">L", int(steam_id).to_bytes(8, byteorder="big")[4:])[0]
        )

    # Get information about a steam user
    def get_user_info(self, steam_id):
        p = {"steamids": [steam_id]}
        r = requests.get("https://backpack.tf/api/IGetUsers/v3", params=p)

        obj = json.loads(r.text)

        if obj["response"]["success"] == 1:
            # steam_id can be either a str or an int
            return obj["response"]["players"][str(steam_id)]
        else:
            return None
