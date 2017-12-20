from enum import Enum

class Spells:
    
    class Magic_PALADIN(Enum):

        PALADIN_LAY_ON_HANDS = 'SPCL211'
        PALADIN_DETECT_EVIL = 'SPCL212'
        PALADIN_PROTECTION_FROM_EVIL = 'SPCL213'
        PALADIN_SUMMON_DEVA = 'SPCL923'

    class Magic_SHAMAN(Enum):

        SHAMAN_SPIRIT_FORM = 'SPCL940'
        SHAMAN_FAVORED_OF_THE_SPIRITS = 'SPCL941'

    class Magic_THIEF(Enum):

        THIEF_DETECT_ILLUSION = 'SPIN805'
        THIEF_SET_SNARE = 'SPCL412'
        THIEF_SET_SPECIAL_SNARE = 'SPCL414'

    class Magic_TOTEMIC(Enum):

        TOTEMIC_DRUID_SUMMON_SPIRIT_ANIMAL = 'SPCL621'

    class Magic_SHAPESHIFTER(Enum):

        SHAPESHIFTER_SHAPESHIFT_NATURAL_FORM = 'SPIN124'
        SHAPESHIFTER_SHAPESHIFT_WEREWOLF = 'SPCL643'
        SHAPESHIFTER_SHAPESHIFT_GREATERWEREWOLF = 'SPCL644'

    class Magic_BLACKGUARD(Enum):

        BLACKGUARD_ABSORB_HEALTH = 'SPCL102'
        BLACKGUARD_ANIMATE_DEAD = 'SPCL106'
        AURA_OF_DESPAIR = 'SPCL103'

    class Magic_RANGER(Enum):

        RANGER_CHARM_ANIMAL = 'SPCL311'
        RANGER_TRACKING = 'SPCL922'

    class Magic_BERSERKER(Enum):

        BERSERKER_ENRAGE = 'SPCL321'
        BERSERKER_RAGE = 'SPCL321'

    class Magic_ARCHER(Enum):

        ARCHER_PROTECTION = 'SPIN898'
        ARCHER_CALL_SHOT = 'SPCL121'

    class Magic_WIZARD(Enum):

        #WIZARD_CHAOS_VISUALS_ONLY = 'SPWI050'
        #WIZARD_DISPEL_MAGIC_VISUALS_ONLY = 'SPWI051'
        #WIZARD_POWER_WORD_SILENCE_VISUALS_ONLY = 'SPWI052'
        #WIZARD_FLESH_TO_STONE_IGNORE_RESISTANCE = 'SPWI053'
        #WIZARD_FINGER_OF_DEATH_IGNORE_RESISTANCE = 'SPWI054'
        #WIZARD_DISINTEGRATE_IGNORE_RESISTANCE = 'SPWI055'
        #WIZARD_DISINTEGRATE2_IGNORE_RESISTANCE = 'SPWI056'
        WIZARD_GREASE = 'SPWI101'
        WIZARD_ARMOR = 'SPWI102'
        WIZARD_BURNING_HANDS = 'SPWI103'
        WIZARD_CHARM_PERSON = 'SPWI104'
        WIZARD_COLOR_SPRAY = 'SPWI105'
        WIZARD_BLINDNESS = 'SPWI106'
        WIZARD_FRIENDS = 'SPWI107'
        WIZARD_PROTECTION_FROM_PETRIFICATION = 'SPWI108'
        WIZARD_HOLD_PORTAL = 'SPWI109'
        WIZARD_IDENTIFY = 'SPWI110'
        WIZARD_INFRAVISION = 'SPWI111'
        WIZARD_MAGIC_MISSILE = 'SPWI112'
        WIZARD_PROTECTION_FROM_EVIL = 'SPWI113'
        WIZARD_SHIELD = 'SPWI114'
        WIZARD_SHOCKING_GRASP = 'SPWI115'
        WIZARD_SLEEP = 'SPWI116'
        WIZARD_CHILL_TOUCH = 'SPWI117'
        WIZARD_CHROMATIC_ORB = 'SPWI118'
        WIZARD_LARLOCH_MINOR_DRAIN = 'SPWI119'
        WIZARD_REFLECTED_IMAGE = 'SPWI120'
        WIZARD_REVEAL_MAGIC = 'SPWI121'
        WIZARD_PROTECTION_CIRCLE = 'SPWI122'
        WIZARD_FIND_FAMILAR = 'SPWI123'
        WIZARD_ALARM = 'SPWI124'
        WIZARD_NAHALS_RECKLESS_DWEOMER = 'SPWI124'
        WIZARD_SPOOK = 'SPWI125'
        WIZARD_BLUR = 'SPWI201'
        WIZARD_DETECT_EVIL = 'SPWI202'
        WIZARD_DETECT_INVISIBILITY = 'SPWI203'
        WIZARD_FOG_CLOUD = 'SPWI204'
        WIZARD_HORROR = 'SPWI205'
        WIZARD_INVISIBILITY = 'SPWI206'
        WIZARD_KNOCK = 'SPWI207'
        WIZARD_KNOW_ALIGNMENT = 'SPWI208'
        WIZARD_LUCK = 'SPWI209'
        WIZARD_RESIST_FEAR = 'SPWI210'
        WIZARD_MELF_ACID_ARROW = 'SPWI211'
        WIZARD_MIRROR_IMAGE = 'SPWI212'
        WIZARD_STINKING_CLOUD = 'SPWI213'
        WIZARD_STRENGTH = 'SPWI214'
        WIZARD_WEB = 'SPWI215'
        WIZARD_WIZARD_LOCK = 'SPWI216'
        WIZARD_AGANNAZAR_SCORCHER = 'SPWI217'
        WIZARD_GHOUL_TOUCH = 'SPWI218'
        WIZARD_VOCALIZE = 'SPWI219'
        WIZARD_POWER_WORD_SLEEP = 'SPWI220'
        WIZARD_RAY_OF_ENFEEBLEMENT = 'SPWI221'
        WIZARD_CHAOS_SHIELD = 'SPWI222'
        WIZARD_DEAFNESS = 'SPWI223'
        WIZARD_GLITTERDUST = 'SPWI224'
        WIZARD_CLAIRVOYANCE = 'SPWI301'
        WIZARD_DISPEL_MAGIC = 'SPWI302'
        WIZARD_REMOVE_MAGIC = 'SPWI302'
        WIZARD_FLAME_ARROW = 'SPWI303'
        WIZARD_FIREBALL = 'SPWI304'
        WIZARD_HASTE = 'SPWI305'
        WIZARD_HOLD_PERSON = 'SPWI306'
        WIZARD_INVISIBILITY_10_FOOT = 'SPWI307'
        WIZARD_LIGHTNING_BOLT = 'SPWI308'
        WIZARD_MONSTER_SUMMONING_1 = 'SPWI309'
        WIZARD_NON_DETECTION = 'SPWI310'
        WIZARD_PROTECTION_FROM_NORMAL_MISSILES = 'SPWI311'
        WIZARD_SLOW = 'SPWI312'
        WIZARD_SKULL_TRAP = 'SPWI313'
        WIZARD_VAMPIRIC_TOUCH = 'SPWI314'
        WIZARD_WRAITH_FORM = 'SPWI315'
        WIZARD_DIRE_CHARM = 'SPWI316'
        WIZARD_GHOST_ARMOR = 'SPWI317'
        WIZARD_MINOR_SPELL_DEFLECTION = 'SPWI318'
        WIZARD_PROTECTION_FROM_FIRE = 'SPWI319'
        WIZARD_PROTECTION_FROM_COLD = 'SPWI320'
        WIZARD_SPELL_THRUST = 'SPWI321'
        WIZARD_DETECT_ILLUSION = 'SPWI322'
        WIZARD_HOLD_UNDEAD = 'SPWI324'
        WIZARD_MELF_METEOR = 'SPWI325'
        WIZARD_TRUE_DISPEL_MAGIC = 'SPWI326'
        WIZARD_CONFUSION = 'SPWI401'
        WIZARD_DIMENSION_DOOR = 'SPWI402'
        WIZARD_FIRE_SHIELD_BLUE = 'SPWI403'
        WIZARD_ICE_STORM = 'SPWI404'
        WIZARD_IMPROVED_INVISIBILITY = 'SPWI405'
        WIZARD_MINOR_GLOBE_OF_INVULNERABILITY = 'SPWI406'
        WIZARD_MONSTER_SUMMONING_2 = 'SPWI407'
        WIZARD_STONE_SKIN = 'SPWI408'
        WIZARD_CONTAGION = 'SPWI409'
        WIZARD_REMOVE_CURSE = 'SPWI410'
        WIZARD_EMOTION_HOPELESSNESS = 'SPWI411'
        WIZARD_GREATER_MALISON = 'SPWI412'
        WIZARD_OTILUKES_RESILIENT_SPHERE = 'SPWI413'
        WIZARD_SPIRIT_ARMOR = 'SPWI414'
        WIZARD_POLYMORPH_OTHER = 'SPWI415'
        WIZARD_POLYMORPH_SELF = 'SPWI416'
        WIZARD_ENCHANTED_WEAPON = 'SPWI417'
        WIZARD_FIRE_SHIELD_RED = 'SPWI418'
        WIZARD_SECRET_WORD = 'SPWI419'
        WIZARD_MINOR_SEQUENCER = 'SPWI420'
        WIZARD_TELEPORT_FIELD = 'SPWI421'
        WIZARD_SPIDER_SPAWN = 'SPWI423'
        WIZARD_FAR_SIGHT = 'SPWI424'
        WIZARD_EYE = 'SPWI425'
        #WIZARD_POLYMORPH_NATURAL_FORM = 'SPWI490'
        #WIZARD_POLYMORPH_FLIND = 'SPWI493'
        #WIZARD_POLYMORPH_OGRE = 'SPWI494'
        #WIZARD_POLYMORPH_SPIDER = 'SPWI495'
        #WIZARD_POLYMORPH_MUSTARD_JELLY = 'SPWI496'
        #WIZARD_POLYMORPH_BROWN_BEAR = 'SPWI497'
        #WIZARD_POLYMORPH_BLACK_BEAR = 'SPWI498'
        #WIZARD_POLYMORPH_WOLF = 'SPWI499'
        WIZARD_ANIMATE_DEAD = 'SPWI501'
        WIZARD_CLOUDKILL = 'SPWI502'
        WIZARD_CONE_OF_COLD = 'SPWI503'
        WIZARD_MONSTER_SUMMONING_3 = 'SPWI504'
        WIZARD_SHADOW_DOOR = 'SPWI505'
        WIZARD_DOMINATION = 'SPWI506'
        WIZARD_HOLD_MONSTER = 'SPWI507'
        WIZARD_CHAOS = 'SPWI508'
        WIZARD_FEEBLEMIND = 'SPWI509'
        WIZARD_SPELL_IMMUNITY = 'SPWI510'
        WIZARD_PROTECTION_FROM_NORMAL_WEAPONS = 'SPWI511'
        WIZARD_PROTECTION_FROM_ELECTRICITY = 'SPWI512'
        WIZARD_BREACH = 'SPWI513'
        WIZARD_LOWER_RESISTANCE = 'SPWI514'
        WIZARD_ORACLE = 'SPWI515'
        WIZARD_CONJURE_LESSER_FIRE_ELEMENTAL = 'SPWI516'
        WIZARD_PROTECTION_FROM_ACID = 'SPWI517'
        WIZARD_PHANTOM_BLADE = 'SPWI518'
        WIZARD_SPELL_SHIELD = 'SPWI519'
        WIZARD_CONJURE_LESSER_AIR_ELEMENTAL = 'SPWI520'
        WIZARD_CONJURE_LESSER_EARTH_ELEMENTAL = 'SPWI521'
        WIZARD_MINOR_SPELL_TURNING = 'SPWI522'
        WIZARD_SUN_FIRE = 'SPWI523'
        #WIZARD_SPELL_IMMUNITY_ABJURATION = 'SPWI590'
        #WIZARD_SPELL_IMMUNITY_CONJURATION = 'SPWI591'
        #WIZARD_SPELL_IMMUNITY_DIVINATION = 'SPWI592'
        #WIZARD_SPELL_IMMUNITY_ENCHANTMENT = 'SPWI593'
        #WIZARD_SPELL_IMMUNITY_ILLUSIONIST = 'SPWI594'
        #WIZARD_SPELL_IMMUNITY_INVOCATION = 'SPWI595'
        #WIZARD_SPELL_IMMUNITY_NECROMANCY = 'SPWI596'
        #WIZARD_SPELL_IMMUNITY_ALTERATION = 'SPWI597'
        WIZARD_INVISIBLE_STALKER = 'SPWI601'
        WIZARD_GLOBE_OF_INVULNERABILITY = 'SPWI602'
        WIZARD_TENSERS_TRANSFORMATION = 'SPWI603'
        WIZARD_FLESH_TO_STONE = 'SPWI604'
        WIZARD_DEATH_SPELL = 'SPWI605'
        WIZARD_PROTECTION_FROM_MAGIC_ENERGY = 'SPWI606'
        WIZARD_MISLEAD = 'SPWI607'
        WIZARD_PIERCE_MAGIC = 'SPWI608'
        WIZARD_TRUE_SIGHT = 'SPWI609'
        WIZARD_MONSTER_SUMMONING_4 = 'SPWI610'
        WIZARD_PROTECTION_FROM_MAGIC_WEAPONS = 'SPWI611'
        WIZARD_POWER_WORD_SILENCE = 'SPWI612'
        WIZARD_IMPROVED_HASTE = 'SPWI613'
        WIZARD_DEATH_FOG = 'SPWI614'
        WIZARD_CHAIN_LIGHTNING = 'SPWI615'
        WIZARD_DISINTEGRATE = 'SPWI616'
        WIZARD_CONTINGENCY = 'SPWI617'
        WIZARD_SPELL_DEFLECTION = 'SPWI618'
        WIZARD_WYVERN_CALL = 'SPWI619'
        WIZARD_CONJURE_FIRE_ELEMENTAL = 'SPWI620'
        WIZARD_CONJURE_AIR_ELEMENTAL = 'SPWI621'
        WIZARD_CONJURE_EARTH_ELEMENTAL = 'SPWI622'
        WIZARD_CARRION = 'SPWI623'
        WIZARD_SUMMON_NISHRUU = 'SPWI624'
        WIZARD_STONE_TO_FLESH = 'SPWI625'
        WIZARD_SPELL_TURNING = 'SPWI701'
        WIZARD_PROTECTION_FROM_THE_ELEMENTS = 'SPWI702'
        WIZARD_PROJECT_IMAGE = 'SPWI703'
        WIZARD_RUBY_RAY_OF_REVERSAL = 'SPWI704'
        WIZARD_KHELBENS_WARDING_WHIP = 'SPWI705'
        WIZARD_WARDING_WHIP = 'SPWI705'
        WIZARD_CACOFIEND = 'SPWI707'
        WIZARD_MANTLE = 'SPWI708'
        WIZARD_TATTOOS_OF_POWER = 'SPWI709'
        WIZARD_SPELL_SEQUENCER = 'SPWI710'
        WIZARD_SPHERE_OF_CHAOS = 'SPWI711'
        WIZARD_DELAYED_BLAST_FIREBALL = 'SPWI712'
        WIZARD_FINGER_OF_DEATH = 'SPWI713'
        WIZARD_PRISMATIC_SPRAY = 'SPWI714'
        WIZARD_POWER_WORD_STUN = 'SPWI715'
        WIZARD_MORDENKAINENS_SWORD = 'SPWI716'
        WIZARD_SUMMON_EFREET = 'SPWI717'
        WIZARD_SUMMON_DJINNI = 'SPWI718'
        WIZARD_SUMMON_HAKEASHAR = 'SPWI719'
        WIZARD_CONTROL_UNDEAD = 'SPWI720'
        WIZARD_MASS_INVISIBILITY = 'SPWI721'
        WIZARD_LIMITED_WISH = 'SPWI722'
        WIZARD_IMPROVED_CHAOS_SHIELD = 'SPWI723'
        WIZARD_DELETED = 'SPWI801'
        WIZARD_PROTECTION_FROM_ENERGY = 'SPWI803'
        WIZARD_SIMULACRUM = 'SPWI804'
        WIZARD_PIERCE_SHIELD = 'SPWI805'
        WIZARD_SUMMON_FIEND = 'SPWI807'
        WIZARD_IMPROVED_MANTLE = 'SPWI808'
        WIZARD_SPELL_TRIGGER = 'SPWI809'
        WIZARD_INCENDIARY_CLOUD = 'SPWI810'
        WIZARD_SYMBOL_FEAR = 'SPWI811'
        WIZARD_ABI_DALZIMS_HORRID_WILTING = 'SPWI812'
        WIZARD_MAZE = 'SPWI813'
        WIZARD_OTTOS_IRRESISTIBLE_DANCE = 'SPWI814'
        WIZARD_POWER_WORD_BLIND = 'SPWI815'
        WIZARD_SYMBOL_STUN = 'SPWI816'
        WIZARD_SYMBOL_DEATH = 'SPWI817'
        WIZARD_BIGBYS_CLENCHED_FIST = 'SPWI818'
        #WIZARD_NPC_SYMBOL_DEATH = 'SPWI897'
        #WIZARD_NPC_SYMBOL_STUN = 'SPWI898'
        #WIZARD_NPC_SYMBOL_FEAR = 'SPWI899'
        WIZARD_SPELL_TRAP = 'SPWI902'
        WIZARD_SPELL_STRIKE = 'SPWI903'
        WIZARD_GATE = 'SPWI905'
        WIZARD_ABSOLUTE_IMMUNITY = 'SPWI907'
        WIZARD_CHAIN_CONTINGENCY = 'SPWI908'
        WIZARD_TIME_STOP = 'SPWI909'
        WIZARD_IMPRISONMENT = 'SPWI910'
        WIZARD_METEOR_SWARM = 'SPWI911'
        WIZARD_POWER_WORD_KILL = 'SPWI912'
        WIZARD_WAIL_OF_THE_BANSHEE = 'SPWI913'
        WIZARD_ENERGY_DRAIN = 'SPWI914'
        WIZARD_BLACK_BLADE_OF_DISASTER = 'SPWI915'
        WIZARD_SHAPECHANGE = 'SPWI916'
        WIZARD_FREEDOM = 'SPWI917'
        WIZARD_BIGBYS_CRUSHING_HAND = 'SPWI918'
        WIZARD_WISH = 'SPWI919'
        WIZARD_ENERGY_BLADES = 'SPWI920'
        #WIZARD_IMPROVED_ALACRITY = 'SPWI921'
        #WIZARD_IMPROVED_ALUCRITY = 'SPWI921'
        #WIZARD_DRAGONS_BREATH = 'SPWI922'
        #WIZARD_SUMMON_PLANATAR_GOOD = 'SPWI923'
        #WIZARD_SUMMON_PLANATAR_EVIL = 'SPWI924'
        #WIZARD_COMET = 'SPWI925'

    class Magic_BARBARIAN(Enum):

        BARBARIAN_RAGE = 'SPCL152'

    class Magic_ASSASSIN(Enum):

        ASSASSIN_POISON = 'SPCL423'

    class Magic_BLADE(Enum):

        BLADE_OFFENSIVE_SPIN = 'SPCL521'
        BLADE_DEFENSIVE_SPIN = 'SPCL522'

    class Magic_HELL(Enum):

        HELL_BUFFET = 'SPIN658'
        HELL_SELFISH_EVIL = 'SPIN747'
        HELL_SELFISH_GOOD = 'SPIN748'
        HELL_WRATH_EVIL = 'SPIN749'
        HELL_WRATH_GOOD = 'SPIN750'
        HELL_PRIDE_EVIL = 'SPIN751'
        HELL_PRIDE_GOOD = 'SPIN752'
        HELL_FEAR_EVIL = 'SPIN753'
        HELL_FEAR_GOOD = 'SPIN754'
        HELL_GREED_EVIL = 'SPIN755'
        HELL_GREED_GOOD = 'SPIN756'
        HELL_GAIN_CHR = 'SPIN759'
        HELL_GAIN_CON = 'SPIN760'
        HELL_GAIN_DEX = 'SPIN761'
        HELL_GAIN_WIS = 'SPIN762'
        HELL_GAIN_INT = 'SPIN763'
        HELL_GAIN_STR = 'SPIN764'
        HELL_LOSE_XP = 'SPIN765'
        HELL_LOSE_DEX = 'SPIN766'
        HELL_LOSE_HP = 'SPIN767'
        HELL_DISPELL = 'SPIN768'
        HELL_HOLD = 'SPIN769'
        HELL_EXPLODE = 'SPIN770'
        HELL_DAMAGE_HALF = 'SPIN771'
        HELL_FEAR = 'SPIN772'
        HELL_HOUND_FLAME = 'SPIN956'

    class Magic_CAVALIER(Enum):

        CAVALIER_REMOVE_FEAR = 'SPCL222'

    class Magic_WILD(Enum):

        WILD_MAGIC_AREA = 'SPIN645'
        WILD_MAGIC_ZONE = 'SPIN778'

    class Magic_LATHANDER(Enum):

        LATHANDER_BOON = 'SPCL741'
        LATHANDER_HOLD_UNDEAD = 'SPCL742'

    class Magic_WARRIOR(Enum):

        WARRIOR_WHIRLWIND = 'SPCL900'
        WARRIOR_GREATER_WHIRLWIND = 'SPCL901'
        WARRIOR_DEATHBLOW = 'SPCL902'
        WARRIOR_GREATER_DEATHBLOW = 'SPCL903'
        WARRIOR_RESIST_MAGIC = 'SPCL904'
        WARRIOR_CRITICAL_STRIKE = 'SPCL905'
        WARRIOR_POWER_ATTACK = 'SPCL906'
        WARRIOR_HARDINESS = 'SPCL907'
        WARRIOR_WAR_CRY = 'SPCL908'
        WARRIOR_SMITE = 'SPCL909'

    class Magic_GAIN(Enum):

        GAIN_ONE_CHA_PERMANENT = 'SPIN554'
        GAIN_ONE_WIS_PERMANENT = 'SPIN555'
        GAIN_ONE_INT_PERMANENT = 'SPIN556'
        GAIN_ONE_DEX_PERMANENT = 'SPIN557'
        GAIN_ONE_THACO = 'SPIN577'
        GAIN_ONE_AC = 'SPIN578'
        GAIN_HASTE_TEMPORARY = 'SPIN584'
        GAIN_MAGIC_RESIST_PERMANENT = 'SPIN585'
        GAIN_ONE_CON_PERMANENT = 'SPIN590'
        GAIN_ONE_STR_PERMANENT = 'SPIN591'

    class Magic_DRUID(Enum):

        DRUID_HUMAN_FORM = 'SPIN123'
        DRUID_SHAPESHIFT_FROM_BLACKBEAR = 'SPIN123'
        DRUID_SHAPESHIFT_BROWNBEAR = 'SPCL611'
        DRUID_SHAPESHIFT_WOLF = 'SPCL612'
        DRUID_SHAPESHIFT_BLACKBEAR = 'SPCL613'
        DRUID_IMMUNE_POISON = 'SPCL924'
        DRUID_RESISTS = 'SPCL925'

    class Magic_EVIL(Enum):

        EVIL_LAYONHANDS = 'SPIN773'

    class Magic_SHADOWDANCER(Enum):

        SHADOWDANCER_SHADOW_TWIN = 'SPCL936'
        SHADOWDANCER_SHADOW_MAZE = 'SPCL937'
        SHADOWDANCER_SHADOW_FORM = 'SPCL938'

    class Magic_INNATE(Enum):

        INNATE_CURE_LIGHT_WOUNDS = 'SPIN101'
        INNATE_SLOW_POISON = 'SPIN102'
        INNATE_DRAW_UPON_HOLY_MIGHT = 'SPIN103'
        INNATE_LARLOCHS_MINOR_DRAIN = 'SPIN104'
        INNATE_HORROR = 'SPIN105'
        INNATE_VAMPIRIC_TOUCH = 'SPIN106'

    class Magic_DM(Enum):

        DM_SHIELD = 'SPIN650'
        DM_SEE_INVISIBLE = 'SPIN651'
        DM_MAGIC_PROTECTION = 'SPIN652'
        DM_COLD_PROTECTION = 'SPIN653'
        DM_FIRE_PROTECTION = 'SPIN654'
        DM_IMPROVED_HASTE = 'SPIN655'

    class Magic_MONK(Enum):

        MONK_STUNNING_BLOW = 'SPCL811'
        MONK_LAY_ON_HANDS = 'SPCL815'
        MONK_QUIVERING_PALM = 'SPCL820'

    class Magic_AVENGER(Enum):

        AVENGER_SHAPESHIFT_NATURAL_FORM = 'SPIN122'
        AVENGER_SHAPESHIFT_SWORDSPIDER = 'SPCL632'
        AVENGER_SHAPESHIFT_BABYWYVERN = 'SPCL633'
        AVENGER_SHAPESHIFT_FIRESALAMANDER = 'SPCL634'

    class Magic_ROGUE(Enum):

        ROGUE_SET_SPIKE_TRAP = 'SPCL910'
        ROGUE_SET_EXPLODING_TRAP = 'SPCL911'
        ROGUE_SET_TIME_TRAP = 'SPCL912'
        ROGUE_EVASION = 'SPCL913'
        ROGUE_GREATER_EVASION = 'SPCL914'
        ROGUE_ASSASINATION = 'SPCL916'
        ROGUE_AVOID_DEATH = 'SPCL917'

    class Magic_BOOK(Enum):

        BOOK_GOLEM = 'SPIN840'
        BOOK_BEHOLD = 'SPIN841'
        BOOK_MIND = 'SPIN842'
        BOOK_UMBER = 'SPIN843'
        BOOK_SPIDER = 'SPIN844'
        BOOK_KOBOLD = 'SPIN845'

    class Magic_INQUIS(Enum):

        INQUIS_DISPEL_MAGIC = 'SPCL231'
        INQUIS_TRUE_SIGHT = 'SPCL232'

    class Magic_BEASTMASTER(Enum):

        BEASTMASTER_FIND_FAMILIAR = 'SPCL342'

    class Magic_POWERWORD(Enum):

        POWERWORD_BLIND = 'SPWI958'
        POWERWORD_STUN = 'SPWI959'
        POWERWORD_KILL = 'SPWI960'

    class Magic_CLERIC(Enum):

        CLERIC_BLESS = 'SPPR101'
        CLERIC_COMMAND = 'SPPR102'
        CLERIC_CURE_LIGHT_WOUNDS = 'SPPR103'
        CLERIC_DETECT_EVIL = 'SPPR104'
        CLERIC_ENTANGLE = 'SPPR105'
        CLERIC_MAGIC_STONE = 'SPPR106'
        CLERIC_PROTECT_FROM_EVIL = 'SPPR107'
        CLERIC_REMOVE_FEAR = 'SPPR108'
        CLERIC_SANCTUARY = 'SPPR109'
        CLERIC_SHILLELAGH = 'SPPR110'
        CLERIC_ARMOR_OF_FAITH = 'SPPR111'
        CLERIC_CIRCLE_OF_PROTECTION = 'SPPR112'
        CLERIC_DOOM = 'SPPR113'
        CLERIC_ANIMAL_FRIENDSHIP = 'SPPR114'
        CLERIC_ENDURE_HEAT_COLD = 'SPPR115'
        CLERIC_SPIRIT_WARD = 'SPPR150'
        CLERIC_AID = 'SPPR201'
        CLERIC_BARKSKIN = 'SPPR202'
        CLERIC_CHANT = 'SPPR203'
        CLERIC_CHARM_PERSON = 'SPPR204'
        CLERIC_FIND_TRAPS = 'SPPR205'
        CLERIC_FLAME_BLADE = 'SPPR206'
        CLERIC_GOOD_BERRIES = 'SPPR207'
        CLERIC_HOLD_PERSON = 'SPPR208'
        CLERIC_KNOW_ALIGNMENT = 'SPPR209'
        CLERIC_RESIST_FIRE = 'SPPR210'
        CLERIC_SILENCE_15_FOOT = 'SPPR211'
        CLERIC_SLOW_POISON = 'SPPR212'
        CLERIC_SPIRITUAL_HAMMER = 'SPPR213'
        CLERIC_DRAW_UPON_HOLY_MIGHT = 'SPPR214'
        CLERIC_RESIST_COLD = 'SPPR215'
        CLERIC_WRITHING_FOG = 'SPPR250'
        CLERIC_ANIMATE_DEAD = 'SPPR301'
        CLERIC_CALL_LIGHTNING = 'SPPR302'
        CLERIC_DISPEL_MAGIC = 'SPPR303'
        CLERIC_GLYPH_OF_WARDING = 'SPPR304'
        CLERIC_HOLD_ANIMAL = 'SPPR305'
        CLERIC_PROTECTION_FROM_FIRE = 'SPPR306'
        CLERIC_REMOVE_CURSE = 'SPPR307'
        CLERIC_REMOVE_PARALYSIS = 'SPPR308'
        CLERIC_INVISIBILITY_PURGE = 'SPPR309'
        CLERIC_MISCAST_MAGIC = 'SPPR310'
        CLERIC_RIGID_THINKING = 'SPPR311'
        CLERIC_STRENGTH_OF_ONE = 'SPPR312'
        CLERIC_HOLY_SMITE = 'SPPR313'
        CLERIC_UNHOLY_BLIGHT = 'SPPR314'
        CLERIC_CURE_MEDIUM_WOUNDS = 'SPPR315'
        CLERIC_CURE_BLIND_DEAF = 'SPPR316'
        CLERIC_CURE_DISEASE = 'SPPR317'
        CLERIC_ZONE_OF_SWEET_AIR = 'SPPR318'
        CLERIC_SUMMON_INSECTS = 'SPPR319'
        CLERIC_SPIRITUAL_CLARITY = 'SPPR350'
        CLERIC_CURE_SERIOUS_WOUNDS = 'SPPR401'
        CLERIC_ANIMAL_SUMMONING_1 = 'SPPR402'
        CLERIC_FREE_ACTION = 'SPPR403'
        CLERIC_NEUTRALIZE_POISON = 'SPPR404'
        CLERIC_MENTAL_DOMINATION = 'SPPR405'
        CLERIC_DEFENSIVE_HARMONY = 'SPPR406'
        CLERIC_PROTECTION_FROM_LIGHTNING = 'SPPR407'
        CLERIC_PROTECTION_FROM_EVIL_10_FOOT = 'SPPR408'
        CLERIC_DEATH_WARD = 'SPPR409'
        CLERIC_CALL_WOODLAND_BEINGS = 'SPPR410'
        CLERIC_POISON = 'SPPR411'
        CLERIC_HOLY_POWER = 'SPPR412'
        CLERIC_NEGATIVE_PLANE_PROTECTION = 'SPPR413'
        CLERIC_CAUSE_SERIOUS_WOUNDS = 'SPPR414'
        CLERIC_FAR_SIGHT = 'SPPR415'
        CLERIC_CLOAK_OF_FEAR = 'SPPR416'
        CLERIC_LESSER_RESTORATION = 'SPPR417'
        CLERIC_SPIRIT_FIRE = 'SPPR450'
        CLERIC_ANIMAL_SUMMONING_2 = 'SPPR501'
        CLERIC_CURE_CRITICAL_WOUNDS = 'SPPR502'
        CLERIC_FLAME_STRIKE = 'SPPR503'
        CLERIC_RAISE_DEAD = 'SPPR504'
        CLERIC_TRUE_SIGHT = 'SPPR505'
        CLERIC_IRONSKIN = 'SPPR506'
        CLERIC_CHAMPIONS_STRENGTH = 'SPPR507'
        CLERIC_CHAOTIC_COMMANDS = 'SPPR508'
        CLERIC_MAGIC_RESISTANCE = 'SPPR509'
        CLERIC_CAUSE_CRITICAL_WOUNDS = 'SPPR510'
        CLERIC_SLAY_LIVING = 'SPPR511'
        CLERIC_GREATER_COMMAND = 'SPPR512'
        CLERIC_RIGHTEOUS_MAGIC = 'SPPR513'
        CLERIC_MASS_CURE = 'SPPR514'
        CLERIC_REPULSE_UNDEAD = 'SPPR515'
        CLERIC_PIXIE_DUST = 'SPPR516'
        CLERIC_INSECT_PLAGUE = 'SPPR517'
        CLERIC_RECALL_SPIRIT = 'SPPR550'
        CLERIC_AERIAL_SERVANT = 'SPPR601'
        CLERIC_ANIMAL_SUMMONING_3 = 'SPPR602'
        CLERIC_BLADE_BARRIER = 'SPPR603'
        CLERIC_CONJURE_ANIMALS = 'SPPR604'
        CLERIC_CONJURE_FIRE_ELEMENTAL = 'SPPR605'
        CLERIC_FIRE_SEEDS = 'SPPR606'
        CLERIC_HEAL = 'SPPR607'
        CLERIC_HARM = 'SPPR608'
        CLERIC_FALSE_DAWN = 'SPPR609'
        CLERIC_DOLOROUS_DECAY = 'SPPR610'
        CLERIC_WONDROUS_RECALL = 'SPPR611'
        CLERIC_BOLT_OF_GLORY = 'SPPR612'
        CLERIC_PHYSICAL_MIRROR = 'SPPR613'
        CLERIC_SOL_SEARING_ORB = 'SPPR614'
        CLERIC_SPIRITUAL_LOCK = 'SPPR650'
        CLERIC_SHIELD_OF_THE_ARCHONS = 'SPPR701'
        CLERIC_CONJURE_EARTH_ELEMENTAL = 'SPPR702'
        CLERIC_GATE = 'SPPR703'
        CLERIC_NATURE_BEAUTY = 'SPPR704'
        CLERIC_FIRE_STORM = 'SPPR705'
        CLERIC_SYMBOL_FEAR = 'SPPR706'
        CLERIC_SUNRAY = 'SPPR707'
        CLERIC_FINGER_OF_DEATH = 'SPPR708'
        CLERIC_CONFUSION = 'SPPR709'
        CLERIC_HOLY_WORD = 'SPPR710'
        CLERIC_REGENERATE = 'SPPR711'
        CLERIC_RESURRECTION = 'SPPR712'
        CLERIC_RESTORATION = 'SPPR713'
        CLERIC_ENERGY_DRAIN = 'SPPR714'
        CLERIC_UNHOLY_WORD = 'SPPR715'
        CLERIC_SPACE_WARP = 'SPPR716'
        CLERIC_CREEPING_DOOM = 'SPPR717'
        CLERIC_SYMBOL_STUN = 'SPPR718'
        CLERIC_SYMBOL_DEATH = 'SPPR719'
        CLERIC_EARTHQUAKE = 'SPPR720'
        CLERIC_ENERGY_BLADES = 'SPPR721'
        CLERIC_STORM_OF_VENGEANCE = 'SPPR722'
        CLERIC_ELEMENTAL_SWARM = 'SPPR723'
        CLERIC_GREATER_ELEMENTAL_SWARM = 'SPPR724'
        CLERIC_GLOBE_OF_BLADES = 'SPPR725'
        CLERIC_SUMMON_DEVA = 'SPPR726'
        CLERIC_SUMMON_FALLEN_DEVA = 'SPPR727'
        CLERIC_IMPLOSION = 'SPPR728'
        CLERIC_MASS_RAISE_DEAD = 'SPPR729'
        CLERIC_AURA_OF_FLAMING_DEATH = 'SPPR730'
        CLERIC_ELEMENTAL_TRANSFORMATION_FIRE = 'SPPR731'
        CLERIC_ELEMENTAL_TRANSFORMATION_EARTH = 'SPPR732'
        CLERIC_ETHER_GATE = 'SPPR750'
        CLERIC_ETHEREAL_RETRIBUTION = 'SPPR751'

    class Magic_KENSAI(Enum):

        KENSAI_KIA = 'SPCL144'

    class Magic_WISH(Enum):

        WISH_SPELL_FAILURE = 'SPIN731'
        WISH_LOSE_SPELL = 'SPIN732'
        WISH_POISON = 'SPIN733'
        WISH_HEAL_PARTY = 'SPIN734'
        WISH_RABBIT = 'SPIN735'
        WISH_GLOBE = 'SPIN736'
        WISH_MEMORIZE = 'SPIN737'
        WISH_PLANE = 'SPIN738'

    class Magic_TRAP(Enum):

        TRAP_DIRE_CHARM = 'SPPR982'
        TRAP_CONFUSION = 'SPPR983'
        TRAP_CHROMATIC_ORB = 'SPPR984'
        TRAP_FLAMESTRIKE = 'SPPR985'
        TRAP_MISCAST_MAGIC = 'SPPR986'
        TRAP_CALL_LIGHTNING = 'SPPR987'
        TRAP_SILENCE = 'SPPR988'
        TRAP_HOLD_PERSON = 'SPPR989'
        TRAP_FIREBALL = 'SPWI001'
        TRAP_LIGHTNING_BOLT = 'SPWI002'
        TRAP_MAGIC_MISSILE = 'SPWI003'
        TRAP_STINKING_CLOUD = 'SPWI004'
        TRAP_ARROW = 'SPWI005'
        TRAP_ARROW_SLAYING = 'SPWI006'
        TRAP_ARROW_ACID = 'SPWI007'
        TRAP_ARROW_BITING = 'SPWI008'
        TRAP_ARROW_DETONATION = 'SPWI009'
        TRAP_ARROW_DISPELLING = 'SPWI010'
        TRAP_ARROW_FIRE = 'SPWI011'
        TRAP_ARROW_ICE = 'SPWI012'
        TRAP_ARROW_PIERCING = 'SPWI013'
        TRAP_MONSTER_SUMMONING = 'SPWI014'
        TRAP_FROST = 'SPWI015'
        TRAP_CLOUDKILL = 'SPWI016'
        TRAP_MINOR_LIGHTNING_BOLT = 'SPWI017'
        TRAP_UNDERWATER_BITE = 'SPWI020'
        TRAP_HALLWAY_SPIKES = 'SPWI021'
        TRAP_MUCK = 'SPWI022'
        TRAP_SHADOW_DEATH = 'SPWI023'
        TRAP_GUILLOTINE = 'SPWI024'
        TRAP_LIGHTNING_ORB1 = 'SPWI025'
        TRAP_LIGHTNING_ORB2 = 'SPWI026'
        TRAP_LIGHTNING_ORB3 = 'SPWI027'
        TRAP_PENDULUM = 'SPIN705'
        TRAP_VENT = 'SPIN706'
        TRAP_DARTS = 'SPIN707'
        TRAP_SLIME = 'SPIN708'
        TRAP_SPEAR = 'SPIN709'

    class Magic_TALOS(Enum):

        TALOS_STORMSHIELD = 'SPCL721'
        TALOS_LIGHTNING_BOLT = 'SPCL722'

    class Magic_SUN(Enum):

        SUN_SOUL_SUN_SOULRAY = 'SPCL236'
        SUN_SOUL_GREATER_SUN = 'SPCL237'
        SUN_SOUL_SUN_SOULBEAM = 'SPCL239'

    class Magic_HELM(Enum):

        HELM_RITUAL_SCROLL = 'SPIN592'
        HELM_SEEKING_SWORD = 'SPCL731'
        HELM_TRUE_SIGHT = 'SPCL732'