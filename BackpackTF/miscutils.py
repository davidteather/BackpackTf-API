import requests
import json
import struct


class MiscUtils:
    def __init__(self, obj=None):
        #r = requests.get("https://backpack.tf/filters")

        #obj = json.loads(r.text)
        # cached because backpacktf has cloudflare for some reason
        if manual_filter == None:
            obj = {"quality":[{"id":"14","color":"830000","name":"Collector's"},{"id":"15","color":"fafafa","name":"Decorated Weapon"},{"id":"1","color":"4D7455","name":"Genuine"},{"id":"13","color":"38F3AB","name":"Haunted"},{"id":"0","color":"B2B2B2","name":"Normal"},{"id":"9","color":"70B04A","name":"Self-Made"},{"id":"11","color":"CF6A32","name":"Strange"},{"id":"6","color":"FFD700","name":"Unique"},{"id":"5","color":"8650AC","name":"Unusual"},{"id":"3","color":"476291","name":"Vintage"}],"particle":[{"id":"3004","name":"'72"},{"id":"91","name":"Abduction"},{"id":"125","name":"Abyssal Aura"},{"id":"3024","name":"Accursed"},{"id":"59","name":"Aces High"},{"id":"3017","name":"Acidic Bubbles of Envy"},{"id":"82","name":"Amaranthine"},{"id":"98","name":"Ancient Codex"},{"id":"105","name":"Ancient Eldritch"},{"id":"69","name":"Anti-Freeze"},{"id":"3047","name":"Arachnid Assault"},{"id":"73","name":"Arcana"},{"id":"3039","name":"Arcane Assistance"},{"id":"3040","name":"Arcane Assistance"},{"id":"3033","name":"Arctic Aurora"},{"id":"148","name":"Aromatica"},{"id":"3038","name":"Astral Presence"},{"id":"92","name":"Atomic"},{"id":"151","name":"Bee Swarm"},{"id":"3023","name":"Bewitched"},{"id":"30","name":"Blizzardy Storm"},{"id":"81","name":"Bonzo The All-Gnawing"},{"id":"111","name":"Brain Drain"},{"id":"34","name":"Bubbling"},{"id":"13","name":"Burning Flames"},{"id":"39","name":"Cauldron Bubbles"},{"id":"75","name":"Chiroptera Venenata"},{"id":"149","name":"Chromatica"},{"id":"19","name":"Circling Heart"},{"id":"18","name":"Circling Peace Sign"},{"id":"11","name":"Circling TF Logo"},{"id":"121","name":"Clairvoyance"},{"id":"58","name":"Cloud 9"},{"id":"38","name":"Cloudy Moon"},{"id":"4","name":"Community Sparkle"},{"id":"703","name":"Cool"},{"id":"3048","name":"Creepy Crawlies"},{"id":"79","name":"Darkblaze"},{"id":"60","name":"Dead Presidents"},{"id":"90","name":"Death at Dusk"},{"id":"100","name":"Death by Disco"},{"id":"139","name":"Defragmenting Reality"},{"id":"80","name":"Demonflame"},{"id":"62","name":"Disco Beat Down"},{"id":"3027","name":"Eerie Lightning"},{"id":"40","name":"Eerie Orbiting Fire"},{"id":"106","name":"Eldritch Flame"},{"id":"94","name":"Electric Hat Protector"},{"id":"67","name":"Electrostatic"},{"id":"3041","name":"Emerald Allurement"},{"id":"3025","name":"Enchanted"},{"id":"704","name":"Energy Orb"},{"id":"103","name":"Ether Trail"},{"id":"129","name":"Ethereal Essence"},{"id":"3035","name":"Festive Spirit"},{"id":"122","name":"Fifth Dimension"},{"id":"37","name":"Flaming Lantern"},{"id":"3018","name":"Flammable Bubbles of Attraction"},{"id":"3005","name":"Fountain of Delight"},{"id":"136","name":"Fragmented Gluons"},{"id":"138","name":"Fragmented Photons"},{"id":"137","name":"Fragmented Quarks"},{"id":"141","name":"Fragmenting Reality"},{"id":"152","name":"Frisky Fireflies"},{"id":"87","name":"Frostbite"},{"id":"135","name":"Frozen Icefall"},{"id":"97","name":"Galactic Codex"},{"id":"114","name":"Galactic Gateway"},{"id":"28","name":"Genteel Smoke"},{"id":"3012","name":"Ghastly Ghosts"},{"id":"85","name":"Ghastly Ghosts Jr"},{"id":"127","name":"Ghastly Grove"},{"id":"3031","name":"Good-Hearted Goodies"},{"id":"162","name":"Gourdian Angel"},{"id":"160","name":"Gravelly Ghoul"},{"id":"71","name":"Green Black Hole"},{"id":"6","name":"Green Confetti"},{"id":"9","name":"Green Energy"},{"id":"156","name":"Green Giggler"},{"id":"45","name":"Harvest Moon"},{"id":"8","name":"Haunted Ghosts"},{"id":"3011","name":"Haunted Phantasm"},{"id":"86","name":"Haunted Phantasm Jr"},{"id":"113","name":"Head of Steam"},{"id":"78","name":"Hellfire"},{"id":"3013","name":"Hellish Inferno"},{"id":"3003","name":"Holy Grail"},{"id":"701","name":"Hot"},{"id":"3015","name":"Infernal Flames"},{"id":"3016","name":"Infernal Smoke"},{"id":"702","name":"Isotope"},{"id":"46","name":"It's A Secret To Everybody"},{"id":"101","name":"It's a mystery to everyone"},{"id":"102","name":"It's a puzzle to me"},{"id":"3029","name":"Jarate Shock"},{"id":"155","name":"Kaleidoscope"},{"id":"56","name":"Kill-a-Watt"},{"id":"43","name":"Knifestorm"},{"id":"157","name":"Laugh-O-Lantern"},{"id":"3036","name":"Magical Spirit"},{"id":"95","name":"Magnetic Hat Protector"},{"id":"12","name":"Massed Flies"},{"id":"3010","name":"Mega Strike"},{"id":"65","name":"Memory Leak"},{"id":"124","name":"Menacing Miasma"},{"id":"61","name":"Miami Nights"},{"id":"3008","name":"Midnight Whirlwind"},{"id":"44","name":"Misty Skull"},{"id":"88","name":"Molten Mallard"},{"id":"89","name":"Morning Glory"},{"id":"128","name":"Mystical Medley"},{"id":"99","name":"Nebula"},{"id":"104","name":"Nether Trail"},{"id":"3030","name":"Nether Void"},{"id":"107","name":"Neutron Star"},{"id":"31","name":"Nuts n' Bolts"},{"id":"3022","name":"Ominous Night"},{"id":"120","name":"Omniscient Orb"},{"id":"112","name":"Open Mind"},{"id":"33","name":"Orbiting Fire"},{"id":"32","name":"Orbiting Planets"},{"id":"66","name":"Overclocked"},{"id":"63","name":"Phosphorous"},{"id":"158","name":"Plum Prankster"},{"id":"76","name":"Poisoned Shadows"},{"id":"3019","name":"Poisonous Bubbles of Regret"},{"id":"68","name":"Power Surge"},{"id":"150","name":"Prismatica"},{"id":"163","name":"Pumpkin Party"},{"id":"7","name":"Purple Confetti"},{"id":"10","name":"Purple Energy"},{"id":"145","name":"Pyroland Daydream"},{"id":"159","name":"Pyroland Nightmare"},{"id":"3042","name":"Pyrophoric Personality"},{"id":"142","name":"Refragmenting Reality"},{"id":"117","name":"Ring of Fire"},{"id":"3020","name":"Roaring Rockets"},{"id":"72","name":"Roboactive"},{"id":"14","name":"Scorching Flames"},{"id":"3006","name":"Screaming Tiger"},{"id":"15","name":"Searing Plasma"},{"id":"3001","name":"Showstopper"},{"id":"3009","name":"Silver Cyclone"},{"id":"3007","name":"Skill Gotten Gains"},{"id":"35","name":"Smoking"},{"id":"153","name":"Smoldering Spirits"},{"id":"144","name":"Snowblinded"},{"id":"143","name":"Snowfallen"},{"id":"77","name":"Something Burning This Way Comes"},{"id":"134","name":"Sparkling Lights"},{"id":"3037","name":"Spectral Escort"},{"id":"3014","name":"Spectral Swirl"},{"id":"74","name":"Spellbound"},{"id":"3043","name":"Spellbound Aspect"},{"id":"3021","name":"Spooky Night"},{"id":"83","name":"Stare From Beyond"},{"id":"109","name":"Starstorm Insomnia"},{"id":"110","name":"Starstorm Slumber"},{"id":"3026","name":"Static Mist"},{"id":"3044","name":"Static Shock"},{"id":"36","name":"Steaming"},{"id":"47","name":"Stormy 13th Hour"},{"id":"29","name":"Stormy Storm"},{"id":"93","name":"Subatomic"},{"id":"64","name":"Sulphurous"},{"id":"17","name":"Sunbeams"},{"id":"3028","name":"Terrifying Thunder"},{"id":"57","name":"Terror-Watt"},{"id":"108","name":"Tesla Coil"},{"id":"116","name":"The Dark Doorway"},{"id":"115","name":"The Eldritch Opening"},{"id":"84","name":"The Ooze"},{"id":"70","name":"Time Warp"},{"id":"3046","name":"Toxic Terrors"},{"id":"130","name":"Twisted Radiance"},{"id":"133","name":"Valiant Vortex"},{"id":"3045","name":"Veno Shock"},{"id":"132","name":"Verdant Vortex"},{"id":"147","name":"Verdatica"},{"id":"161","name":"Vexed Volcanics"},{"id":"118","name":"Vicious Circle"},{"id":"123","name":"Vicious Vortex"},{"id":"131","name":"Violet Vortex"},{"id":"16","name":"Vivid Plasma"},{"id":"96","name":"Voltaic Hat Protector"},{"id":"154","name":"Wandering Wisps"},{"id":"119","name":"White Lightning"},{"id":"126","name":"Wicked Wood"},{"id":"3034","name":"Winter Spirit"},{"id":"3032","name":"Wintery Wisp"}],"rarity":[{"id":"99","color":"FFD700","name":""},{"id":"5","color":"D32CE6","name":"Assassin"},{"id":"1","color":"B0C3D9","name":"Civilian"},{"id":"4","color":"8847FF","name":"Commando"},{"id":"6","color":"EB4B4B","name":"Elite"},{"id":"2","color":"5E98D9","name":"Freelance"},{"id":"7","color":"E4AE39","name":"Immortal"},{"id":"3","color":"4B69FF","name":"Mercenary"},{"id":"0","color":"6A6156","name":"Stock"}],"paint":[{"id":3100495,"color":"2f4f4f","name":"A Color Similar to Slate"},{"id":8208497,"color":"7d4071","name":"A Deep Commitment to Purple"},{"id":1315860,"color":"141414","name":"A Distinctive Lack of Hue"},{"id":12377523,"color":"bcddb3","name":"A Mann's Mint"},{"id":2960676,"color":"2d2d24","name":"After Eight"},{"id":8289918,"color":"7e7e7e","name":"Aged Moustache Grey"},{"id":6637376,"color":"654740","name":"An Air of Debonair"},{"id":15132390,"color":"e6e6e6","name":"An Extraordinary Abundance of Tinge"},{"id":15185211,"color":"e7b53b","name":"Australium Gold"},{"id":3874595,"color":"3b1f23","name":"Balaclavas Are Forever"},{"id":14204632,"color":"d8bed8","name":"Color No. 216-190-216"},{"id":12807213,"color":"c36c2d","name":"Cream Spirit"},{"id":15308410,"color":"e9967a","name":"Dark Salmon Injustice"},{"id":8421376,"color":"808000","name":"Drably Olive"},{"id":7511618,"color":"729e42","name":"Indubitably Green"},{"id":13595446,"color":"cf7336","name":"Mann Co. Orange"},{"id":10843461,"color":"a57545","name":"Muskelmannbraun"},{"id":5322826,"color":"51384a","name":"Noble Hatter's Violet"},{"id":4732984,"color":"483838","name":"Operator's Overalls"},{"id":12955537,"color":"c5af91","name":"Peculiarly Drab Tincture"},{"id":16738740,"color":"ff69b4","name":"Pink as Hell"},{"id":6901050,"color":"694d3a","name":"Radigan Conagher Brown"},{"id":12073019,"color":"b8383b","name":"Team Spirit"},{"id":3329330,"color":"32cd32","name":"The Bitter Taste of Defeat and Lime"},{"id":15787660,"color":"f0e68c","name":"The Color of a Gentlemann's Business Pants"},{"id":8400928,"color":"803020","name":"The Value of Teamwork"},{"id":11049612,"color":"a89a8c","name":"Waterlogged Lab Coat"},{"id":8154199,"color":"7c6c57","name":"Ye Olde Rustic Colour"},{"id":4345659,"color":"424f3b","name":"Zepheniah's Greed"}],"spell_footsteps":[{"id":"8208497","color":"490623","name":"Halloween Spell: Bruised Purple Footprints","defindex":8919},{"id":"3100495","color":"100495","name":"Halloween Spell: Corpse Gray Footprints","defindex":8916},{"id":"8421376","color":"9168","name":"Halloween Spell: Gangreen Footprints","defindex":8915},{"id":"2","color":"109759","name":"Halloween Spell: Headless Horseshoes","defindex":8920},{"id":"13595446","color":"6737280","name":"Halloween Spell: Rotten Orange Footprints","defindex":8918},{"id":"1","color":"4540032","name":"Halloween Spell: Team Spirit Footprints","defindex":8914},{"id":"5322826","color":"6742399","name":"Halloween Spell: Violent Violet Footprints","defindex":8917}],"spell_paints":[{"id":"1","color":"6711680","name":"Halloween Spell: Chromatic Corruption","defindex":8902},{"id":"0","color":"55","name":"Halloween Spell: Die Job","defindex":8901},{"id":"2","color":"5280","name":"Halloween Spell: Putrescent Pigmentation","defindex":8900},{"id":"4","color":"6776960","name":"Halloween Spell: Sinister Staining","defindex":8904},{"id":"3","color":"6744192","name":"Halloween Spell: Spectral Spectrum","defindex":8903}],"origin":[{"id":"1","name":"Achievement"},{"id":"15","name":"CD Key"},{"id":"27","name":"CYOA Blood Money Purchase"},{"id":"16","name":"Collection Reward"},{"id":"23","name":"Contract Completion Reward"},{"id":"4","name":"Crafted"},{"id":"9","name":"Earned"},{"id":"14","name":"Foreign Item"},{"id":"8","name":"Found in Crate"},{"id":"6","name":"Gifted"},{"id":"12","name":"Halloween Drop"},{"id":"20","name":"MvM Badge completion reward"},{"id":"21","name":"MvM Squad surplus reward"},{"id":"19","name":"Periodic score reward"},{"id":"17","name":"Preview Item"},{"id":"2","name":"Purchased"},{"id":"22","name":"Recipe output"},{"id":"13","name":"Steam Purchase"},{"id":"18","name":"Steam Workshop Contribution"},{"id":"5","name":"Store Promotion"},{"id":"7","name":"Support Granted"},{"id":"10","name":"Third-Party Promotion"},{"id":"0","name":"Timed Drop"},{"id":"25","name":"Trade-Up"},{"id":"24","name":"Trade-Up Output"},{"id":"3","name":"Traded"},{"id":"29","name":"Untradable Free Contract Reward"},{"id":"26","name":"Viral Competitive Beta Pass Spread"},{"id":"28","name":"War Paint"},{"id":"11","name":"Wrapped Gift"}],"numerics":[{"name":"Crate Series","field":"crate"},{"name":"Level","field":"level"},{"name":"Medal #","field":"medal"},{"name":"Craft #","field":"craft_number"}],"show_tradable":true,"show_craftable":true,"wear_tiers":{"Factory New":{"id":1,"name":"Factory New"},"Minimal Wear":{"id":2,"name":"Minimal Wear"},"Field-Tested":{"id":3,"name":"Field-Tested"},"Well-Worn":{"id":4,"name":"Well-Worn"},"Battle Scarred":{"id":5,"name":"Battle Scarred"}},"show_australium":true,"show_slot":true,"show_class":true,"show_killstreak_tab":true,"killstreakers":[{"id":2002,"name":"Fire Horns"},{"id":2003,"name":"Cerebral Discharge"},{"id":2004,"name":"Tornado"},{"id":2005,"name":"Flames"},{"id":2006,"name":"Singularity"},{"id":2007,"name":"Incinerator"},{"id":2008,"name":"Hypno-Beam"}],"sheens":[{"id":1,"name":"Team Shine"},{"id":2,"name":"Deadly Daffodil"},{"id":3,"name":"Manndarin"},{"id":4,"name":"Mean Green"},{"id":5,"name":"Agonizing Emerald"},{"id":6,"name":"Villainous Violet"},{"id":7,"name":"Hot Rod"}],"killstreak_tiers":[{"id":0,"name":"None"},{"id":1,"name":"Standard"},{"id":2,"name":"Specialized"},{"id":3,"name":"Professional"}],"strange_parts":[{"id":22,"name":"Airborne Enemies Killed"},{"id":84,"name":"Allied Healing Done"},{"id":95,"name":"Assists"},{"id":19,"name":"Buildings Destroyed"},{"id":79,"name":"Burning Enemy Kills"},{"id":37,"name":"Cloaked Spies Killed"},{"id":33,"name":"Critical Kills"},{"id":82,"name":"Damage Dealt"},{"id":47,"name":"Defender Kills"},{"id":13,"name":"Demomen Killed"},{"id":28,"name":"Domination Kills"},{"id":17,"name":"Engineers Killed"},{"id":83,"name":"Fires Survived"},{"id":81,"name":"Freezecam Taunt Appearances"},{"id":88,"name":"Full Health Kills"},{"id":27,"name":"Full Moon Kills"},{"id":40,"name":"Giant Robots Destroyed"},{"id":23,"name":"Gib Kills"},{"id":45,"name":"Halloween Kills"},{"id":21,"name":"Headshot Kills"},{"id":14,"name":"Heavies Killed"},{"id":87,"name":"Kills"},{"id":67,"name":"Kills During Victory Time"},{"id":34,"name":"Kills While Explosive Jumping"},{"id":49,"name":"Kills While \u00dcbercharged"},{"id":77,"name":"Kills with a Taunt Attack"},{"id":80,"name":"Killstreaks Ended"},{"id":62,"name":"Long-Distance Kills"},{"id":44,"name":"Low-Health Kills"},{"id":18,"name":"Medics Killed"},{"id":38,"name":"Medics Killed That Have Full \u00dcberCharge"},{"id":93,"name":"Not Crit nor MiniCrit Kills"},{"id":94,"name":"Player Hits"},{"id":85,"name":"Point-Blank Kills"},{"id":31,"name":"Posthumous Kills"},{"id":20,"name":"Projectiles Reflected"},{"id":15,"name":"Pyros Killed"},{"id":30,"name":"Revenge Kills"},{"id":68,"name":"Robot Scouts Destroyed"},{"id":74,"name":"Robot Spies Destroyed"},{"id":39,"name":"Robots Destroyed"},{"id":46,"name":"Robots Destroyed During Halloween"},{"id":36,"name":"Sappers Destroyed"},{"id":10,"name":"Scouts Killed"},{"id":11,"name":"Snipers Killed"},{"id":12,"name":"Soldiers Killed"},{"id":16,"name":"Spies Killed"},{"id":61,"name":"Tanks Destroyed"},{"id":89,"name":"Taunting Player Kills"},{"id":32,"name":"Teammates Extinguished"},{"id":48,"name":"Underwater Kills"},{"id":78,"name":"Unusual-Wearing Player Kills"}],"appid":440,"default_quality":6}

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
