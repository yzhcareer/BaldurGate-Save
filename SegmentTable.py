from enum import Enum
from Tables import Tables
import re


class BaseOps:
    
    @staticmethod
    def bytes2Num(barray, signed=False, order='little'):
        return int.from_bytes(barray, signed=signed, byteorder=order)
    
    @staticmethod
    def num2Bytes(num, length, signed=False, order='little'):
        return num.to_bytes(length, signed=signed, byteorder=order)
    
    
class BaseTable(BaseOps, Enum):
    
    def __init__(self, *params): 
        _len = len(params)
        self.position = params[0]
        self.length = params[1]
        self.end = self.position + self.length
        self.signed = params[2] if _len > 2 else False
        self.order = params[3] if _len > 3 else 'little'
        self.table = params[4] if _len > 4 else None
        self.optimum = params[5] if _len > 5 else None
        
    def getBytes(self, buffer, mismatch=0):
        return buffer[mismatch + self.position:
                      mismatch + self.end]
    
    def getValue(self, buffer, mismatch=0):
        return self.bytes2Num(self.getBytes(buffer, mismatch),
                              self.signed,
                              self.order)
    
    def getString(self, buffer, mismatch=0):
        _s = self.getBytes(buffer, mismatch)
        for _i, _c in enumerate(_s):
            if _c < 32 or _c > 127:
                return str(_s[:_i], encoding='UTF-8')
        
    def setValue(self, buffer, new_value, mismatch=0):
        if isinstance(new_value, Enum):
            new_value = new_value.value
        buffer[mismatch + self.position: 
               mismatch + self.end] = self.num2Bytes(new_value,
                                                     self.length,
                                                     self.signed,
                                                     self.order) 
    
    def incValue(self, buffer, inc_value, mismatch=0):
        self.setValue(buffer, self.getValue(buffer, mismatch) + inc_value, mismatch)

    def getRepr(self, buffer, mismatch=0, parent=Tables):
        _value = self.getValue(buffer, mismatch)
        if self.table:
            try:
                return getattr(parent, self.table)(_value).name
            except ValueError:
                return '0x{0:08X}'.format(_value)               
        else:
            return str(_value)
        
    def optimize(self, buffer, mismatch=0):
        if self.optimum is not None:
            self.setValue(buffer, self.optimum, mismatch) 
            
            
class Segments(BaseTable):
    
    EXP = (0x0018, 4, False, 'little', None, 30000000)
    Gold = (0x001c, 4, False, 'little', None, 10000)
    States = (0x0020, 4, False, 'little', 'State', None)
    MaxHP = (0x0024, 2, False, 'little', None, 200)
    CurrentHP = (0x0026, 2, False, 'little', None, 200)
    Reputation = (0x0044, 1, True, 'little', None, 20)
    HideInShadow = (0x0045, 1, False, 'little', None, 250)
    NatureAC = (0x0046, 2, True, 'little', None, -10)
    EffectiveAC = (0x0048, 2, True, 'little', None, -10)
    CrushAC = (0x004A, 2, True, 'little', None, -10)
    MissileAC = (0x004C, 2, True, 'little', None, -10)
    PiercingAC = (0x004E, 2, True, 'little', None, -10)
    SlashingAC = (0x0050, 2, True, 'little', None, -10)
    THAC0 = (0x0052, 1, False, 'little', None, 0)
    NumOfAttack = (0x0053, 1, False, 'little', None, 10)
    SaveVsDeath = (0x0054, 1, False, 'little', None, 0)
    SaveVsWands = (0x0055, 1, False, 'little', None, 0)
    SaveVsPolymorph = (0x0056, 1, False, 'little', None, 0)
    SaveVsBreath = (0x0057, 1, False, 'little', None, 0)
    SaveVsSpell = (0x0058, 1, False, 'little', None, 0)
    ResistFire = (0x0059, 1, False, 'little', None, 100)
    ResistCold = (0x005A, 1, False, 'little', None, 100)
    ResistElectricity = (0x005B, 1, False, 'little', None, 100)
    ResistAcid = (0x005C, 1, False, 'little', None, 100)
    ResistMagic = (0x005D, 1, False, 'little', None, 100)
    ResistMagicFire = (0x005E, 1, False, 'little', None, 100)
    ResistMagicCold = (0x005F, 1, False, 'little', None, 100)
    ResistSlashing = (0x0060, 1, False, 'little', None, 100)
    ResistCrushing = (0x0061, 1, False, 'little', None, 100)
    ResistPiercing = (0x0062, 1, False, 'little', None, 100)
    ResistMissile = (0x0063, 1, False, 'little', None, 100)
    DetectIllusion = (0x0064, 1, False, 'little', None, 250)
    SetTraps = (0x0065, 1, False, 'little', None, 250)
    Lore = (0x0066, 1, False,'little',  None, 100)
    Lockpicking = (0x0067, 1, False, 'little', None, 250)
    Stealth = (0x0068, 1,False, 'little',  None, 250)
    FindTraps = (0x0069, 1, False, 'little',None, 250)
    PickPockets = (0x006A, 1, False, 'little', None, 250)
    Fatigue = (0x006B, 1,False, 'little',  None, 0)
    Intoxication = (0x006C, 1, False, 'little', None, 0)
    Luck = (0x006D, 1, False, 'little', None,  100)
    #LSwordPro = (0x006E, 1, False, 'little', None, 5)
    #SSwordPro = (0x006F, 1, False, 'little', None, 5)
    #BowPro = (0x0070, 1, False, 'little', None, 5)
    #SpearPro = (0x0071, 1, False, 'little', None, 5)
    #BluntPro = (0x0072, 1, False, 'little', None, 5)
    #SpikedPro = (0x0073, 1, False, 'little', None, 5)
    #AxePro = (0x0074, 1, False, 'little', None, 5)
    #MissilePro = (0x0075, 1, False, 'little', None, 5)
    #UnusedPro1 = (0x0076, 1, False, 'little', None, 5)
    #UnusedPro2 = (0x0077, 1, False, 'little', None, 5)
    #UnusedPro3 = (0x0078, 1, False, 'little', None, 5)
    #UnusedPro4 = (0x0079, 1, False, 'little', None, 5)
    #UnusedPro5 = (0x007a, 1, False, 'little', None, 5)
    #UnusedPro6 = (0x007b, 1, False, 'little', None, 5)
    #UnusedPro7 = (0x007c, 1, False, 'little', None, 5)
    #NightMareMode = (0x007d, 1, False, 'little', None, None)
    #Translucency = (0x007e, 1, False, 'little', None, None)
    #MurderInc = (0x007f, 1, False, 'little', None, None)
    #ReputationJoin = (0x0080, 1, False, 'little', None, None)
    #ReputationLeave = (0x0081, 1, False, 'little', None, None)
    TurnUndead = (0x0082, 1, False, 'little', None, 100)
    Tracking = (0x0083, 1, False, 'little', None, 100)
    LvClass1 = (0x0234, 1, False, 'little', None, 1)
    LvClass2 = (0x0235, 1, False, 'little', None, 1)
    LvClass3 = (0x0236, 1, False, 'little', None, 1)
    Sex = (0x0237, 1, False, 'little', 'Gender', None)
    Strength = (0x0238, 1, False, 'little', None, 25)
    StrBonus = (0x0239, 1, False, 'little', None, 0)
    Intelligence = (0x023A, 1, False, 'little', None, 25)
    Wisdom = (0x023B, 1, False, 'little', None, 25)
    Dexterity = (0x023C, 1, False, 'little', None, 25)
    Constitution = (0x023D, 1, False, 'little', None, 25)
    Charisma = (0x023E, 1, False, 'little', None, 25)
    Morale = (0x023F, 1, False, 'little', None, 100)
    MoraleBreak = (0x0240, 1, False, 'little', None, 0)
    RacialEnemy = (0x0241, 1, False, 'little', 'Race', None)
    MoraleRecovery = (0x0242, 2, False, 'little', None, 0)
    Kit = (0x0244, 4, False, 'little', 'Kit', None)
    ScriptOverride = (0x0248, 8, False, 'little', 'Script', None)
    ScriptClass = (0x0250, 8, False, 'little', 'Script', 20619443365495874)
    ScriptRace = (0x0258, 8, False, 'little', 'Script', None)
    ScriptGeneral = (0x0260, 8, False, 'little', 'Script', None)
    ScriptDefault = (0x0268, 8, False, 'little', 'Script', None)
    Race = (0x0272, 1, False, 'little', 'Race', None)
    Class = (0x0273, 1, False, 'little', 'Class', None)
    Gender = (0x0275, 1, False, 'little', 'Gender', None)
    Alignment = (0x027B, 1, False, 'little', 'Alignment', None)
    #KnownSpellOffset = (0x02a0, 4, False, 'little', None, None)
    #KnownSpellCount = (0x02a4, 4, False, 'little', None, None)
    #MemSpellOffset = (0x02a8, 4, False, 'little', None, None)
    #MemSpellCount = (0x02ac, 4, False, 'little', None, None)
    #MemorizedSpellOffset = (0x02b0, 4, False, 'little', None, None)
    #MemorizedSpellCount = (0x02b4, 4, False, 'little', None, None)
    #ItemSlotOffset = (0x02b8, 4, False, 'little', None, None)
    #ItemOffset = (0x02bc, 4, False, 'little', None, None)
    #ItemCount = (0x02c0, 4, False, 'little', None, None)
    #EffectOffset = (0x02c4, 4, False, 'little', None, None)
    #EffectCount = (0x02c8, 4, False, 'little', None, None)
    #DialogRef = (0x02cc, 8, False, 'little', None, None)