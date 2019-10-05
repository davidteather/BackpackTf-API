class MiscUtils:
    def __init__(self):
        self.active = 1

    #
    # Converts quality string to quality int
    #
    def quality_String_To_Int(self, string):
        checkStr = string.lower()

        if checkStr == "normal":
            return 0
        elif checkStr == "genuine":
            return 1
        elif checkStr == "vintage":
            return 3
        elif checkStr == "unusual":
            return 5
        elif checkStr == "unique":
            return 6
        elif checkStr == "community":
            return 7
        elif checkStr == "developer":
            return 8
        elif checkStr == "selfmade":
            return 9
        elif checkStr == "strange":
            return 11
        elif checkStr == "haunted":
            return 13
        elif checkStr == "collectors":
            return 14
        elif checkStr == "paintkitweapon":
            return 15

    #
    # Converts wear_tier string to wear_tier int
    #

    def wear_Tier_String_To_Int(self, string):
        checkStr = string.lower()

        if checkStr == "factory new":
            return 1
        elif checkStr == "minimal wear":
            return 2
        elif checkStr == "field-tested":
            return 3
        elif checkStr == "well-worn":
            return 4
        elif checkStr == "battle scarred":
            return 5

    #
    # Converts killstreaker tier string to killstreaker int
    #

    def killstreaker_Tier_String_To_Int(self, string):
        checkStr = string.lower()

        if checkStr == "standard":
            return 1
        elif checkStr == "specialized":
            return 2
        elif checkStr == "professional":
            return 3

    #
    # Converts sheen string to sheen int
    #

    def sheen_String_To_Int(self, string):
        checkStr = string.lower()

        if checkStr == "team shine":
            return 1
        elif checkStr == "deadly daffodil":
            return 2
        elif checkStr == "manndarin":
            return 3
        elif checkStr == "mean green":
            return 4
        elif checkStr == "agonizing emerald":
            return 5
        elif checkStr == "villainous violet":
            return 6
        elif checkStr == "hot rod":
            return 7


    #
    # Converts steam ID into the account_id account ID is used in trading requests
    #
    def steam_id_to_account_id(self, steam_id):
        import struct
        return str(struct.unpack('>L', int(steam_id).to_bytes(8, byteorder='big')[4:])[0])