from enum import Enum

class Tables:
    
    class Class(Enum):
        MAGE = 0x01
        FIGHTER = 0x02
        CLERIC = 0x03
        THIEF = 0x04
        BARD = 0x05
        PALADIN = 0x06
        FIGHTER_MAGE = 0x07
        FIGHTER_CLERIC = 0x08
        FIGHTER_THIEF = 0x09
        FIGHTER_MAGE_THIEF = 0x0A
        DRUID = 0x0B
        RANGER = 0x0C
        MAGE_THIEF = 0x0D
        CLERIC_MAGE = 0x0E
        CLERIC_THIEF = 0x0F
        FIGHTER_DRUID = 0x10
        FIGHTER_MAGE_CLERIC = 0x11
        CLERIC_RANGER = 0x12
        SORCERER = 0x13
        MONK = 0x14
        ANKHEG = 0x65
        BASILISK = 0x66
        BASILISK_GREATER = 0x67
        BEAR_BLACK = 0x68
        BEAR_BROWN = 0x69
        BEAR_CAVE = 0x6A
        BEAR_POLAR = 0x6B
        CARRIONCRAWLER = 0x6C
        DOG_WILD = 0x6D
        DOG_WAR = 0x6E
        DOPPLEGANGER = 0x6F
        DOPPLEGANGER_GREATER = 0x70
        DRIZZT = 0x71
        ELMINSTER = 0x72
        ETTERCAP = 0x73
        GHOUL = 0x74
        GHOUL_REVEANT = 0x75
        GHOUL_GHAST = 0x76
        GIBBERLING = 0x77
        GNOLL = 0x78
        HOBGOBLIN = 0x79
        KOBOLD = 0x7A
        KOBOLD_TASLOI = 0x7B
        KOBOLD_XVART = 0x7C
        OGRE = 0x7D
        OGRE_MAGE = 0x7E
        OGRE_HALFOGRE = 0x7F
        OGRE_OGRILLON = 0x80
        SAREVOK = 0x81
        FAIRY_SIRINE = 0x82
        FAIRY_DRYAD = 0x83
        FAIRY_NEREID = 0x84
        FAIRY_NYMPH = 0x85
        SKELETON = 0x86
        SKELETON_WARRIOR = 0x87
        SKELETON_BANEGUARD = 0x88
        SPIDER_GIANT = 0x89
        SPIDER_HUGE = 0x8A
        SPIDER_PHASE = 0x8B
        SPIDER_SWORD = 0x8C
        SPIDER_WRAITH = 0x8D
        VOLO = 0x8E
        WOLF = 0x8F
        WOLF_WORG = 0x90
        WOLF_DIRE = 0x91
        WOLF_WINTER = 0x92
        WOLF_VAMPIRIC = 0x93
        WOLF_DREAD = 0x94
        WYVERN = 0x95
        OLIVE_SLIME = 0x96
        MUSTARD_JELLY = 0x97
        OCRE_JELLY = 0x98
        GREY_OOZE = 0x99
        GREEN_SLIME = 0x9A
        INNOCENT = 0x9B
        FLAMING_FIST = 0x9C
        WEREWOLF = 0x9D
        WOLFWERE = 0x9E
        DEATHKNIGHT = 0x9F
        TANARI = 0xA0
        BEHOLDER = 0xA1
        MIND_FLAYER = 0xA2
        VAMPIRE = 0xA3
        VAMPYRE = 0xA4
        OTYUGH = 0xA5
        RAKSHASA = 0xA6
        TROLL = 0xA7
        UMBERHULK = 0xA8
        SAHUAGIN = 0xA9
        SHADOW = 0xAA
        SPECTRE = 0xAB
        WRAITH = 0xAC
        KUO_TOA = 0xAD
        MIST = 0xAE
        CAT = 0xAF
        DUERGAR = 0xB0
        MEPHIT = 0xB1
        MIMIC = 0xB2
        IMP = 0xB3
        GIANT = 0xB4
        ORC = 0xB5
        GOLEM_IRON = 0xB6
        GOLEM_FLESH = 0xB7
        GOLEM_STONE = 0xB8
        GOLEM_CLAY = 0xB9
        ELEMENTAL_AIR = 0xBA
        ELEMENTAL_FIRE = 0xBB
        ELEMENTAL_EARTH = 0xBC
        SPIDER_CENTEOL = 0xBD
        RED_DRAGON = 0xBE
        SHADOW_DRAGON = 0xBF
        SILVER_DRAGON = 0xC0
        GENIE_DJINNI = 0xC1
        GENIE_DAO = 0xC2
        GENIE_EFREETI = 0xC3
        GENIE_NOBLE_DJINNI = 0xC4
        GENIE_NOBLE_EFREETI = 0xC5
        ZOMBIE_NORMAL = 0xC6
        FOOD_CREATURE = 0xC7
        HUNTER_CREATURE = 0xC8
        LONG_SWORD = 0xC9
        LONG_BOW = 0xCA
        MAGE_ALL = 0xCA
        FIGHTER_ALL = 0xCB
        CLERIC_ALL = 0xCC
        THIEF_ALL = 0xCD
        BARD_ALL = 0xCE
        PALADIN_ALL = 0xCF
        DRUID_ALL = 0xD0
        RANGER_ALL = 0xD1
        WIZARD_EYE = 0xD2
        CANDLEKEEP_WATCHER = 0xD3
        AMNISH_SOLDIER = 0xD4
        TOWN_GUARD = 0xD5
        NO_CLASS = 0xFF
        
    class Alignment(Enum):
        NONE = 0x00
        MASK_GOOD = 0x01
        MASK_GENEUTRAL = 0x02
        MASK_EVIL = 0x03
        MASK_LAWFUL = 0x10
        LAWFUL_GOOD = 0x11
        LAWFUL_NEUTRAL = 0x12
        LAWFUL_EVIL = 0x13
        MASK_LCNEUTRAL = 0x20
        NEUTRAL_GOOD = 0x21
        NEUTRAL = 0x22
        NEUTRAL_EVIL = 0x23
        MASK_CHAOTIC = 0x30
        CHAOTIC_GOOD = 0x31
        CHAOTIC_NEUTRAL = 0x32
        CHAOTIC_EVIL = 0x33
        
    class Gender(Enum):
        MALE = 0x01
        FEMALE = 0x02
        OTHER = 0x03
        NIETHER = 0x04
        BOTH = 0x05
        SUMMONED = 0x06
        ILLUSIONARY = 0x07
        EXTRA = 0x08
        SUMMONED_DEMON = 0x09
        
    class Race(Enum):
        NONE = 0
        HUMAN = 0x01
        ELF = 0x02
        HALF_ELF = 0x03
        DWARF = 0x04
        HALFLING = 0x05
        GNOME = 0x06
        HALFORC = 0x07
        ANKHEG = 0x65
        BASILISK = 0x66
        BEAR = 0x67
        CARRIONCRAWLER = 0x68
        DOG = 0x69
        DOPPLEGANGER = 0x6A
        ETTERCAP = 0x6B
        GHOUL = 0x6C
        GIBBERLING = 0x6D
        GNOLL = 0x6E
        HOBGOBLIN = 0x6F
        KOBOLD = 0x70
        OGRE = 0x71
        SKELETON = 0x73
        SPIDER = 0x74
        WOLF = 0x75
        WYVERN = 0x76
        SLIME = 0x77
        FAIRY = 0x78
        DEMONIC = 0x79
        LYCANTHROPE = 0x7A
        BEHOLDER = 0x7B
        MIND_FLAYER = 0x7C
        VAMPIRE = 0x7D
        VAMPYRE = 0x7E
        OTYUGH = 0x7F
        RAKSHASA = 0x80
        TROLL = 0x81
        UMBERHULK = 0x82
        SAHUAGIN = 0x83
        SPECTRE = 0x85
        WRAITH = 0x86
        KUO_TOA = 0x87
        MIST = 0x88
        CAT = 0x89
        DUERGAR = 0x8A
        MEPHIT = 0x8B
        MIMIC = 0x8C
        IMP = 0x8D
        GIANT = 0x8E
        ORC = 0x8F
        GOLEM = 0x90
        ELEMENTAL = 0x91
        DRAGON = 0x92
        GENIE = 0x93
        ZOMBIE = 0x94
        SHADOW = 0x95
        LICH = 0x96
        RABBIT = 0x97
        GITHYANKI = 0x98
        TIEFLING = 0x99
        YUANTI = 0x9A
        DEMILICH = 0x9B
        SOLAR = 0x9C
        ANTISOLAR = 0x9D
        PLANATAR = 0x9E
        DARKPLANATAR = 0x9F
        SWORD = 0xC9
        BOW = 0xCA
        XBOW = 0xCB
        STAFF = 0xCC
        SLING = 0xCD
        MACE = 0xCE
        DAGGER = 0xCF
        SPEAR = 0xD0
        FIST = 0xD1
        HAMMER = 0xD2
        MORNINGSTAR = 0xD3
        ROBES = 0xD4
        LEATHER = 0xD5
        CHAIN = 0xD6
        PLATE = 0xD7
        NO_RACE = 0xFF
        
    class State(Enum):
        STATE_NORMAL = 0x0000
        STATE_SLEEPING = 0x0001
        STATE_BERSERK = 0x0002
        STATE_PANIC = 0x0004
        STATE_STUNNED = 0x0008
        STATE_INVISIBLE = 0x0010
        STATE_HELPLESS = 0x0020
        STATE_IMMOBILE = 0x0029
        STATE_FROZEN_DEATH = 0x0040
        STATE_STONE_DEATH = 0x0080
        STATE_EXPLODING_DEATH = 0x0100
        STATE_FLAME_DEATH = 0x0200
        STATE_ACID_DEATH = 0x0400
        STATE_DEAD = 0x0800
        STATE_REALLY_DEAD = 0x0FC0
        STATE_SILENCED = 0x1000
        STATE_CHARMED = 0x2000
        STATE_POISONED = 0x4000
        STATE_HASTED = 0x8000
        STATE_SLOWED = 0x10000
        STATE_INFRAVISION = 0x20000
        STATE_BLIND = 0x40000
        STATE_DISEASED = 0x80000
        STATE_FEEBLEMINDED = 0x100000
        STATE_HARMLESS = 0x102029
        STATE_NONDETECTION = 0x200000
        STATE_IMPROVEDINVISIBILITY = 0x400000
        STATE_NOT_TARGETABLE = 0x400010
        STATE_BLESS = 0x800000
        STATE_CHANT = 0x1000000
        STATE_DRAWUPONHOLYMIGHT = 0x2000000
        STATE_LUCK = 0x4000000
        STATE_AID = 0x8000000
        STATE_CHANTBAD = 0x10000000
        STATE_BLUR = 0x20000000
        STATE_MIRRORIMAGE = 0x40000000
        STATE_ILLUSIONS = 0x60400010
        STATE_CONFUSED = 0x80000000
        STATE_NOT_APPROACHABLE = 0x80002006
        STATE_RANGED_TARGET = 0x80040004
        CD_STATE_NOTVALID = 0x80101FEF
        STATE_DISABLED = 0x8010202D
        STATE_DISABLED_CASTING = 0x8010302D
        STATE_DEBUFF = 0x8015302D
        
    class Kit(Enum):
        NONE = 0x00000000
        BARBARIAN = 0x00004000
        MAGESCHOOL_WILDMAGE = 0x00008000
        MAGESCHOOL_ABJURER = 0x00400000
        MAGESCHOOL_CONJURER = 0x00800000
        MAGESCHOOL_DIVINER = 0x01000000
        MAGESCHOOL_ENCHANTER = 0x02000000
        MAGESCHOOL_ILLUSIONIST = 0x04000000
        MAGESCHOOL_INVOKER = 0x08000000
        MAGESCHOOL_NECROMANCER = 0x10000000
        MAGESCHOOL_TRANSMUTER = 0x20000000
        TRUECLASS = 0x40000000
        MAGESCHOOL_GENERALIST = 0x40000000
        BERSERKER = 0x40010000
        WIZARDSLAYER = 0x40020000
        KENSAI = 0x40030000
        CAVALIER = 0x40040000
        INQUISITOR = 0x40050000
        UNDEADHUNTER = 0x40060000
        FERALAN = 0x40070000
        STALKER = 0x40080000
        BEASTMASTER = 0x40090000
        ASSASIN = 0x400A0000
        BOUNTYHUNTER = 0x400B0000
        SWASHBUCKLER = 0x400C0000
        BLADE = 0x400D0000
        JESTER = 0x400E0000
        SKALD = 0x400F0000
        TOTEMIC = 0x40100000
        SHAPESHIFTER = 0x40110000
        BEASTFRIEND = 0x40120000
        GODTALOS = 0x40130000
        GODHELM = 0x40140000
        GODLATHANDER = 0x40150000
        BLACKGUARD = 0x40200000
        SHADOWDANCER = 0x40210000
        DWARVEN_DEFENDER = 0x40220000
        DRAGON_DISCIPLE = 0x40230000
        DARK_MOON = 0x40240000
        SUN_SOUL = 0x40250000
        GRIZZLY_BEAR = 0x40270000
        OHTYR = 0x40280000
        
    class Target(Enum):
        NONE = 0
        SELF_PRE = 1
        PRE_TARGET = 2
        PARTY = 3
        EVERYONE_PARTY = 4
        EVERYONE_NOPARTY = 5
        EVERYONE_MATCH_CASTER = 6
        EVERYONE_MATCH_TARGET = 7
        EVERYONE_NOCASTER = 8
        SELF_POST = 9  

    class Time(Enum):
        DURATION = 0
        PERMANENT = 1
        EQUIPPED = 2
        DELAYED_DURATION = 3
        DELAYED = 4
        DELAYED_PERMANENT = 5
        DURATION_2 = 6
        PERMANENT_2 = 7
        PERMANENT_UNSAVED = 8
        PERMANENT_AFTER_DEATH = 9
        TRIGGER = 10
        ABSOLUTE = 4096

    class WeaponType(Enum):
        BastardSword = 89
        LongSword = 90
        ShortSword = 91
        Axe = 92
        TwoHandedSword = 93
        Katana = 94
        ScimitarWakizashiNinjaTo = 95
        Dagger = 96
        WarHammer = 97
        Spear = 98
        Halberd = 99
        FlailMorningstar = 100
        Mace = 101
        QuarterStaff = 102
        Crossbow = 103
        LongBow = 104
        ShortBow = 105
        Darts = 106
        Sling = 107
        #Blackjack = 108
        #Gun = 109
        #MartialArts = 110
        TwoHandedWeaponSkill = 111
        SwordandShieldSkill = 112
        SingleWeaponSkill = 113
        TwoWeaponSkill = 114
        Club = 115
        #ExtraProficiency2 = 116
        #ExtraProficiency3 = 117
        #ExtraProficiency4 = 118
        #ExtraProficiency5 = 119
        #ExtraProficiency6 = 120
        #ExtraProficiency7 = 121
        #ExtraProficiency8 = 122
        #ExtraProficiency9 = 123
        #ExtraProficiency10 = 124
        #ExtraProficiency11 = 125
        #ExtraProficiency12 = 126
        #ExtraProficiency13 = 127
        #ExtraProficiency14 = 128
        #ExtraProficiency15 = 129
        #ExtraProficiency16 = 130
        #ExtraProficiency17 = 131
        #ExtraProficiency18 = 132
        #ExtraProficiency19 = 133
        #ExtraProficiency20 = 134