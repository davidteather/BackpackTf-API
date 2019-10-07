class MiscUtils:
    def __init__(self):
        import requests
        import json

        r = requests.get("https://backpack.tf/filters")

        obj = json.loads(r.text)

        particles = obj['particle']
        qualities = obj['quality']
        rarities = obj['rarity']
        paints = obj['paint']
        origins = obj['origin']
        wear_tiers = obj['wear_tiers']
        killstreakers = obj['killstreakers']
        sheens = obj['sheens']
        killstreak_tiers = obj['killstreak_tiers']
        strange_parts = obj['strange_parts']

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
            self.particleObj[particle['name'].lower()] = int(particle['id'])

        for quality in qualities:
            self.qualitiesObj[quality['name'].lower()] = int(quality['id'])

        for rarity in rarities:
            self.raritiesObj[rarity['name'].lower()] = int(rarity['id'])

        for paint in paints:
            self.paintsObj[paint['name'].lower()] = int(paint['id'])

        for particle in origins:
            self.originsObj[particle['name'].lower()] = int(particle['id'])

        for particle in wear_tiers:
            self.wear_tiersObj[wear_tiers[particle]['name'].lower()] = int(wear_tiers[particle]['id'])

        for particle in killstreakers:
            self.killstreakers[particle['name'].lower()] = int(particle['id'])

        for particle in sheens:
            self.sheensObj[particle['name'].lower()] = int(particle['id'])

        for particle in killstreak_tiers:
            self.killstreak_tiers[particle['name'].lower()] = int(particle['id'])

        for particle in strange_parts:
            self.strange_partsObj[particle['name'].lower()] = int(particle['id'])


    #
    # Converts quality string to quality int
    #
    def quality_String_To_Int(self, string):
        try:
            return self.qualitiesObj[string.lower()]
        except:
            return ""

    #
    # Converts particle string to particle int
    #
    def particle_String_To_Int(self, string):
        try:
            return self.particleObj[string.lower()]
        except:
            return ""

    #
    # Converts rarity string to rarity int
    #
    def rarity_String_To_Int(self, string):
        try:
            return self.raritiesObj[string.lower()]
        except:
            return ""

    
    #
    # Origin quality string to origin int
    #
    def origin_String_To_Int(self, string):
        try:
            return self.originsObj[string.lower()]
        except:
            return ""


    #
    # Converts wear_tier string to wear_tier int
    #
    def wear_tier_String_To_Int(self, string):
        try:
            return self.wear_tiersObj[string.lower()]
        except:
            return ""


    #
    # Converts killstreaker string to killstreaker int
    #
    def killstreaker_String_To_Int(self, string):
        try:
            return self.killstreakers[string.lower()]
        except:
            return ""

    

    #
    # Converts sheen string to sheen int
    #
    def sheen_String_To_Int(self, string):
        try:
            return self.sheensObj[string.lower()]
        except:
            return ""


    #
    # Converts killstreak_tier string to killstreak_tier int
    #
    def killstreak_tier_String_To_Int(self, string):
        try:
            return self.killstreak_tiers[string.lower()]
        except:
            return ""


    #
    # Converts strange_part string to strange_part int
    #
    def strange_parts_String_To_Int(self, string):
        try:
            return self.strange_partsObj[string.lower()]
        except:
            return ""

    
    #
    # Converts paint string to paint int
    #
    def paint_String_To_Int(self, string):
        try:
            return self.paintsObj[string.lower()]
        except:
            return ""


    #
    # Converts steam ID into the account_id account ID is used in trading requests
    #
    def steam_id_to_account_id(self, steam_id):
        import struct
        return str(struct.unpack('>L', int(steam_id).to_bytes(8, byteorder='big')[4:])[0])