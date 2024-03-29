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

    class Script(Enum):   
        NULL = 0x0
        AJANTIS = 0x5349544E414A41
        ALORA = 0x61726F6C61
        BDAERIEC = 0x4345495245414442
        BDANOMEC = 0x43454D4F4E414442
        BDCERNDC = 0x43444E5245434442
        BDDEFAI = 0x49414645444442
        BDDORNC = 0x434E524F444442
        BDEDWINC = 0x434E495744454442
        BDHAERC = 0x43524541484442
        BDHEXXAC = 0x4341585845484442
        BDIMOENC = 0x434E454F4D494442
        BDJAHEIC = 0x43494548414A4442
        BDJANC = 0x434E414A4442
        BDKELDOC = 0x434F444C454B4442
        BDKORGAC = 0x434147524F4B4442
        BDMAZZYC = 0x43595A5A414D4442
        BDMINSCC = 0x4343534E494D4442
        BDNALIAC = 0x4341494C414E4442
        BDNEERAC = 0x43415245454E4442
        BDRASAAC = 0x4341415341524442
        BDSAREVC = 0x4356455241534442
        BDVALYGC = 0x4347594C41564442
        BDVICONC = 0x434E4F4349564442
        BDWILSOC = 0x434F534C49574442
        BDYOSHIC = 0x434948534F594442
        BPPLOT = 0x544F4C505042
        BRANWEN = 0x6E65776E617262
        CORAN = 0x6E61726F43
        DPLAYER = 0x524559414C5044
        DPLAYER3 = 0x33524559414C5044
        DYNAHEIR = 0x52494548414E5944
        EDWIN = 0x6E69776445
        ELDOTH = 0x48544F444C45
        FALDORN = 0x6E726F646C6166
        GARRICK = 0x6B636972726167
        IMOEN = 0x6E656F6D69
        INITDLG = 0x474C4454494E49
        INITOBE = 0x45424F54494E49
        JAHEIRA = 0x6172696568614A
        KAGAIN = 0x6E696167614B
        KHALID = 0x64696C61684B
        KIVAN = 0x4E4156494B
        MAGE1 = 0x314547414D
        MAGE5 = 0x354547414D
        MINSC = 0x63736E694D
        MONTARON = 0x6E6F7261746E6F4D
        NONE = 0x656E6F4E
        PRIEST1 = 0x31545345495250
        PRIEST2 = 0x32545345495250
        QUAYLE = 0x454C59415551
        SAFANA = 0x414E41464153
        SHARTEEL = 0x4C45455452414853
        SHOUT = 0x54554F4853
        SKIE = 0x65696B73
        TIAX = 0x58414954
        TTBRAN = 0x6E6172627474
        TTIMOEN = 0x6E656F6D697474
        TTJAHEIR = 0x72696568616A7474
        TTMINSC = 0x63736E696D7474
        TTXAN = 0x4E41585454
        VICONIA = 0x41494E4F434956
        WTARSGT = 0x54475352415457
        WTASIGHT = 0x5448474953415457
        WTASIGHT2 = 0x7468676973617477
        WTRUNSGT = 0x5447534E55525457
        XAN = 0x6E6178
        XZAR = 0x52415A58
        YESLICK = 0x6B63696C736579
        
    class Effects(Enum):
        Stat_AC_vs_Damage_Type_Modifier_Variants_IWD2 = 0x0
        Stat_Attacks_Per_Round_Modifier_Variants_BG1 = 0x1
        Cure_Sleep = 0x2
        State_Berserking_Variants_IWD1 = 0x3
        Cure_Berserking = 0x4
        Charm_Charm_Specific_Creature_Variants_IWD1_IWD2_PST = 0x5
        Stat_Charisma_Modifier_Variants_IWD1_PST = 0x6
        Colour_Set_Character_colours_by_Palette_Variants_IWD1 = 0x7
        Colour_Change_by_RGB_Variants_BG1_IWD1_PST = 0x8
        Colour_Glow_Pulse_Variants_BG1_IWD1_PST = 0x9
        Stat_Constitution_Modifier_Variants_IWD1_PST = 0xA
        Cure_Poison = 0xB
        HP_Damage_Variants_BG2_PST_BG1 = 0xC
        Death_Instant_Death_Variants_BG1_IWD1_PST = 0xD
        Graphics_Defrost_Variants_PST_BG1 = 0xE
        Stat_Dexterity_Modifier_Variants_IWD1_IWD2_PST = 0xF
        State_Haste_Variants_BG1_IWD1 = 0x10
        HP_Current_HP_Modifier_Variants_IWD2_BG1 = 0x11
        HP_Maximum_HP_Modifier = 0x12
        Stat_Intelligence_Modifier_Variants_IWD1 = 0x13
        State_Invisibility_Variants_BG1_IWD1_IWD2_PST = 0x14
        Stat_Lore_Modifier_Variants_IWD2 = 0x15
        Stat_Cumulative_Luck_Bonus_Variants_IWD1_PST = 0x16
        Stat_Morale_Modifier_Variants_BG1 = 0x17
        State_Horror_Variants_IWD1 = 0x18
        State_Poison_Variants_BG1_IWD1_IWD2_PST = 0x19
        Item_Remove_Curse_Variants_PST = 0x1A
        Stat_Acid_Resistance_Modifier_Variants_IWD2 = 0x1B
        Stat_Cold_Resistance_Modifier_Variants_IWD2 = 0x1C
        Stat_Electricity_Resistance_Modifier_Variants_IWD2 = 0x1D
        Stat_Fire_Resistance_Modifier_Variants_IWD2 = 0x1E
        Stat_Magic_Damage_Resistance_Modifier_Variants_BG1 = 0x1F
        Cure_Death_Raise_Dead_Variants_IWD2 = 0x20
        Stat_Save_vs_Death_Modifier_Variants_IWD2 = 0x21
        Stat_Save_vs_Wands_Modifier_Variants_IWD2 = 0x22
        Stat_Save_vs_Petrification_Polymorph_Modifier_Variants_IWD2 = 0x23
        Stat_Save_vs_Breath_Weapons_Modifier_Variants_IWD2 = 0x24
        Stat_Save_vs_Spells_Modifier_Variants_IWD2 = 0x25
        State_Silence = 0x26
        State_Unconsciousness_Variants_IWD2_PST = 0x27
        State_Slow = 0x28
        Graphics_Sparkle_Variants_BG1_IWD1_IWD2_PST = 0x29
        Spell_Wizard_Spell_Slots_Modifier_Variants_IWD1 = 0x2A
        Cure_Stone_to_Flesh = 0x2B
        Stat_Strength_Modifier_Variants_IWD1_IWD2_PST = 0x2C
        State_Stun_Variants_IWD1 = 0x2D
        Cure_Stun_Unstun_Variants_PST = 0x2E
        Cure_Invisibility = 0x2F
        Cure_Silence_Vocalize = 0x30
        Stat_Wisdom_Modifier_Variants_IWD1_PST = 0x31
        Colour_Glow_by_RGB_Brief_Variants_BG1_IWD1_IWD2_PST = 0x32
        Colour_Strong_Dark_by_RGB_Variants_BG1_IWD1_IWD2 = 0x33
        Colour_Very_Bright_by_RGB_Variants_BG1_IWD1_IWD2_PST = 0x34
        Graphics_Animation_Change_Variants_IWD1_IWD2_PST = 0x35
        Stat_THAC0_Modifier_Variants_IWD2 = 0x36
        Death_Kill_Creature_Type_Variants_PST = 0x37
        Alignment_Invert_Variants_PST = 0x38
        Alignment_Change_Variants_PST = 0x39
        Cure_Dispellable_Effects_Dispel_Magic = 0x3A
        Stat_Stealth_Modifier = 0x3B
        Stat_Miscast_Magic_Variants_IWD1_BG1 = 0x3C
        Crash_Variants_IWD2 = 0x3D
        Spell_Priest_Spell_Slots_Modifier_Variants_IWD1 = 0x3E
        State_Infravision = 0x3F
        State_Remove_Infravision = 0x40
        Overlay_Blur = 0x41
        Graphics_Transparency_Fade_Variants_IWD1_PST = 0x42
        Summon_Creature_Summoning_Variants_IWD2_PST = 0x43
        Summon_Unsummon_Creature = 0x44
        Protection_From_Detection_Non_Detection = 0x45
        Cure_Non_Detection_Variants_IWD2_PST = 0x46
        IDS_Sex_Change = 0x47
        IDS_Set_IDS_State_Variants_BG1_IWD2_PST = 0x48
        Stat_Extra_Damage_Modifier_Variants_IWD1 = 0x49
        State_Blindness_Variants_BG1 = 0x4A
        Cure_Blindness = 0x4B
        State_Feeblemindedness_Variants_IWD2 = 0x4C
        Cure_Feeblemindedness = 0x4D
        State_Disease_Variants_BG1_BG2_IWD1_PST = 0x4E
        Cure_Disease = 0x4F
        State_Deafness_Variants_IWD2 = 0x50
        Cure_Deafness = 0x51
        Set_AI_Script_Variants_PST = 0x52
        Protection_From_Projectile_Variants_BG1_IWD1_IWD2_PST = 0x53
        Stat_Magical_Fire_Resistance_Modifier_Variants_IWD1_IWD2 = 0x54
        Stat_Magical_Cold_Resistance_Modifier_Variants_IWD1_IWD2 = 0x55
        Stat_Slashing_Resistance_Modifier_Variants_IWD2 = 0x56
        Stat_Crushing_Resistance_Modifier_Variants_IWD2 = 0x57
        Stat_Piercing_Resistance_Modifier_Variants_IWD2 = 0x58
        Stat_Missiles_Resistance_Modifier_Variants_IWD2 = 0x59
        Stat_Open_Locks_Modifier = 0x5A
        Stat_Find_Traps_Modifier = 0x5B
        Stat_Pick_Pockets_Modifier = 0x5C
        Stat_Fatigue_Modifier = 0x5D
        Stat_Drunkenness_Modifier = 0x5E
        Stat_Tracking_Skill_Modifier = 0x5F
        Stat_Level_Change_Variants_BG1 = 0x60
        Stat_Strength_Bonus_Modifier = 0x61
        HP_Regeneration_Variants_BG1_IWD1_IWD2_PST = 0x62
        Spell_Effect_Duration_Modifier = 0x63
        Protection_from_Creature_Type_Variants_IWD2 = 0x64
        Protection_from_Opcode = 0x65
        Protection_from_Spell_Levels = 0x66
        Text_Change_Name = 0x67
        Stat_Experience_Points = 0x68
        Stat_Gold_Variants_BG1 = 0x69
        Stat_Morale_Break_Modifier = 0x6A
        Portrait_Change = 0x6B
        Stat_Reputation = 0x6C
        State_Hold_Variants_BG2_PST_BG1 = 0x6D
        Empty_Variants_BG1_IWD2_PST = 0x6E
        Item_Create_Magical_Weapon = 0x6F
        Item_Remove_Item = 0x70
        Empty_Variants_BG1 = 0x71
        Graphics_Dither_Variants_IWD1 = 0x72
        Detect_Alignment_Variants_IWD2 = 0x73
        State_Cure_Invisibility = 0x74
        Spell_Effect_Reveal_Area_Variants_IWD2 = 0x75
        Empty_Variants_BG1_1 = 0x76
        Spell_Effect_Mirror_Image_Variants_IWD1 = 0x77
        Protection_from_Melee_Weapons = 0x78
        Empty = 0x79
        Item_Create_Inventory_Item_Variants_BG1_IWD2 = 0x7A
        Item_Remove_Inventory_Item = 0x7B
        Spell_Effect_Teleport_Dimension_Door_Variants_PST_BG1 = 0x7C
        Spell_Effect_Teleport_Dimension_Door_Variants_BGEE_PST = 0x7C
        Spell_Effect_Unlock_Knock = 0x7D
        Stat_Movement_Modifier_Variants_PST = 0x7E
        Summon_Monster_Summoning_Variants_IWD2_PST = 0x7F
        State_Confusion = 0x80
        State_Aid_Variants_PST = 0x81
        State_Bless_Variants_PST = 0x82
        State_Positive_Chant_Variants_IWD2 = 0x83
        State_Raise_Strength_Constitution_Dexterity_Non_Cumulative = 0x84
        Spell_Effect_Luck_Non_Cumulative = 0x85
        State_Petrification = 0x86
        Graphics_Polymorph_into_Specific_Variants_BG1_IWD2_PST = 0x87
        State_Force_Visible = 0x88
        State_Negative_Chant_Variants_IWD2 = 0x89
        Graphics_Character_Animation_Change_Variants_BG1_IWD1_PST = 0x8A
        Text_Display_String = 0x8B
        Graphics_Casting_Glow_Variants_IWD2_PST = 0x8C
        Graphics_Lighting_Effects_Variants_IWD2_PST = 0x8D
        Graphics_Display_Special_Effect_Icon_Variants_BG1_IWD1_IWD2 = 0x8E
        Item_Create_Item_in_Slot_Variants_IWD2_PST = 0x8F
        Button_Disable_Button_Variants_BG1_IWD1_IWD2 = 0x90
        Spell_Disable_Spell_Casting_Abilities_Variants_IWD2 = 0x91
        Spell_Cast_Spell_at_Creature_Variants_IWD2_PST = 0x92
        Spell_Learn_Spell_Variants_IWD2_PST_BG1 = 0x93
        Spell_Cast_Spell_at_Point = 0x94
        Identify = 0x95
        Spell_Effect_Find_Traps = 0x96
        Summon_Replace_Creature_Variants_IWD2_PST = 0x97
        Spell_Effect_Play_Movie_Variants_BG1_IWD1_IWD2_PST = 0x98
        Overlay_Sanctuary = 0x99
        Overlay_Entangle = 0x9A
        Overlay_Minor_Globe_Variants_IWD2 = 0x9B
        Overlay_Protection_from_Normal_Missiles_Cylinder = 0x9C
        State_Web_Effect = 0x9D
        Overlay_Grease = 0x9E
        Spell_Effect_Mirror_Image_Exact_Number = 0x9F
        Remove_Sanctuary_Variants_IWD2 = 0xA0
        Cure_Horror = 0xA1
        Cure_Hold_Variants_PST = 0xA2
        Protection_Free_Action = 0xA3
        Cure_Drunkeness_Variants_BG1 = 0xA4
        Spell_Effect_Pause_Target = 0xA5
        Stat_Magic_Resistance_Modifier_Variants_BG1_PST = 0xA6
        Stat_THAC0_Modifier_with_Missile_Weapons_Variants_IWD2_PST = 0xA7
        Summon_Remove_Creature_Variants_PST = 0xA8
        Graphics_Prevent_Special_Effect_Icon_Variants_BG1_IWD1_IWD2 = 0xA9
        Graphics_Play_Damage_Animation_Variants_PST = 0xAA
        Spell_Give_Ability_Variants_PST = 0xAB
        Spell_Remove_Spell_Variants_BG1_IWD1 = 0xAC
        Stat_Poison_Resistance_Modifier = 0xAD
        Spell_Effect_Play_Sound_Effect_Variants_BG1_IWD1_PST = 0xAE
        State_Hold_Variants_BG1_IWD2_IWD1 = 0xAF
        Stat_Movement_Modifier_II = 0xB0
        Use_EFF_File = 0xB1
        Spell_Effect_THAC0_vs_Creature_Type_Modifier_Variants_PST_BG1 = 0xB2
        Spell_Effect_Damage_vs_Creature_Type_Modifier_Variants_PST_BG1 = 0xB3
        Item_Can_t_Use_Item_Variants_IWD2_PST = 0xB4
        Item_Can_t_Use_Itemtype_Variants_BG1_BG2_IWD1_IWD2_PST = 0xB5
        Item_Apply_Effect_Item = 0xB6
        Item_Apply_Effect_Itemtype_Variants_IWD2_PST = 0xB7
        Graphics_Passwall_Don_t_Jump = 0xB8
        State_Hold_Variants_BG1_IWD2_PST = 0xB9
        Script_MoveToArea_Variants_PST = 0xBA
        Script_Store_Local_Variable_Variants_BG1_PST = 0xBB
        Spell_Effect_Aura_Cleansing_Variants_PST = 0xBC
        Stat_Casting_Time_Modifier_Variants_BG1_PST = 0xBD
        Stat_Attack_Speed_Factor_Variants_PST = 0xBE
        Spell_Casting_Level_Modifier_Variants_BG2_IWD1_PST = 0xBF
        Spell_Effect_Find_Familiar_Variants_IWD1_PST = 0xC0
        Spell_Effect_Invisible_Detection_by_Script_Variants_IWD2_PST = 0xC1
        Ignore_Dialog_Pause_Variants_IWD1_IWD2_PST = 0xC2
        Spell_Effect_Death_Dependent_Constitution_Loss_Variants_IWD1_PST = 0xC3
        Spell_Effect_Familiar_Block_Variants_IWD1_PST = 0xC4
        Spell_Bounce_Projectile_Variants_IWD1_IWD2_PST = 0xC5
        Spell_Bounce_Opcode_Variants_IWD1_IWD2_PST = 0xC6
        Spell_Bounce_Spell_Level_Variants_IWD1_IWD2_PST = 0xC7
        Spell_Decrementing_Bounce_Spells_Variants_IWD1_IWD2_PST = 0xC8
        Spell_Decrementing_Spell_Immunity_Variants_IWD1_IWD2_PST = 0xC9
        Spell_Bounce_Spell_School_Variants_IWD1_IWD2_PST = 0xCA
        Spell_Bounce_Secondary_Type_Variants_IWD1_IWD2_PST = 0xCB
        Spell_Protection_from_Spell_School_Variants_IWD1_IWD2_PST = 0xCC
        Spell_Protection_from_Spell_Secondary_Type_Variants_IWD1_IWD2_PST = 0xCD
        Spell_Protection_from_Spell_Variants_IWD1_IWD2_PST = 0xCE
        Spell_Bounce_Specified_Spell_Variants_IWD1_IWD2_PST = 0xCF
        HP_Minimum_Limit_Variants_PST = 0xD0
        Death_Kill_60HP_Variants_IWD1_IWD2_PST = 0xD1
        Spell_Effect_Stun_90HP_Variants_IWD2_PST = 0xD2
        Spell_Effect_Imprisonment_Variants_IWD1_IWD2_PST = 0xD3
        Protection_Freedom_Variants_IWD1_IWD2_PST = 0xD4
        Spell_Effect_Maze_Variants_IWD1_IWD2 = 0xD5
        Spell_Effect_Select_Spell_Variants_IWD1 = 0xD6
        Graphics_Play_3D_Effect_Variants_IWD1_IWD2 = 0xD7
        Spell_Effect_Level_Drain_Variants_IWD1_IWD2 = 0xD8
        Spell_Effect_Unconsciousness_20HP_Variants_IWD1_IWD2 = 0xD9
        Protection_Stoneskin_Variants_BG2_IWD2 = 0xDA
        Stat_AC_vs_Creature_Type_Modifier_Variants_BG2_IWD1_IWD2 = 0xDB
        Removal_Remove_School_Variants_IWD1_IWD2 = 0xDC
        Removal_Remove_Secondary_Type_Variants_IWD1_IWD2 = 0xDD
        Spell_Effect_Teleport_Field_Variants_IWD1_IWD2 = 0xDE
        Spell_Effect_Immunity_School_Decrement_Variants_IWD1_IWD2 = 0xDF
        Cure_Level_Drain_Restoration_Variants_IWD1_IWD2 = 0xE0
        Spell_Reveal_Magic_Variants_IWD1_IWD2 = 0xE1
        Spell_Immunity_Secondary_Type_Decrement_Variants_IWD1_IWD2 = 0xE2
        Spell_Bounce_School_Decrement_Variants_IWD1_IWD2 = 0xE3
        Spell_Bounce_Secondary_Type_Decrement_Variants_IWD1_IWD2 = 0xE4
        Removal_Remove_One_School_Variants_IWD1_IWD2 = 0xE5
        Removal_Remove_One_Secondary_Type_Variants_IWD1_IWD2 = 0xE6
        Spell_Effect_Time_Stop_Variants_IWD1 = 0xE7
        Spell_Effect_Cast_Spell_on_Condition_Variants_BG2_IWD1_IWD2 = 0xE8
        Stat_Proficiency_Modifier_Variants_IWD1 = 0xE9
        Spell_Effect_Contingency_Creation_Variants_IWD1_IWD2 = 0xEA
        Spell_Effect_Wing_Buffet_Variants_IWD1 = 0xEB
        Spell_Effect_Image_Projection_Variants_IWD1_IWD2 = 0xEC
        Spell_Effect_Puppet_ID_Variants_IWD1_IWD2 = 0xED
        Death_Disintegrate_Variants_BG2_IWD1 = 0xEE
        Spell_Effect_Farsight_Variants_IWD1_IWD2 = 0xEF
        Graphics_Remove_Special_Effect_Icon_Variants_IWD1_IWD2 = 0xF0
        Charm_Control_Creature_Variants_IWD1 = 0xF1
        Cure_Confusion_Variants_IWD1_IWD2 = 0xF2
        Item_Drain_Item_Charges_Variants_BG2_IWD1_IWD2 = 0xF3
        Spell_Drain_Wizard_Spell_Variants_IWD1_IWD2 = 0xF4
        Check_For_Berserk_Variants_IWD1_IWD2 = 0xF5
        Spell_Effect_Berserking_Variants_IWD1_IWD2 = 0xF6
        Spell_Effect_Attack_Nearest_Creature_Variants_IWD1 = 0xF7
        Item_Set_Melee_Effect_Variants_IWD1_IWD2 = 0xF8
        Item_Set_Ranged_Effect_Variants_IWD1_IWD2 = 0xF9
        Spell_Effect_Damage_Modifier_Variants_IWD1_IWD2 = 0xFA
        Spell_Effect_Change_Bard_Song_Effect_Variants_IWD1_IWD2 = 0xFB
        Spell_Effect_Set_Trap_Variants_IWD1_IWD2 = 0xFC
        Spell_Effect_Add_Map_Marker_Variants_IWD1_IWD2 = 0xFD
        Spell_Effect_Remove_Map_Marker_Variants_IWD1 = 0xFE
        Item_Create_Inventory_Item_days_Variants_IWD1 = 0xFF
        Spell_Spell_Sequencer_Active_Variants_IWD1 = 0x100
        Spell_Spell_Sequencer_Creation_Variants_IWD1 = 0x101
        Spell_Spell_Sequencer_Activation_Variants_IWD1_IWD2 = 0x102
        Protection_Spell_Trap_Variants_IWD1_IWD2 = 0x103
        Spell_Spell_Sequencer_Activation_Variants_BG2_IWD1 = 0x104
        Spell_Restore_Lost_Spells_Variants_IWD1 = 0x105
        Stat_Visual_Range_Variants_IWD1_IWD2 = 0x106
        Stat_Backstab_Variants_IWD1 = 0x107
        Spell_Effect_Drop_Weapons_in_Panic_Variants_IWD1 = 0x108
        Script_Modify_Global_Variable_Variants_IWD1 = 0x109
        Spell_Remove_Protection_from_Spell_Variants_IWD1 = 0x10A
        Text_Protection_from_Display_Specific_String_Variants_IWD1 = 0x10B
        Spell_Effect_Clear_Fog_of_War_Wizard_Eye_Variants_IWD1 = 0x10C
        Spell_Effect_Shake_Window_Variants_IWD1 = 0x10D
        Cure_Unpause_Target_Variants_IWD1 = 0x10E
        Graphics_Avatar_Removal_Variants_IWD1 = 0x10F
        Spell_Apply_Repeating_EFF_Variants_IWD1 = 0x110
        Remove_Specific_Area_Effect_Zone_of_Sweet_Air_Variants_IWD1 = 0x111
        Spell_Effect_Teleport_to_Target_Variants_IWD1 = 0x112
        Stat_Hide_in_Shadows_Modifier_Variants_IWD1 = 0x113
        Stat_Detect_Illusion_Modifier_Variants_IWD1_IWD2 = 0x114
        Stat_Set_Traps_Modifier_Variants_IWD1 = 0x115
        Stat_To_Hit_Modifier_Variants_IWD1 = 0x116
        Button_Enable_Button_Variants_IWD1 = 0x117
        Spell_Effect_Wild_Magic_Variants_IWD1 = 0x118
        Stat_Wild_Magic_Variants_IWD1 = 0x119
        Script_Scripting_State_Modifier_Variants_IWD1 = 0x11A
        Use_EFF_File_Cursed_Variants_BG2_IWD1 = 0x11B
        Stat_Melee_THAC0_Modifier_Variants_IWD1 = 0x11C
        Stat_Melee_Weapon_Damage_Modifier_Variants_IWD1 = 0x11D
        Stat_Missile_Weapon_Damage_Modifier_Variants_IWD1 = 0x11E
        Graphics_Selection_Circle_Removal_Variants_IWD1 = 0x11F
        Stat_Fist_THAC0_Modifier_Variants_IWD1_IWD2 = 0x120
        Stat_Fist_Damage_Modifier_Variants_IWD1_IWD2 = 0x121
        Text_Change_Title_Variants_IWD1_IWD2 = 0x122
        Graphics_Disable_Visual_Effect_Variants_IWD1_IWD2 = 0x123
        Protection_Backstab_Variants_IWD1 = 0x124
        Script_Enable_Offscreen_AI_Variants_IWD1 = 0x125
        Spell_Effect_Existance_Delay_Override_Variants_IWD1 = 0x126
        Graphics_Disable_Permanent_Death_Variants_IWD1 = 0x127
        Graphics_Protection_from_Specific_Animation_Variants_IWD1 = 0x128
        Spell_Effect_Immunity_to_Turn_Undead_Variants_IWD2 = 0x129
        Spell_Effect_Execute_Script_cut250a_Variants_IWD2 = 0x12A
        Spell_Effect_Chaos_Shield = 0x12B
        Spell_Effect_NPCBump = 0x12C
        Stat_Critical_Hit_Modifier_Variants_BG2 = 0x12D
        Item_Can_Use_Any_Item = 0x12E
        Spell_Effect_Backstab_Every_Hit = 0x12F
        Mass_Raise_Dead = 0x130
        Stat_THAC0_Modifier_Off_Hand = 0x131
        Stat_THAC0_Modifier_On_Hand = 0x132
        Ranger_Tracking_Ability = 0x133
        Protection_From_Tracking = 0x134
        Script_Modify_Local_Variable = 0x135
        Protection_from_Timestop = 0x136
        Spell_Random_Wish_Spell = 0x137
        Crash = 0x138
        High_Level_Ability_Denotation = 0x139
        Spell_Golem_Stoneskin = 0x13A
        Graphics_Animation_Removal = 0x13B
        Spell_Magical_Rest = 0x13C
        State_Haste_2 = 0x13D
        Unused = 0x13E
        Usability_Item_Usability = 0x13F
        Change_Weather = 0x140
        Removal_Effects_specified_by_Resource = 0x141
        Unused_1 = 0x142
        Stat_Turn_Undead_Level = 0x143
        Protection_Immunity_Spell_and_Message = 0x144
        Stat_Save_vs_all = 0x145
        Add_Effects_List = 0x146
        Graphics_Icewind_Visual_Spell_Hit_plays_sound = 0x147
        State_Set_State = 0x148
        Spell_Effect_Slow_Poison = 0x149
        Text_Float_Text = 0x14A
        Summon_Random_Monster_Summoning = 0x14B
        Stat_Specific_Damage_Modifier = 0x14C
        Spell_Effect_Static_Charge = 0x14D
        Spell_Effect_Turn_Undead = 0x14E
        Spell_Effect_Seven_Eyes = 0x14F
        Graphics_Display_Eyes_Overlay = 0x150
        Remove_Opcode = 0x151
        Disable_Rest = 0x152
        Alter_Animation = 0x153
        Spell_Effect_Change_Backstab_Effect = 0x154
        Spell_Effect_Change_Critical_Hit_Effect = 0x155
        Animation_Override_Data = 0x156
        HP_Swap = 0x157
        Enchantment_vs_creature_type = 0x158
        Enchantment_bonus = 0x159
        Save_vs_school_bonus = 0x15A
        Unused_2 = 0x15B
        Unused_3 = 0x15C
        Unused_4 = 0x15D
        Unused_5 = 0x15E
        Unused_6 = 0x15F
        Unused_7 = 0x160
        Unused_8 = 0x161
        Unused_9 = 0x162
        Unused_10 = 0x163
        Unused_11 = 0x164
        Unused_12 = 0x165
        Unused_13 = 0x166
        Unused_14 = 0x167
        Stat_Ignore_Reputation_Breaking_Point = 0x168
        Cast_spell_on_critical_miss = 0x169
        Critical_miss_bonus = 0x16A
        Movement_rate_check = 0x16B
        Unused_15 = 0x16C
        Make_unselectable = 0x16D
        Spell_Apply_Spell_On_Move = 0x16E
        Minimum_base_stats = 0x16F
        